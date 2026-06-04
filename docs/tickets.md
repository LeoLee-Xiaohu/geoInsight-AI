# GeoInsight AI — Draft Tickets

> **Status:** Draft — review and edit before creating issues.
> Organised by epic (milestone) following the project proposal phases.

---

## Epic 1: Requirements & Data Setup

### TICKET-001 — Identify and Index IMOS Datasets
**Type:** Task
**Priority:** High
**Labels:** `data`, `setup`

**Description:**
Identify the IMOS datasets in scope for the POC (Sea Surface Temperature, Degree Heating Days, Mosaic) and document their S3 locations, formats (Zarr/Parquet), variable names, and CF-convention metadata.

**Acceptance Criteria:**
- [ ] S3 paths for AusTemp Zarr dataset (and any Parquet datasets) are documented
- [ ] Key variables listed: SST, Degree Heating Days, Mosaic
- [ ] CF-convention metadata fields noted (e.g., coordinate names, units)
- [ ] STAC catalogue compatibility assessed (optional)

---

## Epic 2: IMOS Knowledge Base

### TICKET-002 — Clean and Prepare IMOS Metadata
**Type:** Task
**Priority:** High
**Labels:** `knowledge-base`, `data`

**Description:**
Clean raw IMOS dataset metadata and create a structured index suitable for embedding. Include dataset descriptions, variable names, spatial extents, temporal coverage, and named geographic regions (e.g., Storm Bay lat/lon bbox).

**Acceptance Criteria:**
- [ ] Metadata cleaned and normalised to a consistent schema
- [ ] Geographic region dictionary (e.g., Australian coastal bays) included
- [ ] Metadata index exported as a structured file (JSON/CSV)

---

### TICKET-003 — Build Vector Knowledge Base (RAG)
**Type:** Feature
**Priority:** High
**Labels:** `knowledge-base`, `rag`, `ai`

**Description:**
Embed the cleaned IMOS metadata using an embedding model (AWS Bedrock or compatible) and store it in a vector database for retrieval-augmented generation (RAG).

**Acceptance Criteria:**
- [ ] Embedding pipeline implemented and tested
- [ ] Vector store populated with IMOS metadata chunks
- [ ] Basic similarity search returns correct datasets for sample queries (e.g., "sea surface temperature Storm Bay")

---

### TICKET-004 — Geolocation Lookup Service
**Type:** Feature
**Priority:** Medium
**Labels:** `knowledge-base`, `geospatial`

**Description:**
Implement a geolocation resolver that maps natural place names (e.g., "Storm Bay", "Great Barrier Reef") to lat/lon bounding boxes using IMOS GeoServer, GeoNames API, or a custom lookup table.

**Acceptance Criteria:**
- [ ] Resolver returns bbox for known IMOS-relevant locations
- [ ] Falls back gracefully when a location is not found
- [ ] Integrated into agent context retrieval

---

## Epic 3: LLM Agent Core

### TICKET-005 — AWS Bedrock LLM Integration
**Type:** Feature
**Priority:** High
**Labels:** `ai`, `aws`, `infrastructure`

**Description:**
Set up and configure access to AWS Bedrock (Nova/Claude models) for use as the backbone LLM. Implement a thin client wrapper with error handling and retry logic.

**Acceptance Criteria:**
- [ ] AWS Bedrock client configured with appropriate IAM role/permissions
- [ ] Basic prompt/response round-trip tested
- [ ] Model ID and region parameterised via config (not hardcoded)

---

### TICKET-006 — Prompt Engineering for GeoInsight Agent
**Type:** Task
**Priority:** High
**Labels:** `ai`, `prompt-engineering`

**Description:**
Design and test initial system prompts and few-shot examples for the GeoInsight agent. Prompts should guide the LLM to extract: dataset name, variable, geographic region, time range, and visualisation type from user queries.

**Acceptance Criteria:**
- [ ] System prompt drafted and reviewed
- [ ] At least 5 few-shot examples covering SST, region, and time range extraction
- [ ] Prompt tested against sample queries with correct structured output
- [ ] Prompt injection / security edge cases documented

---

### TICKET-007 — LangGraph Agent Orchestration
**Type:** Feature
**Priority:** High
**Labels:** `ai`, `orchestration`

**Description:**
Implement the LangGraph-based agent workflow that orchestrates: intent parsing → knowledge base retrieval → data query → visualisation generation → response formatting. Follow the workflow diagram in the project proposal.

**Acceptance Criteria:**
- [ ] LangGraph state machine implemented with defined nodes and edges
- [ ] Agent correctly routes between knowledge-base retrieval and data-query tools
- [ ] Conversation context (multi-turn) preserved across interactions
- [ ] Unit tests for each node/tool

---

### TICKET-008 — MCP Integration for Context Management
**Type:** Feature
**Priority:** Medium
**Labels:** `ai`, `mcp`

**Description:**
Integrate Model Context Protocol (MCP) to manage tool calls and provide structured context to the LLM (dataset schemas, region metadata, previous turns).

**Acceptance Criteria:**
- [ ] MCP tool definitions created for knowledge-base lookup and data-fetch tools
- [ ] LLM correctly selects and invokes tools via MCP
- [ ] Context window usage stays within model limits for typical queries

---

## Epic 4: Data Access Layer

### TICKET-009 — S3 Zarr Dataset Loader
**Type:** Feature
**Priority:** High
**Labels:** `data`, `s3`, `zarr`

**Description:**
Implement a data access module that loads AusTemp Zarr datasets from S3 using `s3fs` and `xarray`. Support spatial (bbox) and temporal slicing, with aggregation/downsampling for large requests.

**Acceptance Criteria:**
- [ ] Zarr dataset opens successfully from S3 without downloading entirely
- [ ] Spatial slice by lat/lon bbox works correctly
- [ ] Temporal slice by date range works correctly
- [ ] Downsampling applied when data exceeds a configurable size threshold
- [ ] S3 access uses read-only IAM policy

---

### TICKET-010 — Parquet Dataset Loader (Optional)
**Type:** Feature
**Priority:** Low
**Labels:** `data`, `s3`, `parquet`

**Description:**
Implement a loader for Parquet datasets stored on S3 using `boto3` / `pandas` / `geopandas`. Supports filtering by spatial and temporal attributes where available.

**Acceptance Criteria:**
- [ ] Parquet file(s) readable from S3
- [ ] Column-level filtering works for time and region fields
- [ ] Integrated into the same data-access interface as the Zarr loader

---

## Epic 5: Visualisation

### TICKET-011 — Time Series Plot Generation
**Type:** Feature
**Priority:** High
**Labels:** `visualisation`

**Description:**
Implement a function that takes a sliced xarray DataArray and produces a time series line chart (PNG or HTML) using Matplotlib. Include title, axis labels, and a brief statistical summary (e.g., mean, trend).

**Acceptance Criteria:**
- [ ] Line chart generated for SST time series
- [ ] Chart includes title, axis labels with units, and date range
- [ ] Summary stats (mean, min, max) included in response text
- [ ] Output format is configurable (PNG / HTML)

---

### TICKET-012 — Spatial Map Plot Generation
**Type:** Feature
**Priority:** Medium
**Labels:** `visualisation`

**Description:**
Implement a function that produces a spatial heatmap/colourmap of a 2D geospatial variable (e.g., SST over a region) using Matplotlib and xarray.

**Acceptance Criteria:**
- [ ] Spatial plot renders with correct projection and bbox
- [ ] Colourbar with variable units included
- [ ] Handles missing/NaN values gracefully

---

## Epic 6: Frontend (Gradio POC)

### TICKET-013 — Gradio Chat Interface
**Type:** Feature
**Priority:** Medium
**Labels:** `frontend`, `ui`

**Description:**
Build a Gradio-based chat UI as the MVP front end. Users can type natural language queries, view text responses, and see generated plot images inline. Multi-turn conversation context should be maintained within a session.

**Acceptance Criteria:**
- [ ] Chat input/output renders correctly
- [ ] Plot images (PNG) display inline in the chat
- [ ] Session conversation history preserved across turns
- [ ] Basic error messages shown when agent cannot answer

---

## Epic 7: Backend & API

### TICKET-014 — FastAPI Backend Service
**Type:** Feature
**Priority:** Medium
**Labels:** `backend`, `api`

**Description:**
Implement a FastAPI service exposing endpoints for the GeoInsight agent: `POST /query` (accepts user message + session context, returns agent response + optional plot). Connects the Gradio UI to the LangGraph agent.

**Acceptance Criteria:**
- [ ] `POST /query` endpoint functional and documented (OpenAPI)
- [ ] Session/context ID threading works across requests
- [ ] Returns structured JSON with `message` and optional `plot_url` or base64 image
- [ ] Health check endpoint (`GET /health`) implemented

---

## Epic 8: Testing & Evaluation

### TICKET-015 — Agent Evaluation & Prompt Coverage
**Type:** Task
**Priority:** Medium
**Labels:** `testing`, `ai`

**Description:**
Define an evaluation set of at least 20 diverse queries covering different datasets, regions, time ranges, and visualisation types. Score the agent on intent extraction accuracy, correct dataset selection, and visualisation correctness.

**Acceptance Criteria:**
- [ ] Evaluation dataset of ≥20 queries created
- [ ] Scoring rubric defined (intent, dataset, region, time, plot type)
- [ ] Baseline scores recorded
- [ ] Gaps used to improve prompts or RAG retrieval

---

### TICKET-016 — Security & Prompt Injection Hardening
**Type:** Task
**Priority:** High
**Labels:** `security`

**Description:**
Review and harden the agent against prompt injection attacks. Enforce S3 read-only access policies. Validate and sanitise all LLM-generated code/queries before execution.

**Acceptance Criteria:**
- [ ] Prompt injection test cases documented and passing
- [ ] S3 IAM policy limited to read-only on relevant buckets
- [ ] No user-supplied strings passed directly to `exec`/`eval`
- [ ] Secrets managed via AWS Secrets Manager (no hardcoded keys)

---

## Epic 9: Deployment

### TICKET-017 — Dockerise Application
**Type:** Task
**Priority:** Medium
**Labels:** `deployment`, `docker`

**Description:**
Create Dockerfiles for the FastAPI backend and Gradio frontend. Build a `docker-compose.yml` for local development.

**Acceptance Criteria:**
- [ ] `Dockerfile` builds successfully for backend and frontend
- [ ] `docker-compose up` starts both services locally
- [ ] Environment variables externalised via `.env` / AWS Secrets Manager

---

### TICKET-018 — Deploy to AWS ECS / Lambda
**Type:** Task
**Priority:** Medium
**Labels:** `deployment`, `aws`

**Description:**
Deploy the Dockerised application to AWS ECS (Fargate) or Lambda. Set up ECR for image hosting. Optionally use Terraform for infrastructure-as-code.

**Acceptance Criteria:**
- [ ] Container image pushed to ECR
- [ ] ECS service (or Lambda function) running and reachable
- [ ] CloudWatch logging enabled
- [ ] Terraform config checked in (optional but recommended)

---

## Milestone Summary

| Milestone | Tickets | Target Duration |
|---|---|---|
| M1: IMOS Knowledge Base Agent | TICKET-001 to TICKET-008 | ~5–7 weeks |
| M2: Data Visualisation AI Agent | TICKET-009 to TICKET-018 | ~4–5 weeks |
| **Total** | **18 tickets** | **~9–11 weeks** |
