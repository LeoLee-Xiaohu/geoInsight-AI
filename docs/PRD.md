# GeoInsight AI Product Requirements Document

## Problem Statement

Marine, environmental, and climate data users need to discover and explore IMOS geospatial datasets without first learning dataset catalogues, S3 storage layouts, Zarr or Parquet formats, Python data tooling, or plotting workflows. A user may know the scientific question they want to ask, such as whether sea surface temperature near Storm Bay changed over the last week, but may not know which IMOS dataset contains the right variable, how to locate the data in AWS S3, how to slice it by region and date, or how to turn the result into a readable chart.

The current workflow requires specialist knowledge across metadata discovery, geospatial lookup, cloud data access, and visualization. This slows down exploratory analysis, creates repeated engineering work for common questions, and limits access for non-technical users who could benefit from self-service scientific insight.

## Solution

GeoInsight AI will provide an AI-powered natural language interface for dynamic geospatial data exploration. Users will ask conversational questions about IMOS datasets, regions, variables, and time periods. The system will interpret the request, retrieve relevant IMOS metadata from a knowledge base, resolve natural place names into spatial bounds, load the appropriate S3-hosted data, generate a visualization, and return a concise explanation with the generated plot.

The first product milestone is an IMOS Knowledge Base Agent that can answer dataset discovery questions, identify relevant IMOS datasets, and explain why they match a user request. The second milestone is an IMOS Data Visualization Agent that can query supported Zarr and Parquet datasets from S3, perform spatial and temporal slicing, aggregate or downsample when needed, and produce charts through a Gradio proof-of-concept interface backed by an agent service.

The product will focus initially on IMOS geospatial datasets, with proof-of-concept variables including Sea Surface Temperature, Degree Heating Days, and Mosaic products. The reference use case is a user discovering and plotting sea surface temperature near Storm Bay using AusTemp Sea Surface Temperature data.

## User Stories

1. As a non-technical IMOS data user, I want to ask which datasets are relevant to a natural language topic, so that I can discover useful data without searching catalogues manually.
2. As a marine scientist, I want to ask about sea surface temperature near a named region, so that I can quickly identify the datasets that measure that variable.
3. As an environmental analyst, I want the assistant to explain why a dataset is relevant, so that I can judge whether it fits my analysis need.
4. As a portal user, I want to ask follow-up questions in a conversation, so that I do not need to repeat the full context each turn.
5. As a data user, I want the assistant to understand variable synonyms such as SST and sea surface temperature, so that my query does not require exact metadata wording.
6. As a data user, I want the assistant to resolve place names such as Storm Bay into geographic bounds, so that I do not need to provide latitude and longitude coordinates.
7. As a data user, I want the assistant to resolve relative date ranges such as the past 7 days, so that I can ask questions naturally.
8. As a data user, I want to request a time series chart, so that I can see how a variable changes over time.
9. As a data user, I want to request a spatial map, so that I can inspect geographic variation across a region.
10. As a data user, I want generated charts to include labels, units, titles, and date ranges, so that the output is interpretable.
11. As a data user, I want the assistant to summarize mean, minimum, and maximum values when it generates a chart, so that I get immediate context from the data.
12. As a data user, I want the assistant to return an image or dashboard-ready output, so that results can be displayed in the IMOS-Live portal or a proof-of-concept UI.
13. As a data user, I want clear feedback when a query is too broad, so that I can refine region, time, dataset, or variable constraints.
14. As a data user, I want clear feedback when a dataset cannot be found, so that I understand what to try next.
15. As a data user, I want clear feedback when a region cannot be resolved, so that I can provide a more specific location.
16. As a data user, I want the assistant to recommend relevant IMOS datasets before plotting, so that I can confirm the intended data source.
17. As a data user, I want to compare a current period with a previous period in a follow-up question, so that I can explore trends without starting over.
18. As a data user, I want the system to avoid overloading me with raw metadata, so that answers stay focused on my question.
19. As a developer, I want a structured metadata index for IMOS datasets, so that retrieval and agent reasoning are grounded in consistent data.
20. As a developer, I want a vector knowledge base for IMOS metadata, so that natural language queries can retrieve relevant datasets and variables.
21. As a developer, I want a geolocation resolver for named regions, so that agent queries can be converted into spatial slices.
22. As a developer, I want a common data-access interface for Zarr and Parquet, so that the agent can call data tools without coupling itself to storage details.
23. As a developer, I want S3 Zarr loading through streaming-compatible libraries, so that large datasets are not downloaded in full.
24. As a developer, I want configurable aggregation and downsampling thresholds, so that large spatial and temporal requests remain responsive.
25. As a developer, I want LangGraph orchestration for the agent workflow, so that parsing, retrieval, data access, plotting, and response formatting are explicit and testable.
26. As a developer, I want AWS Bedrock model configuration to be parameterized, so that model IDs and regions are not hardcoded.
27. As a developer, I want prompt examples for dataset, variable, region, time range, and visualization extraction, so that the agent has stable behavior for common query forms.
28. As a developer, I want prompt-injection edge cases documented and tested, so that the system does not follow malicious user instructions.
29. As a developer, I want tool calls to use structured inputs and outputs, so that LLM reasoning is separated from executable data access behavior.
30. As a developer, I want a FastAPI endpoint for agent queries, so that frontends can call the agent through a stable service boundary.
31. As a frontend user, I want a Gradio chat interface, so that the proof of concept can be used without custom portal integration.
32. As a frontend user, I want generated plots displayed inline in the chat, so that I can view text and visual results together.
33. As a system operator, I want Dockerized services, so that local development and deployment use repeatable runtime environments.
34. As a system operator, I want deployment support for AWS ECS or Lambda, so that the proof of concept can be productionized on AWS.
35. As a system operator, I want CloudWatch logging for deployed services, so that runtime behavior and failures can be inspected.
36. As a security owner, I want S3 access restricted to read-only permissions on relevant buckets, so that the agent cannot mutate source data.
37. As a security owner, I want secrets managed outside the codebase, so that credentials are not committed or exposed.
38. As a project stakeholder, I want an evaluation set of diverse prompts, so that agent quality can be measured and improved over time.

## Implementation Decisions

- The product will be delivered in two milestones: first the IMOS Knowledge Base Agent, then the IMOS Data Visualization AI Agent.
- The initial scope will target IMOS geospatial datasets, with proof-of-concept support for Sea Surface Temperature, Degree Heating Days, and Mosaic products.
- AusTemp Sea Surface Temperature will be the primary reference dataset for the Storm Bay demonstration flow.
- The IMOS knowledge base will contain normalized dataset metadata, including dataset names, descriptions, variables, units, spatial extents, temporal coverage, storage locations, and relevant metadata conventions.
- Metadata will be cleaned into a structured schema before embedding, rather than embedding inconsistent raw metadata directly.
- Retrieval-augmented generation will be used to ground dataset discovery and reduce unsupported model claims.
- A vector store will be populated from IMOS metadata chunks and queried by the agent for dataset discovery and variable matching.
- A geolocation resolver will map natural place names to latitude and longitude bounding boxes. Initial sources may include IMOS GeoServer, GeoNames, or a curated lookup table for IMOS-relevant regions.
- The agent will extract structured intent from user queries, including dataset candidate, variable, geographic region, time range, visualization type, and output format.
- LangGraph will orchestrate the agent workflow as explicit nodes for intent parsing, knowledge-base retrieval, data-query planning, data loading, visualization generation, and response formatting.
- Conversation context will be preserved within a user session so follow-up questions can reuse prior dataset, variable, region, and time constraints.
- AWS Bedrock will provide the main LLM integration, with support for suitable Nova or Claude models. Model ID and AWS region will be configuration values.
- Model Context Protocol can be used to expose structured tool context to the LLM, especially for knowledge-base lookup, dataset schema access, data loading, and previous conversation state.
- Data access will use S3-compatible libraries and read data lazily where possible. Zarr access will use S3, s3fs, and xarray. Parquet support may use boto3, pandas, and geopandas.
- The Zarr loader will support spatial slicing by bounding box, temporal slicing by date range, and aggregation or downsampling for large requests.
- Parquet loading is lower priority and should conform to the same data-access interface when implemented.
- Visualization generation will initially use Matplotlib, with PNG as the primary proof-of-concept output and HTML as a configurable option where useful.
- Time series plots will include title, axis labels, units, date range, and summary statistics.
- Spatial plots will include correct geographic bounds, colorbar, variable units, and graceful handling of missing values.
- The proof-of-concept frontend will be a Gradio chat application that shows text answers and generated plots inline.
- A FastAPI backend will expose the agent through a query endpoint and a health endpoint, allowing the frontend and future portal integrations to use the same service.
- API responses will return structured data containing the assistant message and an optional plot reference or encoded plot payload.
- Docker will be used for repeatable local and deployment environments. Separate backend and frontend containers may be used if that keeps service boundaries clear.
- AWS deployment will target ECS Fargate or Lambda, with ECR for container images and CloudWatch for logs. Terraform is optional but recommended for repeatability.
- IAM permissions for data access will be read-only and limited to relevant S3 resources.
- The system will not execute arbitrary user-provided code or unsanitized LLM-generated code. Data operations should be implemented as constrained tool calls.
- Secrets will be stored outside the repository, using AWS Secrets Manager or equivalent configuration.
- Error handling will provide actionable user-facing responses for missing datasets, unresolved regions, unsupported variables, overly broad requests, unavailable S3 data, and plotting failures.

## Testing Decisions

- Tests should verify external behavior and contracts rather than internal implementation details. Agent tests should assert structured outcomes, tool routing, retrieved dataset relevance, and response behavior instead of exact prose.
- Metadata cleaning should be tested with representative raw metadata samples and expected normalized fields.
- Knowledge-base retrieval should be tested with sample queries such as sea surface temperature near Storm Bay and should verify that relevant IMOS datasets rank highly.
- Geolocation lookup should be tested for known regions, ambiguous names, and missing regions.
- Intent extraction should be evaluated against examples covering dataset names, variable synonyms, natural regions, absolute dates, relative dates, time series requests, and spatial map requests.
- LangGraph nodes should be tested individually where possible, with integration tests covering the full path from user query to selected dataset and planned tool calls.
- S3 data loaders should be tested against small fixtures or controlled test datasets that exercise spatial slicing, temporal slicing, missing values, and aggregation thresholds.
- Visualization modules should be tested for generated output presence, correct labels and units, and graceful behavior for missing or sparse data.
- FastAPI endpoints should be tested for request validation, successful query responses, optional plot payloads, health checks, and error cases.
- Gradio behavior should be manually verified for chat rendering, inline plots, session continuity, and error display during the proof-of-concept phase.
- Security testing should include prompt-injection attempts, attempts to override tool constraints, attempts to access unauthorized S3 paths, and attempts to cause direct code execution.
- Agent evaluation should include at least 20 diverse queries across datasets, variables, regions, time ranges, and visualization types. Scoring should track intent extraction, dataset selection, region resolution, time parsing, and visualization correctness.
- Baseline evaluation results should be recorded before prompt and retrieval improvements, then reused as a regression set.
- Deployment verification should include container build checks, local startup checks, environment-variable configuration, and deployed health checks.

## Out of Scope

- Real-time streaming data processing is out of scope for the initial product.
- New data ingestion pipelines are out of scope; source datasets are assumed to already exist in S3 or an accessible catalogue.
- Predictive modeling, forecasting, or advanced statistical modeling is out of scope. The focus is discovery, slicing, aggregation, visualization, and explanatory summaries.
- Broad multilingual support is out of scope for the proof of concept.
- Fine-tuning custom models is out of scope unless later justified by evaluation results after prompt and retrieval improvements.
- Full production portal integration is out of scope for the initial Gradio proof of concept, though API boundaries should allow future integration.
- Support for all IMOS datasets is out of scope for the first release. The initial scope is a targeted set of geospatial datasets and variables.
- Unrestricted execution of LLM-generated code is out of scope and should not be introduced.
- Write access to source S3 datasets is out of scope.

## Further Notes

- The expected delivery timeline from the proposal is 9 to 11 weeks: approximately 5 to 7 weeks for the IMOS Knowledge Base Agent and 4 to 5 weeks for the Data Visualization AI Agent.
- The project should prioritize a reliable Storm Bay sea surface temperature demonstration before broadening dataset and region coverage.
- The key technical risks are prompt ambiguity, natural-language geolocation quality, large dataset performance, visual clutter from high-volume data, scope creep, and security around LLM-controlled tool use.
- Mitigations include few-shot prompt examples, retrieval grounding, curated regional lookup data, configurable data-size limits, aggregation and downsampling, read-only S3 permissions, and constrained tool interfaces.
- The product should use IMOS-specific terminology consistently so that the agent, documentation, tickets, and tests share the same domain language.
