# GeoInsight Agent — Product Requirements Document (PRD)

> Related docs: [project_proposal.md](./project_proposal.md) · [system_design.md](./system_design.md) · [data.md](./data.md)

| | |
|---|---|
| **Product** | GeoInsight Agent — AI-powered natural language interface for IMOS geospatial data |
| **Status** | Draft |
| **Owner** | Leo Li (Data Engineer) |
| **Target** | POC in 9–11 weeks (+2 weeks buffer recommended) |

## 1. Problem Statement

IMOS/AODN hosts hundreds of ocean datasets (Zarr/Parquet on S3), but exploring them requires knowing the catalog, understanding data formats (NetCDF/Zarr conventions, chunking, CRS), and writing Python. Scientists, students, and policy users without these skills cannot self-serve. Even technical users spend significant time on dataset discovery and boilerplate slicing/plotting code.

## 2. Goals & Success Metrics

| Goal | Metric | Target (POC) |
|---|---|---|
| Accurate dataset discovery | Recall@5 on golden query set (~30 queries) | ≥ 85% |
| Correct entity resolution | Place/time/variable extraction accuracy on test set | ≥ 90% |
| Trustworthy answers | Hallucinated dataset names / S3 paths | 0 (grounded in KB only) |
| Usable visualization | E2E success rate on scripted SST scenarios | ≥ 80% |
| Responsiveness | Discovery answer latency / plot latency | < 10 s / < 60 s |
| Safety | Prompt-injection test suite pass rate | 100% blocked |

### Non-Goals (POC)
- Real-time/streaming data; data ingestion pipelines; predictive modelling
- Model fine-tuning (deferred — prompt engineering only)
- Multilingual support; multi-dataset regridding/comparison (architecture leaves a hook, not implemented)
- Write access of any kind

## 3. Users & Personas

| Persona | Need | Example |
|---|---|---|
| **Marine researcher (non-dev)** | Find and preview datasets for a region/variable without code | "What SST datasets cover Storm Bay?" |
| **Data-savvy scientist** | Fast exploratory plots before deep analysis | "Plot daily-mean SST for Storm Bay, past 7 days" |
| **IMOS portal user (public/policy)** | Plain-language answers about ocean observations | "Is the water near Hobart warmer than usual?" (graceful partial answer) |
| **AODN engineer (internal)** | Verify catalog metadata quality via conversational probing | Direct `/datasets/search` access |

## 4. User Stories & Requirements

### Epic A — Dataset Discovery (Milestone 1)
| ID | Story | Priority | Acceptance Criteria |
|---|---|---|---|
| A1 | As a user, I can ask in natural language what datasets exist for a variable/region and get a ranked list | P0 | Returns dataset titles, spatial/temporal coverage, access status; grounded in KB; no fabricated entries |
| A2 | As a user, I can ask follow-up questions about a listed dataset (coverage, parameters, license) | P0 | Answers cite KB metadata fields |
| A3 | As a user, I'm told clearly when a dataset is discoverable but not queryable (no cloud-optimised version) | P0 | `queryable=false` datasets labelled; suggests alternatives |
| A4 | As a user, out-of-scope questions are politely declined | P0 | GuardRail blocks; explains the agent's scope |

### Epic B — Data Query & Visualization (Milestone 2)
| ID | Story | Priority | Acceptance Criteria |
|---|---|---|---|
| B1 | As a user, I can request a time-series plot for a variable + place + time range | P0 | Line chart PNG + caption with computed stats; correct bbox/time slice |
| B2 | As a user, I can request a spatial map for a variable at a time/period | P0 | Map (pcolormesh) with coastline context, correct extent and colorbar units |
| B3 | As a user, I can refine a previous request conversationally ("compare with previous month") | P1 | Session state reused; only changed entity re-resolved |
| B4 | As a user, oversized requests are refused with a suggested smaller scope | P0 | Size estimated from Zarr metadata pre-load; cap ~100 MB / 1M points |
| B5 | As a user, ambiguous place names trigger a clarifying question | P1 | Gazetteer returns candidates; agent asks rather than guesses |

### Epic C — Platform
| ID | Story | Priority | Acceptance Criteria |
|---|---|---|---|
| C1 | Chat UI (Gradio) with inline plot rendering and session history | P0 | Multi-turn session; images displayed inline |
| C2 | KB ingestion pipeline is repeatable and idempotent | P0 | One command rebuilds vector + catalog stores from `imos_results.json` + cloud-opt configs |
| C3 | All LLM tool calls restricted to a fixed parameterised toolbox | P0 | No code generation/execution path exists |
| C4 | Read-only S3 access enforced via IAM | P0 | Task role policy reviewed |
| C5 | Agent traces observable per session | P1 | LangSmith/Langfuse traces incl. token cost |

## 5. Functional Scope Detail

### 5.1 POC Datasets & Variables
- **AusTemp** Zarr on S3: Sea Surface Temperature, Degree Heating Days, Mosaic
- Discovery spans the full ~829-record AODN catalog; visualization limited to cloud-optimised datasets

### 5.2 Entity Resolution Rules
- **Time**: relative phrases ("past 7 days", "last month") resolved deterministically in code against query date — never by the LLM
- **Place**: gazetteer lookup returns polygon/bbox; "near X" applies a default buffer (configurable, e.g. 0.5°) and states the assumption in the answer
- **Variable**: mapped to AODN parameter vocabulary terms; unknown variables → clarifying question
- **Geospatial handling**: CRS normalisation, 0–360 vs ±180 longitude, dateline-crossing bboxes, and land masking handled in a deterministic `geo_utils` tool layer shared by all data agents

### 5.3 Out of Scope Behaviours
- No arbitrary code execution; no data download/export (plot artifacts only); no user accounts in POC

## 6. UX Requirements

- Single chat surface; assistant messages may contain text + image artifacts
- Every data answer states: dataset used, spatial/temporal slice applied, aggregation method
- Errors are conversational and actionable ("That range has no data; the dataset ends 2013-12. Try …")
- Loading states for long-running queries (>5 s)

## 7. Dependencies & Assumptions

| Dependency | Assumption | Risk if false |
|---|---|---|
| `data/raw/imos_results.json` | Representative, refreshable from AODN Elasticsearch | Stale KB → wrong discovery answers |
| `aodn_cloud_optimised` configs | Stable schema; mappable to catalog UUIDs | Manual mapping effort grows |
| AusTemp Zarr on S3 | Readable, consolidated metadata, documented chunking | Slicing perf degrades |
| AWS Bedrock access | Claude + embedding models available in region | Model substitution needed |
| Gazetteer source | IMOS GeoServer or bundled GeoNames extract (decision pending) | Place resolution blocked — resolve in Phase 1 |

## 8. Release Plan

| Release | Contents | Exit Criteria |
|---|---|---|
| **M1 — Discovery Agent** | KB ingestion + Supervisor + Discovery agent + minimal Gradio | Epic A done; recall@5 ≥ 85% |
| **M2 — Visualization Agent** | Zarr tools + geo_utils + Visualization agent | Epic B P0 done; E2E ≥ 80% on scripted scenarios |
| **M3 — Hardened POC** | Guardrails, eval suite, Docker/ECS deploy | All P0 criteria + safety suite pass |

## 9. Open Questions

1. Gazetteer source of truth — IMOS GeoServer vs. GeoNames extract? *(blocks B5, decide Phase 1)*
2. How many catalog records map to cloud-optimised configs? *(sizes the queryable set)*
3. PNG-only vs. interactive HTML for IMOS-Live portal embedding?
4. Bedrock model split: Claude for supervisor vs. Nova/Haiku for extraction — benchmark cost/latency.
5. Who fills the second team role (evaluation, MCP, security testing) named in the proposal?
