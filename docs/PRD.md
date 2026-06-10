# GeoInsight AI Product Requirements Document

## Document Status

- Status: Draft for stakeholder review
- Source: `docs/project_proposal.md`
- Delivery model: Two milestones over an estimated 9 to 11 weeks
- Primary proof of concept: Discover and visualize AusTemp sea surface temperature near Storm Bay
- Owner: GeoInsight AI project team

Targets marked **provisional** are working acceptance thresholds for the proof of concept and must be confirmed with IMOS stakeholders before release.

## 1. Product Summary

GeoInsight AI is a natural-language interface for discovering and exploring IMOS geospatial data. It is intended for users who understand the scientific question they want to ask but do not necessarily know the relevant IMOS dataset, metadata catalogue, S3 path, storage format, geospatial tooling, or plotting workflow.

The product will:

1. Interpret a natural-language question.
2. Retrieve relevant IMOS dataset metadata.
3. Identify suitable datasets and explain why they match.
4. Resolve supported place names and time expressions into query constraints.
5. Read a bounded subset of supported data from AWS S3.
6. Produce an interpretable chart and concise data summary.
7. Preserve enough conversation context to support follow-up questions.

The first milestone delivers dataset discovery through an IMOS Knowledge Base Agent. The second milestone delivers an end-to-end Data Visualization Agent and a Gradio proof-of-concept application.

## 2. Problem Statement

Discovering and visualizing IMOS data currently requires specialist knowledge across several areas:

- IMOS catalogues and metadata conventions
- Dataset and variable selection
- S3 locations and access patterns
- Zarr or Parquet storage formats
- Spatial and temporal subsetting
- Scientific data aggregation
- Plotting and interpretation

This creates a barrier for non-technical users and repeated setup work for technical users. A user asking, "How has sea surface temperature near Storm Bay changed over the last week?" should not need to first learn the data catalogue and write a Python data pipeline.

## 3. Goals

### 3.1 Product Goals

1. Enable users to discover relevant in-scope IMOS datasets through natural-language questions.
2. Explain dataset recommendations using retrieved IMOS metadata rather than unsupported model knowledge.
3. Translate supported requests into constrained spatial, temporal, variable, and visualization parameters.
4. Demonstrate efficient access to AusTemp Zarr data in S3 without downloading the complete dataset.
5. Generate scientifically interpretable time-series visualizations and summaries.
6. Support a multi-turn Storm Bay SST demonstration through a Gradio chat interface.
7. Establish reusable service boundaries for future IMOS-Live integration and additional datasets.

### 3.2 Success Measures

The proof of concept will be evaluated against a versioned test set containing at least 20 representative prompts.

| Measure | Provisional target |
|---|---:|
| Expected dataset appears in the top 3 retrieval results | >= 90% |
| Correct variable extraction | >= 90% |
| Correct region resolution for supported named regions | >= 90% |
| Correct absolute or relative time-range extraction | >= 90% |
| Correct visualization-type selection | >= 90% |
| Required Storm Bay SST end-to-end scenarios complete successfully | 100% |
| Prompt-injection and unauthorized-tool test cases blocked | 100% |
| Unhandled errors in the evaluation set | 0 |

Scores must be reported by dimension. A single combined score is not sufficient to approve a milestone.

## 4. Non-Goals

The initial release will not provide:

- Real-time streaming-data processing
- Observation-data ingestion or transformation pipelines
- Support for every IMOS dataset
- Forecasting, predictive modelling, or advanced statistical analysis
- Broad multilingual support
- Custom model fine-tuning unless evaluation shows that prompting and retrieval cannot meet requirements
- Full IMOS-Live portal integration
- Production-grade public authentication or authorization
- Unrestricted execution of user-provided or model-generated code
- Write access to source datasets

Metadata extraction, normalization, embedding, and indexing are in scope. "No data ingestion" refers specifically to ingestion of source observation datasets.

## 5. Users and Primary Jobs

### 5.1 Non-Technical Data User

Needs to discover datasets and produce a useful visualization without writing code or knowing storage details.

### 5.2 Marine Scientist or Environmental Analyst

Needs to validate that a recommended dataset, variable, region, period, and aggregation are appropriate before relying on the result.

### 5.3 IMOS Developer

Needs structured metadata, constrained tools, stable API contracts, and testable orchestration.

### 5.4 System Operator

Needs repeatable deployment, least-privilege AWS access, externalized configuration, and actionable logs.

## 6. Scope and Release Boundaries

### 6.1 Required POC Scope

The following are required for the end-to-end proof of concept:

| Capability | Required scope |
|---|---|
| Reference dataset | AusTemp Sea Surface Temperature |
| Storage format | Zarr in AWS S3 |
| Reference variable | Sea surface temperature (SST) |
| Reference region | Storm Bay |
| Time expressions | Absolute dates and relative periods such as "past 7 days" |
| Discovery output | Ranked dataset recommendations with evidence |
| Data operation | Spatial subset, temporal subset, and bounded aggregation |
| Visualization | SST time-series PNG |
| Summary | Mean, minimum, maximum, period, region, units, and data source |
| Interface | Gradio chat application backed by FastAPI |
| Conversation | Follow-up reuse of dataset, variable, region, and time context |

### 6.2 Discovery Scope

The knowledge base should include metadata for the confirmed POC dataset set. Candidate topics from the proposal are:

- Sea Surface Temperature
- Degree Heating Days
- Mosaic products

Before implementation, each candidate must be recorded in a dataset inventory with:

- Stable dataset identifier and display name
- S3 or catalogue location
- Storage format
- Supported variables and units
- Coordinate names and reference system
- Spatial and temporal coverage
- Quality-control fields
- Known update frequency

"Degree Heating Days" and "Mosaic" do not become visualization requirements until exact datasets, variables, access paths, and expected operations are confirmed.

### 6.3 Conditional Scope

The following capabilities are optional and must not block the required Storm Bay SST flow:

- Parquet data loading
- Spatial heatmaps
- HTML or interactive plot output
- Model Context Protocol integration
- Terraform infrastructure
- Additional named regions
- Additional datasets and variables

Conditional items should only enter a milestone after their data source and acceptance criteria are documented.

## 7. Primary User Journey

### 7.1 Dataset Discovery

User:

> I am interested in sea surface temperature near Storm Bay. Which IMOS datasets are relevant?

The system must:

1. Extract the topic and region.
2. Retrieve matching dataset metadata.
3. Return a ranked list of relevant datasets.
4. Explain each recommendation using metadata evidence.
5. State variable availability, temporal coverage, and spatial relevance when known.
6. Avoid inventing unsupported datasets or capabilities.

### 7.2 Visualization Follow-Up

User:

> Plot the temperature changes near Storm Bay using AusTemp over the past 7 days.

The system must:

1. Reuse conversation context where applicable.
2. Resolve the requested period to explicit UTC start and end timestamps.
3. Resolve Storm Bay to the configured bounding box and disclose that interpretation.
4. Validate that AusTemp contains the requested variable and period.
5. Build a structured, bounded data query.
6. Read only the required Zarr subset.
7. Apply documented quality filtering and aggregation.
8. Return a time-series PNG and concise summary.

### 7.3 Clarification Behaviour

The agent may execute a plot request without a separate confirmation when dataset, variable, region, time range, and plot type are all unambiguous and supported.

It must ask a focused clarification question when:

- More than one dataset is similarly suitable and the choice materially affects the result.
- A place name has multiple plausible matches.
- The variable is absent or ambiguous.
- No time range is supplied and no documented default applies.
- The request exceeds configured data-size or time-range limits.

## 8. Functional Requirements

### FR-1: Metadata Inventory and Normalization

The system must maintain a normalized metadata record for each in-scope dataset. Required fields are:

- `dataset_id`
- `title`
- `description`
- `variables`
- `units`
- `spatial_extent`
- `temporal_coverage`
- `storage_format`
- `storage_location`
- `coordinate_reference_system`
- `coordinate_names`
- `quality_control_fields`
- `source_metadata_reference`
- `last_indexed_at`

Normalization must preserve a reference to the source metadata so recommendations can be traced.

### FR-2: Knowledge-Base Retrieval

The system must:

- Embed normalized metadata chunks into a selected vector store.
- Use the same embedding model for indexing and queries.
- Return structured metadata with each retrieval result.
- Support configurable `top_k`.
- Return no match when results do not meet the configured relevance threshold.
- Record retrieval evaluation results in a versioned artifact.

### FR-3: Intent Extraction

The agent must produce validated structured intent containing:

- Dataset candidate
- Variable
- Region name and/or bounding box
- Start and end timestamp
- Visualization type
- Output format
- Aggregation request
- Unresolved or ambiguous fields

Natural-language synonyms such as "SST" and "sea surface temperature" must map to the same supported variable.

### FR-4: Geolocation Resolution

The resolver must:

- Resolve Storm Bay to an approved, versioned bounding box.
- Return the source and confidence or match type.
- Detect ambiguous and unknown locations.
- Never let the LLM invent coordinates.

The initial source will be selected during data setup from IMOS GeoServer, GeoNames, or a curated IMOS lookup table. The approved Storm Bay result must be available locally so the required demo does not depend on an external geocoder.

### FR-5: Date Resolution

The system must:

- Resolve relative dates using the request time.
- Use UTC for internal query boundaries.
- Return explicit dates in the response.
- Treat "past 7 days" as a documented interval convention.
- Reject dates outside dataset coverage with an actionable message.

The exact inclusivity convention for start and end timestamps must be consistent across parsing, querying, plotting, and tests.

### FR-6: Conversation Context

Within one session, the system must preserve the most recent confirmed:

- Dataset
- Variable
- Region
- Time range
- Visualization type

A user must be able to replace any prior constraint explicitly. The Gradio POC must provide a way to start a new session and clear context.

### FR-7: Data Query Planning

The LLM may select from approved operations but must not generate executable Python. A validated query plan must contain only allow-listed:

- Dataset identifiers
- Variables
- Spatial bounds
- Temporal bounds
- Aggregations
- Downsampling options
- Output types

All parameters must be checked against dataset metadata and configured resource limits before S3 access.

### FR-8: Zarr Data Access

The required loader must:

- Open AusTemp Zarr from S3 using `s3fs` and `xarray`.
- Use read-only credentials.
- Read lazily where supported.
- Apply spatial and temporal selection before materializing data.
- Detect empty selections.
- Enforce configurable limits before loading or plotting.
- Return a standard internal result independent of storage details.

Parquet support must use the same logical data-access contract if later enabled.

### FR-9: Scientific Processing

For every supported dataset-variable pair, a processing profile must define:

- Source variable name
- Display name and canonical unit
- Fill-value and missing-value handling
- Quality-control flags to include or exclude
- Valid range, if defined by source metadata
- Spatial aggregation method
- Temporal aggregation method
- Weighting method
- Downsampling method

For the Storm Bay SST time series:

- Invalid and source-defined fill values must be excluded.
- Source quality-control flags must be applied when available and documented.
- Spatial aggregation must be explicitly identified in the response.
- Area weighting must be used when required by the dataset grid; otherwise the unweighted method must be disclosed.
- Summary statistics must be computed from the same filtered series shown in the chart.
- The system must not claim a trend or causal conclusion from mean, minimum, and maximum alone.

### FR-10: Visualization

The required PNG time-series output must include:

- Dataset and variable
- Region
- Explicit date range
- Axis labels
- Units
- Aggregation method
- A readable indication of missing periods when applicable

The accompanying response must include mean, minimum, maximum, units, region interpretation, date range, dataset source, and any quality or coverage warning.

Spatial-map support is conditional. If implemented, it must include geographic extent, color scale, units, timestamp or aggregation period, and missing-value handling.

### FR-11: API

The FastAPI service must expose:

- `POST /query`
- `GET /health`

`POST /query` must accept a user message and optional session identifier. It must return structured JSON containing:

- `session_id`
- `message`
- `status`
- `resolved_intent`
- `sources`
- Optional `plot`
- Optional warnings or clarification request
- Machine-readable error code when unsuccessful

The plot transport mechanism must be selected before frontend integration. Base64 is acceptable for local POC use; object storage with an expiring URL is preferred for deployed use.

### FR-12: Gradio Interface

The Gradio POC must:

- Accept chat messages.
- Display agent text and PNG plots inline.
- Preserve context within a browser session.
- Allow the user to clear the session.
- Display clarification prompts and actionable errors.
- Identify itself as a proof of concept.

### FR-13: Error Handling

The system must distinguish at least:

- No matching dataset
- Unsupported variable
- Unknown or ambiguous region
- Invalid or unsupported date range
- No data in the selected subset
- Query exceeds configured limits
- S3 or metadata service unavailable
- Model or embedding service unavailable
- Plot generation failure

Errors must not expose credentials, internal prompts, stack traces, or unauthorized storage paths.

## 9. Non-Functional Requirements

### NFR-1: Performance and Resource Limits

The following initial targets are **provisional**:

- Dataset-discovery response: p95 <= 10 seconds under single-user POC load
- Required cached/warm Storm Bay SST visualization: p95 <= 30 seconds
- Hard request timeout: 60 seconds
- Maximum default requested period: 31 days
- Maximum in-memory materialized data per request: 250 MB
- Maximum plotted time-series points: 2,000 after aggregation/downsampling

All limits must be configurable. Requests exceeding them must be narrowed or aggregated, not allowed to exhaust service resources.

### NFR-2: Reliability

- A failure in one external service must produce a controlled error response.
- Bedrock and transient S3 calls must use bounded retries with backoff.
- Health checks must distinguish process health from dependency readiness where practical.
- The required demo path must have deterministic fixtures for automated testing.

### NFR-3: Security

- S3 access must be read-only and restricted to approved resources.
- User input and model output must never be passed to `exec`, `eval`, a shell, or an unrestricted query engine.
- Tool calls must use validated structured schemas and allow-listed dataset identifiers.
- Secrets must be externalized through environment configuration for local development and AWS Secrets Manager or an equivalent service when deployed.
- Logs must redact credentials, authorization headers, sensitive configuration, and full signed URLs.
- Sessions must be isolated by unguessable identifiers.
- The deployed POC must not be publicly reachable without an explicitly approved access-control decision.
- Request size and rate limits must be configured for deployment.

### NFR-4: Observability

Each request must have a correlation identifier. Structured logs should capture:

- Session and request identifiers
- Selected dataset and variable
- Resolved region and time range
- Tools invoked
- Timing by workflow stage
- Data shape and estimated/materialized size
- Aggregation or downsampling applied
- Outcome and machine-readable error code

Prompts and user text must only be retained according to an approved logging and retention policy.

### NFR-5: Cost Control

- Model IDs, regions, token limits, retrieval count, and data-size limits must be configurable.
- Evaluation and load tests must record model usage and approximate AWS cost.
- AWS resources created for development or demonstration must have documented ownership and cleanup procedures.

### NFR-6: Deployment

- Backend and frontend must build as containers.
- Local startup must be reproducible with Docker Compose.
- AWS deployment will use ECR and one selected compute target.
- ECS Fargate is the default deployment assumption because the POC includes long-lived web services and potentially large scientific dependencies.
- Lambda remains an alternative only if packaging size, runtime duration, memory, and filesystem constraints are proven acceptable.
- CloudWatch logging is required for the deployed POC.

## 10. Architecture Constraints

- AWS Bedrock is the primary LLM provider.
- Model ID and AWS region must be configuration values.
- LangGraph will orchestrate explicit workflow nodes.
- RAG will ground dataset discovery in normalized IMOS metadata.
- Data access will be exposed as constrained tools.
- FastAPI will provide the backend service boundary.
- Gradio will provide the proof-of-concept frontend.
- Matplotlib PNG is the required visualization format.
- MCP is optional and should only be introduced if it simplifies tool interoperability or context management for the POC.
- Prefect is not required unless a separate scheduled workflow need is identified.

## 11. Milestones

### Milestone 1: IMOS Knowledge Base Agent

Estimated duration: 5 to 6 weeks.

Required deliverables:

- Confirmed dataset inventory
- Normalized metadata schema and records
- Versioned Storm Bay region definition
- Embedding and vector-store pipeline
- Semantic retrieval function
- AWS Bedrock client
- Structured intent extraction
- Dataset-discovery agent
- Retrieval and agent evaluation harnesses
- Prompt-injection test set

Milestone acceptance:

1. A user can ask for SST datasets relevant to Storm Bay and receive grounded recommendations.
2. AusTemp appears in the top three results for the reference query.
3. Recommendations cite structured metadata fields and do not fabricate storage or variable details.
4. The Milestone 1 evaluation thresholds in Section 3.2 are met for retrieval, variable, and region dimensions.
5. Unknown datasets and regions produce controlled, actionable responses.

### Milestone 2: Data Visualization Agent

Estimated duration: 4 to 5 weeks.

Required deliverables:

- AusTemp S3 Zarr loader
- Scientific processing profile for SST
- Time-series plot generation
- LangGraph end-to-end workflow
- FastAPI service
- Gradio interface
- Docker Compose environment
- AWS demonstration deployment
- End-to-end evaluation and security results

Milestone acceptance:

1. The reference two-turn Storm Bay flow succeeds from a clean session.
2. The returned chart and summary use the requested region and explicit date range.
3. Values, units, quality filtering, aggregation, and statistics match an independently calculated fixture or reference script.
4. Data access remains within configured resource limits and does not download the full Zarr dataset.
5. Follow-up questions correctly reuse or replace session context.
6. Required API, UI, security, container, and deployment checks pass.
7. All applicable success thresholds in Section 3.2 are met.

## 12. Testing and Evaluation

Testing must prioritize observable behavior and scientific correctness.

### 12.1 Automated Tests

- Metadata schema and normalization tests
- Deterministic metadata chunking tests
- Retrieval tests and precision-at-k evaluation
- Intent extraction tests
- Known, ambiguous, and unknown geolocation tests
- Relative and absolute date parsing tests
- Query-plan schema and allow-list tests
- Zarr slicing, empty-result, missing-value, QC, aggregation, and limit tests
- Plot labels, units, date range, and statistics tests
- LangGraph node and routing tests
- FastAPI contract and error tests
- Session isolation and context-reset tests
- Prompt-injection and unauthorized-resource tests
- Container build and startup tests

### 12.2 Scientific Reference Tests

The Storm Bay SST scenario must have a fixed test period and expected results generated by a reviewed reference calculation. Tests must compare:

- Selected grid cells
- Included timestamps
- QC filtering
- Aggregated series
- Mean, minimum, and maximum
- Units

Tolerance values must be documented for floating-point comparisons.

### 12.3 Manual POC Verification

- Multi-turn Gradio flow
- Inline plot rendering
- Clarification behaviour
- Error readability
- Deployed endpoint and CloudWatch logs
- Chart readability with sparse and missing data

## 13. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Ambiguous natural-language requests | Structured extraction, few-shot examples, and focused clarification |
| Hallucinated dataset facts | Metadata-grounded retrieval and source references |
| Incorrect place-name resolution | Curated required-region records and ambiguity handling |
| Scientifically misleading aggregation | Dataset-specific processing profiles and reference calculations |
| Large or slow S3 queries | Early slicing, lazy access, hard limits, aggregation, and timeout handling |
| Prompt injection or unsafe tool use | Allow-listed structured tools, no generated-code execution, and adversarial tests |
| Scope expansion across datasets and formats | Required dataset matrix and conditional-scope gate |
| AWS cost growth | Configurable limits, usage logging, and resource cleanup |
| Schedule pressure | Prioritize the required Storm Bay SST path before optional capabilities |

## 14. Dependencies

- Access to confirmed IMOS metadata sources
- Read-only access to required S3 datasets
- Confirmed AusTemp Zarr path and schema
- AWS Bedrock model and embedding-model access
- Agreement on the Storm Bay bounding box
- Identification of source QC conventions
- AWS account permissions for ECR, compute, secrets, IAM, and CloudWatch
- Stakeholder availability to review dataset recommendations and scientific outputs

## 15. Open Decisions

These decisions must be resolved before the dependent work begins:

| Decision | Required by |
|---|---|
| Exact in-scope dataset IDs beyond AusTemp | Metadata inventory completion |
| Exact Degree Heating Days and Mosaic meanings | Scope expansion |
| Vector-store technology | Embedding pipeline implementation |
| Primary geolocation source | Geolocation service implementation |
| Approved Storm Bay bounding box | Reference tests |
| SST QC and aggregation rules | Zarr loader and plotting |
| Relative-date inclusivity convention | Intent and date tests |
| Plot transport: base64 or expiring URL | API/frontend integration |
| ECS Fargate or Lambda | Deployment implementation |
| Deployed POC access control | Public or shared deployment |
| Session and prompt retention period | Deployment and logging |
| Whether Parquet is included | Milestone 2 planning |
| Whether MCP provides enough value for the POC | Agent integration |

## 16. Definition of Done

The proof of concept is complete when:

1. Both milestone acceptance criteria are satisfied.
2. Required automated, scientific-reference, security, and deployment tests pass.
3. Evaluation results and known limitations are documented.
4. The dataset inventory and processing profile match the deployed behavior.
5. The application runs from a clean checkout using documented configuration.
6. The deployed demonstration can complete the reference Storm Bay SST flow.
7. No critical or high-severity security issue remains open.
8. Optional capabilities are clearly identified as delivered, deferred, or unsupported.
