# GeoInsight AI — Draft Tickets

> **Status:** Draft — review and edit before creating issues.
> Organised by epic (milestone) following the project proposal phases.

---

## Epic 1: Requirements & Data Setup

### TICKET-001 — Identify and Index IMOS Datasets

**Type:** Task | **Priority:** High | **Labels:** `data`, `setup`

## User Story

**AS A** data engineer setting up the GeoInsight POC

**I WANT** a complete inventory of IMOS datasets in scope with their S3 locations, formats, and metadata fields

**SO THAT** downstream data loaders and the knowledge base can be built on a well-understood foundation

## Acceptance Criteria
1. S3 paths for AusTemp Zarr dataset (and any Parquet datasets) are documented
2. Key variables listed: SST, Degree Heating Days, Mosaic
3. CF-convention metadata fields noted (e.g., coordinate names, units)
4. STAC catalogue compatibility assessed (optional)

## Notes
1. Datasets in scope: Sea Surface Temperature, Degree Heating Days, Mosaic
2. Formats: Zarr and Parquet stored on S3

## Tasks
- [ ] Enumerate all IMOS datasets in scope with S3 paths
- [ ] Document variable names and CF-convention metadata fields
- [ ] Note data formats (Zarr/Parquet) and access patterns
- [ ] Assess STAC catalogue compatibility
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. Access to IMOS S3 buckets

## Demo
1. Present the dataset inventory document listing S3 paths, variables, and metadata fields for all in-scope datasets

---

## Epic 2: IMOS Knowledge Base

### TICKET-002 — Clean and Prepare IMOS Metadata

**Type:** Task | **Priority:** High | **Labels:** `knowledge-base`, `data`

## User Story

**AS A** data engineer preparing the IMOS knowledge base

**I WANT** cleaned and normalised IMOS dataset metadata indexed in a consistent schema

**SO THAT** the metadata can be reliably embedded into a vector store for accurate RAG retrieval

## Acceptance Criteria
1. Metadata cleaned and normalised to a consistent schema
2. Geographic region dictionary (e.g., Australian coastal bays including Storm Bay lat/lon bbox) included
3. Metadata index exported as a structured file (JSON/CSV) ready for embedding

## Notes
1. Include dataset descriptions, variable names, spatial extents, temporal coverage, and named geographic regions
2. Source data from IMOS Elasticsearch metadata
3. Prerequisite for TICKET-003 (Build Vector Knowledge Base)

## Tasks
- [ ] Extract raw IMOS dataset metadata from Elasticsearch
- [ ] Define and implement a normalised metadata schema
- [ ] Clean and transform raw metadata to conform to the schema
- [ ] Build geographic region dictionary (Australian coastal bays, e.g. Storm Bay, Great Barrier Reef)
- [ ] Export cleaned metadata index as JSON/CSV
- [ ] Validate output against schema and sample queries
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-001 — IMOS dataset inventory completed
2. Access to IMOS Elasticsearch metadata endpoint

## Demo
1. Show normalised metadata file with sample entries covering description, variables, spatial/temporal extents, and geographic regions

---

### TICKET-003 — Build Vector Knowledge Base (RAG)

**Type:** Feature | **Priority:** High | **Labels:** `knowledge-base`, `rag`, `ai`

## User Story

**AS AN** AI agent developer

**I WANT** IMOS metadata embedded and stored in a vector database

**SO THAT** the GeoInsight agent can retrieve the most relevant datasets via semantic similarity search

## Acceptance Criteria
1. Embedding pipeline implemented and tested
2. Vector store populated with IMOS metadata chunks
3. Basic similarity search returns correct datasets for sample queries (e.g., "sea surface temperature Storm Bay")

## Notes
1. Use AWS Bedrock or a compatible embedding model
2. Chunk metadata records appropriately before embedding
3. Prerequisite for TICKET-007 (LangGraph Agent Orchestration)

## Tasks
- [ ] Select and configure embedding model (AWS Bedrock or compatible)
- [ ] Implement chunking strategy for metadata records
- [ ] Build embedding pipeline and run against cleaned metadata
- [ ] Populate vector store with embedded chunks
- [ ] Test similarity search with sample queries
- [ ] Document vector store schema and access pattern
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-002 — Cleaned metadata index available

## Demo
1. Run sample query "sea surface temperature Storm Bay" and show top-ranked retrieved metadata chunks

---

### TICKET-003a — Implement Metadata Chunking Strategy

**Type:** Task | **Priority:** High | **Labels:** `knowledge-base`, `rag`

## User Story

**AS A** data engineer building the IMOS knowledge base

**I WANT** a well-defined chunking strategy that breaks each IMOS metadata record into embeddable text units

**SO THAT** each chunk carries enough context for semantic retrieval while staying within embedding model token limits

## Acceptance Criteria
1. Each metadata record is split into one or more text chunks according to a documented strategy
2. Every chunk carries structured fields: `dataset_id`, `variable`, `bbox`, `temporal_coverage`, `source_record`
3. Unit tests cover single-variable records, multi-variable records, and records with missing optional fields
4. Chunking output is a deterministic, serialisable list (JSON) given the same input

## Notes
1. Chunk size should be tuned to the token limit of the selected embedding model (from TICKET-003 ADR)
2. Overlap between chunks is optional; document the decision either way
3. This is a prerequisite for TICKET-003c (Embedding Ingestion Pipeline)

## Tasks
- [ ] Define chunking schema (fields per chunk, overlap policy, max token budget)
- [ ] Implement `chunk_metadata_record(record) -> List[Chunk]` function
- [ ] Write unit tests for normal, edge, and missing-field cases
- [ ] Serialise chunks to JSON and validate against schema
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-003 — Embedding model selected and token limit known
2. TICKET-002 — Cleaned metadata index available

## Demo
1. Show chunked output for the AusTemp SST dataset record, with all required structured fields present

---

### TICKET-003b — Bootstrap Vector Store with Schema

**Type:** Task | **Priority:** High | **Labels:** `knowledge-base`, `rag`, `infrastructure`

## User Story

**AS A** data engineer preparing the IMOS knowledge base

**I WANT** a running vector store instance with a defined collection schema

**SO THAT** the embedding ingestion pipeline has a stable target to write to and the retrieval function has a stable source to read from

## Acceptance Criteria
1. Vector store instance is initialised and reachable (locally or on AWS)
2. Collection is created with the correct schema: embedding vector, `dataset_id`, `variable`, `bbox`, `temporal_coverage`, `chunk_text`
3. An empty similarity query executes without error and returns an empty result set
4. Setup is reproducible via a script or config file (no manual console steps)

## Notes
1. Technology follows the decision in TICKET-003 ADR (e.g., FAISS, AWS OpenSearch Serverless, or pgvector)
2. Local and cloud configurations should be separated by environment variable
3. This is a prerequisite for TICKET-003c (Embedding Ingestion Pipeline)

## Tasks
- [ ] Provision or initialise vector store instance for the chosen technology
- [ ] Define and create collection/index with required schema
- [ ] Verify empty query executes and returns correctly
- [ ] Write setup script or configuration file for reproducible initialisation
- [ ] Document connection details and environment variables in README
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-003 — Vector store technology decided

## Demo
1. Run setup script, show collection exists, and execute an empty query that returns zero results without error

---

### TICKET-003c — Build Embedding Ingestion Pipeline

**Type:** Feature | **Priority:** High | **Labels:** `knowledge-base`, `rag`, `ai`

## User Story

**AS A** data engineer populating the IMOS knowledge base

**I WANT** an ingestion pipeline that reads cleaned metadata, chunks it, embeds each chunk, and upserts it into the vector store

**SO THAT** the vector store is fully populated and ready for semantic retrieval

## Acceptance Criteria
1. Pipeline reads cleaned metadata JSON/CSV produced by TICKET-002
2. Each record is chunked using the strategy from TICKET-003a
3. Embedding API is called for each chunk using the model from TICKET-003
4. Chunks are upserted into the vector store (TICKET-003b); re-running the pipeline does not create duplicates
5. Pipeline logs progress and surfaces errors without crashing the full run
6. At least the AusTemp SST dataset is successfully ingested end-to-end

## Notes
1. Use idempotent upsert (not insert) so the pipeline can be re-run safely after metadata updates
2. Batch API calls to the embedding model where the provider supports it
3. This is a prerequisite for TICKET-003d (Semantic Retrieval Function)

## Tasks
- [ ] Implement pipeline entrypoint: read metadata → chunk → embed → upsert
- [ ] Add idempotency: use `dataset_id` + chunk index as document key
- [ ] Implement batched embedding API calls
- [ ] Add progress logging and per-record error handling
- [ ] Run pipeline against full cleaned metadata index and verify record count in vector store
- [ ] Write integration test using a small fixture dataset (2–3 records)
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-003a — Chunking strategy implemented
2. TICKET-003b — Vector store bootstrapped with schema
3. TICKET-002 — Cleaned metadata index available

## Demo
1. Run pipeline against the AusTemp SST metadata record; show the resulting chunk count and one sample document in the vector store

---

### TICKET-003d — Implement Semantic Retrieval Function

**Type:** Feature | **Priority:** High | **Labels:** `knowledge-base`, `rag`, `ai`

## User Story

**AS AN** AI agent receiving a natural language query

**I WANT** a retrieval function that embeds the query and returns the most relevant IMOS metadata chunks

**SO THAT** the agent can ground its dataset discovery responses in factual, ranked metadata

## Acceptance Criteria
1. `retrieve(query: str, top_k: int) -> List[MetadataChunk]` is implemented and callable
2. Query "sea surface temperature Storm Bay" returns the AusTemp SST dataset chunk in the top 3 results
3. Function returns an empty list (not an error) when the vector store contains no relevant matches
4. Integration test covers at least 3 diverse queries and asserts expected datasets appear in top-k results

## Notes
1. Embed the query using the same model as the ingestion pipeline
2. Return full chunk metadata (not just text) so callers have `dataset_id`, `variable`, `bbox`, etc.
3. `top_k` should be configurable; default of 5 is a reasonable starting point

## Tasks
- [ ] Implement `retrieve(query, top_k)` using the vector store client
- [ ] Ensure query is embedded with the same model used during ingestion
- [ ] Return structured `MetadataChunk` objects including all schema fields
- [ ] Handle empty-result and connection-error cases gracefully
- [ ] Write integration tests with at least 3 sample queries
- [ ] Document function signature and expected output format
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-003c — Vector store populated with embedded chunks

## Demo
1. Call `retrieve("sea surface temperature Storm Bay", top_k=5)` and show the AusTemp SST chunk ranked in the top 3 results

---

### TICKET-003e — Build Retrieval Evaluation Harness

**Type:** Task | **Priority:** Medium | **Labels:** `knowledge-base`, `rag`, `testing`

## User Story

**AS AN** AI agent developer

**I WANT** an evaluation harness that scores retrieval quality against a fixed query set

**SO THAT** I can track a baseline and detect regressions when the embedding model, chunking, or metadata changes

## Acceptance Criteria
1. At least 10 evaluation queries are defined, each with one or more expected `dataset_id` values
2. Harness computes precision@k (k=3 and k=5) for each query and reports mean scores
3. Baseline results are recorded in a versioned file committed to the repository
4. Harness can be re-run in CI or locally without manual steps

## Notes
1. Queries should cover: SST, Degree Heating Days, Mosaic, named regions (Storm Bay, Great Barrier Reef), variable synonyms (e.g., "heat stress"), and time-range phrasing
2. Record baseline before any prompt or retrieval tuning so the file serves as a regression reference
3. A simple script that prints results to stdout and writes a JSON results file is sufficient for the proof-of-concept phase

## Tasks
- [ ] Define 10+ evaluation queries with expected `dataset_id` ground truth
- [ ] Implement harness script: run each query through `retrieve()`, compare results to ground truth
- [ ] Compute and report precision@3 and precision@5
- [ ] Write baseline results to a versioned JSON file in the repository
- [ ] Document how to run the harness in the README
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-003d — Semantic retrieval function implemented

## Demo
1. Run the harness and show the printed precision@3 and precision@5 scores alongside the committed baseline results file

---

### TICKET-004 — Geolocation Lookup Service

**Type:** Feature | **Priority:** Medium | **Labels:** `knowledge-base`, `geospatial`

## User Story

**AS AN** AI agent receiving a natural language query

**I WANT** a geolocation resolver that maps place names to lat/lon bounding boxes

**SO THAT** the agent can translate user-supplied region names into spatial coordinates for data queries

## Acceptance Criteria
1. Resolver returns bbox for known IMOS-relevant locations
2. Falls back gracefully when a location is not found
3. Integrated into agent context retrieval

## Notes
1. Sources to consider: IMOS GeoServer, GeoNames API, or a custom lookup table
2. Must handle common Australian marine regions (e.g., Storm Bay, Great Barrier Reef, Coral Sea)

## Tasks
- [ ] Evaluate and select geolocation source (GeoServer / GeoNames / custom table)
- [ ] Implement resolver function: place name → lat/lon bbox
- [ ] Build fallback behaviour for unknown locations
- [ ] Populate lookup table with IMOS-relevant Australian regions
- [ ] Integrate resolver into agent context retrieval flow
- [ ] Unit test resolver with known and unknown place names
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-002 — Geographic region dictionary from metadata preparation

## Demo
1. Demonstrate resolver returning correct bbox for "Storm Bay" and a graceful fallback message for an unknown location

---

## Epic 3: LLM Agent Core

### TICKET-005 — AWS Bedrock LLM Integration

**Type:** Feature | **Priority:** High | **Labels:** `ai`, `aws`, `infrastructure`

## User Story

**AS A** backend developer building the GeoInsight agent

**I WANT** a configured and tested AWS Bedrock LLM client wrapper

**SO THAT** all agent components can send prompts and receive structured responses reliably

## Acceptance Criteria
1. AWS Bedrock client configured with appropriate IAM role/permissions
2. Basic prompt/response round-trip tested
3. Model ID and region parameterised via config (not hardcoded)

## Notes
1. Target models: Nova / Claude via AWS Bedrock
2. Implement error handling and retry logic in the wrapper
3. Config should be driven by environment variables or a config file

## Tasks
- [ ] Set up AWS Bedrock IAM role with least-privilege permissions
- [ ] Implement thin client wrapper around Bedrock API
- [ ] Add error handling and retry logic
- [ ] Parameterise model ID and AWS region via config
- [ ] Write integration test for basic prompt/response round-trip
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. AWS account and Bedrock model access approved

## Demo
1. Show a successful prompt/response round-trip to Bedrock returning a structured answer to a sample geospatial query

---

### TICKET-006 — Prompt Engineering for GeoInsight Agent

**Type:** Task | **Priority:** High | **Labels:** `ai`, `prompt-engineering`

## User Story

**AS AN** AI agent developer

**I WANT** well-designed system prompts and few-shot examples for the GeoInsight agent

**SO THAT** the LLM reliably extracts structured intent (dataset, variable, region, time range, visualisation type) from natural language queries

## Acceptance Criteria
1. System prompt drafted and reviewed by the team
2. At least 5 few-shot examples covering SST, region, and time range extraction
3. Prompt tested against sample queries with correct structured output
4. Prompt injection / security edge cases documented

## Notes
1. Structured output fields: dataset name, variable, geographic region, time range, visualisation type
2. Security edge cases should feed into TICKET-016

## Tasks
- [ ] Draft initial system prompt
- [ ] Create ≥5 few-shot examples covering diverse query types
- [ ] Test prompt against sample queries and iterate
- [ ] Document prompt injection edge cases
- [ ] Review prompt with team and incorporate feedback
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-005 — Bedrock LLM client available for testing

## Demo
1. Run 5 sample queries through the prompt and show correctly structured JSON output for each

---

### TICKET-007 — LangGraph Agent Orchestration

**Type:** Feature | **Priority:** High | **Labels:** `ai`, `orchestration`

## User Story

**AS AN** end user asking a geospatial question

**I WANT** the GeoInsight agent to orchestrate intent parsing, knowledge retrieval, data querying, and visualisation in a coherent workflow

**SO THAT** I receive an accurate, contextual answer with a chart in a single interaction

## Acceptance Criteria
1. LangGraph state machine implemented with defined nodes and edges
2. Agent correctly routes between knowledge-base retrieval and data-query tools
3. Conversation context (multi-turn) preserved across interactions
4. Unit tests for each node/tool

## Notes
1. Workflow: intent parsing → knowledge base retrieval → data query → visualisation generation → response formatting
2. Follow the workflow diagram in the project proposal

## Tasks
- [ ] Define LangGraph nodes and edges matching the workflow diagram
- [ ] Implement intent parsing node
- [ ] Implement knowledge base retrieval node (integrates TICKET-003)
- [ ] Implement data query node (integrates TICKET-009)
- [ ] Implement visualisation node (integrates TICKET-011/012)
- [ ] Implement response formatting node
- [ ] Add multi-turn context preservation
- [ ] Write unit tests for each node
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-003 — Vector knowledge base available
2. TICKET-005 — Bedrock LLM client available
3. TICKET-006 — System prompts finalised

## Demo
1. Submit a multi-turn conversation (e.g., SST query then a follow-up region refinement) and show the agent routing correctly through all nodes

---

### TICKET-008 — MCP Integration for Context Management

**Type:** Feature | **Priority:** Medium | **Labels:** `ai`, `mcp`

## User Story

**AS AN** AI agent developer

**I WANT** Model Context Protocol (MCP) integrated to manage tool calls and provide structured context to the LLM

**SO THAT** the agent can reliably invoke the right tools with the right context without exceeding the model's context window

## Acceptance Criteria
1. MCP tool definitions created for knowledge-base lookup and data-fetch tools
2. LLM correctly selects and invokes tools via MCP
3. Context window usage stays within model limits for typical queries

## Notes
1. Tools to define: knowledge-base lookup, data-fetch, geolocation resolver
2. Monitor token usage per query to catch context overflow early

## Tasks
- [ ] Define MCP tool schemas for knowledge-base lookup and data-fetch
- [ ] Implement MCP tool routing in the agent
- [ ] Validate LLM selects correct tools for sample queries
- [ ] Add context window monitoring / truncation logic
- [ ] Integration test covering end-to-end tool invocation
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-007 — LangGraph agent skeleton in place

## Demo
1. Show the LLM correctly selecting and invoking the knowledge-base lookup tool for a sample query via MCP

---

## Epic 4: Data Access Layer

### TICKET-009 — S3 Zarr Dataset Loader

**Type:** Feature | **Priority:** High | **Labels:** `data`, `s3`, `zarr`

## User Story

**AS AN** agent data pipeline

**I WANT** to load spatially and temporally sliced data from AusTemp Zarr datasets on S3

**SO THAT** only the relevant subset of data is fetched efficiently without downloading entire datasets

## Acceptance Criteria
1. Zarr dataset opens successfully from S3 without downloading entirely
2. Spatial slice by lat/lon bbox works correctly
3. Temporal slice by date range works correctly
4. Downsampling applied when data exceeds a configurable size threshold
5. S3 access uses read-only IAM policy

## Notes
1. Libraries: `s3fs`, `xarray`
2. Size threshold for downsampling should be configurable via environment variable

## Tasks
- [ ] Implement S3 Zarr open using `s3fs` and `xarray`
- [ ] Add spatial slicing by lat/lon bbox
- [ ] Add temporal slicing by date range
- [ ] Implement configurable downsampling for large requests
- [ ] Enforce read-only IAM policy for S3 access
- [ ] Write unit tests for slicing and downsampling logic
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-001 — S3 paths and dataset structure documented
2. Read-only S3 IAM role provisioned

## Demo
1. Demonstrate loading a spatial and temporal slice of the AusTemp SST dataset and display the resulting xarray DataArray shape and values

---

### TICKET-010 — Parquet Dataset Loader (Optional)

**Type:** Feature | **Priority:** Low | **Labels:** `data`, `s3`, `parquet`

## User Story

**AS AN** agent data pipeline

**I WANT** to load and filter Parquet datasets from S3

**SO THAT** non-gridded IMOS data can be accessed through the same data-access interface as the Zarr loader

## Acceptance Criteria
1. Parquet file(s) readable from S3
2. Column-level filtering works for time and region fields
3. Integrated into the same data-access interface as the Zarr loader

## Notes
1. Libraries: `boto3`, `pandas`, `geopandas`
2. Optional ticket — implement only if Parquet datasets are confirmed in scope

## Tasks
- [ ] Confirm Parquet datasets are in scope and identify S3 paths
- [ ] Implement S3 Parquet reader using `boto3` / `pandas`
- [ ] Add column-level filtering for time and region fields
- [ ] Integrate into shared data-access interface
- [ ] Write unit tests for filtering logic
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-001 — Parquet dataset paths documented
2. TICKET-009 — Shared data-access interface defined

## Demo
1. Show filtered Parquet records returned for a given time range and region

---

## Epic 5: Visualisation

### TICKET-011 — Time Series Plot Generation

**Type:** Feature | **Priority:** High | **Labels:** `visualisation`

## User Story

**AS AN** end user querying SST trends over time

**I WANT** a time series line chart generated from the queried data

**SO THAT** I can visually understand temperature patterns and trends for a specific region and period

## Acceptance Criteria
1. Line chart generated for SST time series
2. Chart includes title, axis labels with units, and date range
3. Summary stats (mean, min, max) included in response text
4. Output format is configurable (PNG / HTML)

## Notes
1. Library: Matplotlib
2. Input: sliced xarray DataArray from the Zarr loader

## Tasks
- [ ] Implement time series plot function accepting an xarray DataArray
- [ ] Add title, axis labels with units, and date range annotation
- [ ] Compute and include summary stats (mean, min, max) in response
- [ ] Make output format configurable (PNG / HTML)
- [ ] Write unit tests with mock DataArray inputs
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-009 — Zarr loader producing xarray DataArrays

## Demo
1. Show a generated SST time series chart for Storm Bay with title, labels, and a summary stats block

---

### TICKET-012 — Spatial Map Plot Generation

**Type:** Feature | **Priority:** Medium | **Labels:** `visualisation`

## User Story

**AS AN** end user querying SST across a geographic region

**I WANT** a spatial heatmap of the 2D geospatial variable rendered for the queried bbox

**SO THAT** I can see the spatial distribution of the variable at a glance

## Acceptance Criteria
1. Spatial plot renders with correct projection and bbox
2. Colourbar with variable units included
3. Handles missing/NaN values gracefully

## Notes
1. Libraries: Matplotlib, xarray, Cartopy (optional for projection)
2. Input: 2D xarray DataArray sliced to bbox

## Tasks
- [ ] Implement spatial plot function accepting a 2D xarray DataArray
- [ ] Add correct projection and bbox extent
- [ ] Add colourbar with variable units
- [ ] Handle NaN/missing values without crashing
- [ ] Write unit tests with mock 2D DataArray inputs
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-009 — Zarr loader producing 2D xarray DataArrays

## Demo
1. Show a rendered SST heatmap for a defined bbox (e.g., Storm Bay) with colourbar and correct spatial extent

---

## Epic 6: Frontend (Gradio POC)

### TICKET-013 — Gradio Chat Interface

**Type:** Feature | **Priority:** Medium | **Labels:** `frontend`, `ui`

## User Story

**AS AN** end user exploring IMOS data

**I WANT** a chat interface where I can type natural language questions and receive text answers with inline charts

**SO THAT** I can explore oceanographic data without needing to write code or know dataset details

## Acceptance Criteria
1. Chat input/output renders correctly
2. Plot images (PNG) display inline in the chat
3. Session conversation history preserved across turns
4. Basic error messages shown when agent cannot answer

## Notes
1. Framework: Gradio
2. MVP front end — not production-ready
3. Connects to the FastAPI backend (TICKET-014)

## Tasks
- [ ] Scaffold Gradio chat UI
- [ ] Integrate with FastAPI `POST /query` endpoint
- [ ] Display inline PNG plot images in chat responses
- [ ] Preserve session conversation history across turns
- [ ] Add user-facing error messages for agent failures
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-014 — FastAPI backend service running

## Demo
1. Conduct a live multi-turn chat demo: ask an SST query, receive a text response with an inline chart, then ask a follow-up question

---

## Epic 7: Backend & API

### TICKET-014 — FastAPI Backend Service

**Type:** Feature | **Priority:** Medium | **Labels:** `backend`, `api`

## User Story

**AS A** frontend or API consumer

**I WANT** a FastAPI service that accepts natural language queries and returns agent responses with optional plots

**SO THAT** the Gradio UI and any future client can interact with the GeoInsight agent over HTTP

## Acceptance Criteria
1. `POST /query` endpoint functional and documented (OpenAPI)
2. Session/context ID threading works across requests
3. Returns structured JSON with `message` and optional `plot_url` or base64 image
4. Health check endpoint (`GET /health`) implemented

## Notes
1. Framework: FastAPI
2. Connect Gradio UI (TICKET-013) to the LangGraph agent (TICKET-007)

## Tasks
- [ ] Scaffold FastAPI application
- [ ] Implement `POST /query` endpoint with session context threading
- [ ] Implement `GET /health` endpoint
- [ ] Return structured JSON with `message` and optional `plot_url`/base64 image
- [ ] Auto-generate OpenAPI docs
- [ ] Write integration tests for both endpoints
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-007 — LangGraph agent orchestration complete

## Demo
1. Send a `curl` request to `POST /query` and show structured JSON response with message and base64 plot image

---

## Epic 8: Testing & Evaluation

### TICKET-015 — Agent Evaluation & Prompt Coverage

**Type:** Task | **Priority:** Medium | **Labels:** `testing`, `ai`

## User Story

**AS A** project lead assessing the GeoInsight POC

**I WANT** a structured evaluation of the agent across diverse query types with recorded baseline scores

**SO THAT** we can identify gaps in prompt coverage and RAG retrieval to guide improvement

## Acceptance Criteria
1. Evaluation dataset of ≥20 queries created
2. Scoring rubric defined (intent, dataset, region, time, plot type)
3. Baseline scores recorded
4. Gaps used to improve prompts or RAG retrieval

## Notes
1. Queries should cover different datasets, regions, time ranges, and visualisation types
2. Results feed back into TICKET-006 (prompt improvements) and TICKET-003 (RAG tuning)

## Tasks
- [ ] Create evaluation dataset of ≥20 diverse queries
- [ ] Define scoring rubric across all intent dimensions
- [ ] Run agent against evaluation dataset and record scores
- [ ] Identify failing cases and root causes
- [ ] Feed gaps back into prompt and RAG improvements
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-007 — Agent orchestration complete and testable

## Demo
1. Present evaluation scorecard showing per-dimension accuracy across the 20-query set and highlight top improvement areas

---

### TICKET-016 — Security & Prompt Injection Hardening

**Type:** Task | **Priority:** High | **Labels:** `security`

## User Story

**AS A** security-conscious developer

**I WANT** the GeoInsight agent hardened against prompt injection and with enforced read-only S3 access

**SO THAT** the POC cannot be exploited to exfiltrate data, execute arbitrary code, or leak credentials

## Acceptance Criteria
1. Prompt injection test cases documented and passing
2. S3 IAM policy limited to read-only on relevant buckets
3. No user-supplied strings passed directly to `exec`/`eval`
4. Secrets managed via AWS Secrets Manager (no hardcoded keys)

## Notes
1. Prompt injection edge cases sourced from TICKET-006
2. Review all LLM-generated code/query paths before execution

## Tasks
- [ ] Document and implement prompt injection test cases
- [ ] Audit all code paths for `exec`/`eval` with user-supplied input
- [ ] Restrict S3 IAM policy to read-only on relevant buckets only
- [ ] Migrate any hardcoded secrets to AWS Secrets Manager
- [ ] Conduct security review with team
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-006 — Prompt injection edge cases documented
2. TICKET-005 — Bedrock IAM role in place

## Demo
1. Run prompt injection test cases and show all passing; demonstrate Secrets Manager integration replacing any hardcoded credentials

---

## Epic 9: Deployment

### TICKET-017 — Dockerise Application

**Type:** Task | **Priority:** Medium | **Labels:** `deployment`, `docker`

## User Story

**AS A** developer onboarding to the GeoInsight POC

**I WANT** a Docker Compose setup that spins up the full application locally with a single command

**SO THAT** I can develop, test, and demo the system without complex local environment setup

## Acceptance Criteria
1. `Dockerfile` builds successfully for backend and frontend
2. `docker-compose up` starts both services locally
3. Environment variables externalised via `.env` / AWS Secrets Manager

## Notes
1. Separate Dockerfiles for FastAPI backend and Gradio frontend
2. Use `.env` for local dev; AWS Secrets Manager for production

## Tasks
- [ ] Write `Dockerfile` for FastAPI backend
- [ ] Write `Dockerfile` for Gradio frontend
- [ ] Write `docker-compose.yml` for local development
- [ ] Externalise all environment variables via `.env`
- [ ] Test `docker-compose up` end-to-end locally
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-013 — Gradio frontend complete
2. TICKET-014 — FastAPI backend complete

## Demo
1. Run `docker-compose up` from a clean checkout and show both services healthy and a successful end-to-end query

---

### TICKET-018 — Deploy to AWS ECS / Lambda

**Type:** Task | **Priority:** Medium | **Labels:** `deployment`, `aws`

## User Story

**AS A** stakeholder wanting to demo GeoInsight AI

**I WANT** the application deployed and reachable on AWS

**SO THAT** the POC can be accessed and evaluated without running it locally

## Acceptance Criteria
1. Container image pushed to ECR
2. ECS service (or Lambda function) running and reachable
3. CloudWatch logging enabled
4. Terraform config checked in (optional but recommended)

## Notes
1. Target: AWS ECS Fargate or Lambda
2. Use ECR for container image hosting
3. Terraform IaC is optional but recommended for repeatability

## Tasks
- [ ] Create ECR repository and push Docker images
- [ ] Configure ECS Fargate service (or Lambda) for backend and frontend
- [ ] Enable CloudWatch logging for all services
- [ ] Set up IAM roles for ECS task execution
- [ ] Write Terraform config for infrastructure (optional)
- [ ] Smoke test deployed endpoints
- [ ] Clean up any AWS resources created during backlog work
- [ ] DOD [Link to checklist](https://www.notion.so/imos-world/Definition-of-Done-DoD-b98281f003a44ce890dfba5af2f00337)

## PRs
[Pull Request (PR) Review Guidelines](https://www.notion.so/imos-world/Pull-Request-PR-Review-Guidelines-f726880c6f1542c9a9ef906f8397a5fa)

1.

## Dependencies
1. TICKET-017 — Docker images built and tested locally

## Demo
1. Access the deployed Gradio UI via public URL and run a live end-to-end query returning a chart

---

## Milestone Summary

| Milestone | Tickets | Target Duration |
|---|---|---|
| M1: IMOS Knowledge Base Agent | TICKET-001 to TICKET-008 | ~5–7 weeks |
| M2: Data Visualisation AI Agent | TICKET-009 to TICKET-018 | ~4–5 weeks |
| **Total** | **18 tickets** | **~9–11 weeks** |
