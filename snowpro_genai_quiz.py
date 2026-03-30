import streamlit as st
import random

st.set_page_config(
    page_title="SnowPro Gen AI Quiz",
    page_icon=":material/school:",
    layout="centered",
)

QUESTIONS = [
    # =========================================================================
    # DOMAIN 1: Snowflake for Gen AI Overview (30%) — ~27 questions
    # =========================================================================
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which Snowflake Cortex feature is specifically designed for Retrieval Augmented Generation (RAG) over unstructured data?",
        "options": ["Cortex Analyst", "Cortex Search", "Cortex Fine-tuning", "Snowflake Copilot"],
        "answer": 1,
        "explanation": "Cortex Search is purpose-built for RAG use cases and unstructured data search.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What is the purpose of the CORTEX_MODELS_ALLOWLIST parameter?",
        "options": [
            "To enable cross-region inference",
            "To set up network policies for LLM access",
            "To restrict which LLM models can be used in an account",
            "To configure guardrails for LLM responses"
        ],
        "answer": 2,
        "explanation": "CORTEX_MODELS_ALLOWLIST lets administrators restrict access to specific LLM models within a Snowflake account.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/parameters#cortex-models-allowlist"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which parameter enables LLM inference across Snowflake regions?",
        "options": [
            "CROSS_REGION_INFERENCE",
            "CORTEX_ENABLED_CROSS_REGION",
            "CORTEX_MODELS_ALLOWLIST",
            "REGION_INFERENCE_ENABLED"
        ],
        "answer": 1,
        "explanation": "CORTEX_ENABLED_CROSS_REGION enables cross-region inference to improve availability and reduce latency.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#label-cortex-llm-cross-region"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which interface allows users to interactively test LLM prompts in Snowsight without writing SQL?",
        "options": [
            "Snowflake Copilot",
            "Cortex LLM Playground",
            "Cortex Analyst",
            "Streamlit in Snowflake"
        ],
        "answer": 1,
        "explanation": "Cortex LLM Playground (Public Preview) provides an interactive UI to test LLM prompts directly in Snowsight.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-llm-playground"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "How are Cortex Analyst semantic models stored in Snowflake?",
        "options": [
            "As tables in a schema",
            "As YAML files in a stage or natively in semantic views",
            "As JSON documents in a warehouse",
            "As Python objects in the Model Registry"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst semantic models can be stored as YAML files in a stage or natively in semantic views (Public Preview).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which Snowflake feature assists users with natural language SQL generation within worksheets?",
        "options": [
            "Cortex Analyst",
            "Cortex Search",
            "Snowflake Copilot",
            "Cortex Agents"
        ],
        "answer": 2,
        "explanation": "Snowflake Copilot assists users by generating SQL from natural language within Snowsight worksheets.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-copilot"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What are the three interfaces for invoking Cortex LLM functions?",
        "options": [
            "SQL, Python SDK, and Streamlit",
            "SQL, REST API, and Cortex LLM Playground",
            "REST API, Python SDK, and JDBC",
            "SQL, gRPC, and WebSocket"
        ],
        "answer": 1,
        "explanation": "Cortex LLM functions can be invoked via SQL, REST API, and the Cortex LLM Playground.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which two methods allow you to bring your own models into Snowflake?",
        "options": [
            "Cortex Fine-tuning and Cortex Search",
            "Snowflake Model Registry and Snowpark Container Services",
            "Cortex Analyst and Cortex Agents",
            "Snowflake Copilot and LLM Playground"
        ],
        "answer": 1,
        "explanation": "Custom models can be brought into Snowflake via the Snowflake Model Registry (serialized files) or Snowpark Container Services (Docker containers).",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What is a key consideration when enabling cross-region inference?",
        "options": [
            "It requires a dedicated virtual warehouse",
            "It may introduce additional latency",
            "It only works with Cortex Search",
            "It disables guardrails"
        ],
        "answer": 1,
        "explanation": "Cross-region inference may introduce latency as requests are routed to other regions for model availability.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#label-cortex-llm-cross-region"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which Cortex feature converts structured data questions into SQL queries?",
        "options": [
            "Cortex Search",
            "Cortex Analyst",
            "Cortex Fine-tuning",
            "COMPLETE function"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst performs text-to-SQL conversion for structured data analysis using semantic models.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What is the role of RBAC in the context of Snowflake Gen AI features?",
        "options": [
            "It controls which LLM models are available globally",
            "It manages role-based access to Cortex functions and resources",
            "It configures cross-region inference routing",
            "It sets token limits per user"
        ],
        "answer": 1,
        "explanation": "RBAC controls access to Cortex functions and Gen AI resources through role-based privileges.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/sql/grant-database-role"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which vector distance function measures the angle between two vectors?",
        "options": [
            "VECTOR_L1_DISTANCE",
            "VECTOR_L2_DISTANCE",
            "VECTOR_INNER_PRODUCT",
            "VECTOR_COSINE_SIMILARITY"
        ],
        "answer": 3,
        "explanation": "VECTOR_COSINE_SIMILARITY measures the cosine of the angle between two vectors, indicating directional similarity.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/vector_cosine_similarity"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What data type does Snowflake use to store vector embeddings?",
        "options": [
            "ARRAY",
            "VARIANT",
            "VECTOR",
            "FLOAT[]"
        ],
        "answer": 2,
        "explanation": "Snowflake has a dedicated VECTOR data type for storing vector embeddings efficiently.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/data-types-vector"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which SQL function creates a fine-tuning job in Snowflake Cortex?",
        "options": [
            "CORTEX.TRAIN('CREATE')",
            "SNOWFLAKE.CORTEX.FINETUNE('CREATE')",
            "CORTEX.FINE_TUNE('START')",
            "CREATE FINE_TUNING JOB"
        ],
        "answer": 1,
        "explanation": "FINETUNE('CREATE') in the SNOWFLAKE.CORTEX schema initiates a fine-tuning job.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-finetuning"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which vector function computes the sum of absolute differences between vector elements?",
        "options": [
            "VECTOR_INNER_PRODUCT",
            "VECTOR_L1_DISTANCE",
            "VECTOR_L2_DISTANCE",
            "VECTOR_COSINE_SIMILARITY"
        ],
        "answer": 1,
        "explanation": "VECTOR_L1_DISTANCE (Manhattan distance) computes the sum of absolute differences between corresponding elements.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/vector_l1_distance"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Cortex Agents are currently in which availability stage?",
        "options": [
            "Generally Available",
            "Public Preview",
            "Private Preview",
            "Deprecated"
        ],
        "answer": 1,
        "explanation": "Cortex Agents are in Public Preview as of the exam study guide (Feb 2026).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agent"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "How does the Snowflake Model Registry allow you to bring custom models?",
        "options": [
            "By uploading Docker containers",
            "By logging serialized model files (e.g., pickle, ONNX)",
            "By writing models in SQL",
            "By connecting to external REST APIs"
        ],
        "answer": 1,
        "explanation": "The Snowflake Model Registry accepts serialized model files like pickle, ONNX, or other formats for custom models.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which Cortex feature allows you to customize a pre-trained LLM with your own training data?",
        "options": [
            "Cortex Search",
            "Cortex Analyst",
            "Cortex Fine-tuning",
            "COMPLETE with system prompt"
        ],
        "answer": 2,
        "explanation": "Cortex Fine-tuning lets you customize pre-trained LLMs with your own training data for domain-specific tasks.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-finetuning"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What does the VECTOR_L2_DISTANCE function compute?",
        "options": [
            "Dot product of two vectors",
            "Cosine of the angle between vectors",
            "Euclidean distance between two vectors",
            "Manhattan distance between two vectors"
        ],
        "answer": 2,
        "explanation": "VECTOR_L2_DISTANCE computes the Euclidean (straight-line) distance between two vectors.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/vector_l2_distance"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which access control mechanism is used to grant privileges on Cortex AI features?",
        "options": [
            "Network policies",
            "GRANT DATABASE ROLE",
            "IP whitelisting",
            "OAuth scopes"
        ],
        "answer": 1,
        "explanation": "GRANT DATABASE ROLE is used to assign roles that control access to Cortex AI features.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/sql/grant-database-role"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Cortex Search exposes which type of API for application integration?",
        "options": [
            "gRPC API",
            "GraphQL API",
            "REST API",
            "WebSocket API"
        ],
        "answer": 2,
        "explanation": "Cortex Search provides REST APIs for integration with applications.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which function is the general-purpose LLM function in Snowflake Cortex for text generation?",
        "options": [
            "SUMMARIZE",
            "COMPLETE",
            "TRANSLATE",
            "EXTRACT_ANSWER"
        ],
        "answer": 1,
        "explanation": "COMPLETE is the general-purpose function for text generation using LLMs in Snowflake Cortex.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What does VECTOR_INNER_PRODUCT compute?",
        "options": [
            "The Euclidean distance between vectors",
            "The dot product of two vectors",
            "The cosine similarity between vectors",
            "The Manhattan distance between vectors"
        ],
        "answer": 1,
        "explanation": "VECTOR_INNER_PRODUCT computes the dot product (scalar product) of two vectors.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/vector_inner_product"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Semantic views for Cortex Analyst are currently in which availability stage?",
        "options": [
            "Generally Available",
            "Public Preview",
            "Private Preview",
            "Beta"
        ],
        "answer": 1,
        "explanation": "Semantic views as a native storage option for Cortex Analyst semantic models are in Public Preview.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which Snowflake Cortex LLM function should be used to generate an instructional lesson plan based on a prompt?",
        "options": [
            "COMPLETE",
            "EXTRACT_ANSWER",
            "SUMMARIZE",
            "TRANSLATE"
        ],
        "answer": 0,
        "explanation": "COMPLETE is the general-purpose LLM function for generating text content like lesson plans from prompts.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What is the primary difference between Cortex Search and Cortex Analyst?",
        "options": [
            "Cortex Search works with structured data; Cortex Analyst with unstructured",
            "Cortex Search is for RAG over unstructured data; Cortex Analyst is for text-to-SQL over structured data",
            "Cortex Search uses fine-tuned models; Cortex Analyst uses base models",
            "Cortex Search is GA; Cortex Analyst is deprecated"
        ],
        "answer": 1,
        "explanation": "Cortex Search handles RAG over unstructured data while Cortex Analyst converts natural language to SQL for structured data.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "What does Snowflake's guardrails feature do in the context of Gen AI?",
        "options": [
            "Encrypts LLM responses at rest",
            "Filters out harmful or unsafe LLM responses",
            "Limits the number of concurrent LLM requests",
            "Routes requests to the nearest region"
        ],
        "answer": 1,
        "explanation": "Guardrails (Cortex Guard) filter harmful or unsafe content from LLM responses.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    # =========================================================================
    # DOMAIN 2: Snowflake Gen AI & LLM Functions (44%) — ~40 questions
    # =========================================================================
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which Cortex function returns a sentiment score between -1 and 1?",
        "options": [
            "CLASSIFY_TEXT",
            "SENTIMENT",
            "EXTRACT_ANSWER",
            "SUMMARIZE"
        ],
        "answer": 1,
        "explanation": "SENTIMENT returns a score from -1 (negative) to 1 (positive) indicating the sentiment of the input text.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/sentiment-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which function translates text from one language to another in Snowflake Cortex?",
        "options": [
            "COMPLETE",
            "SUMMARIZE",
            "TRANSLATE",
            "EXTRACT_ANSWER"
        ],
        "answer": 2,
        "explanation": "TRANSLATE is the dedicated Cortex function for language translation.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/translate-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does the CLASSIFY_TEXT function do?",
        "options": [
            "Translates text to a target language",
            "Assigns text to one of the provided categories",
            "Extracts answers from a document",
            "Generates embeddings for text"
        ],
        "answer": 1,
        "explanation": "CLASSIFY_TEXT categorizes input text into one of the user-specified categories.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/classify_text-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which Cortex function extracts specific answers from a text passage given a question?",
        "options": [
            "SUMMARIZE",
            "CLASSIFY_TEXT",
            "EXTRACT_ANSWER",
            "COMPLETE"
        ],
        "answer": 2,
        "explanation": "EXTRACT_ANSWER finds and returns answers to a question from a provided text passage.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/extract_answer-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the difference between EMBED_TEXT_768 and EMBED_TEXT_1024?",
        "options": [
            "They use different LLM models",
            "They produce embeddings of different dimensions (768 vs 1024)",
            "768 is for English only; 1024 supports all languages",
            "768 is deprecated in favor of 1024"
        ],
        "answer": 1,
        "explanation": "EMBED_TEXT_768 produces 768-dimensional embeddings and EMBED_TEXT_1024 produces 1024-dimensional embeddings.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/embed_text-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does the COUNT_TOKENS helper function do?",
        "options": [
            "Counts the number of words in a string",
            "Counts the number of tokens a given model will use for the input text",
            "Counts the API calls made to Cortex functions",
            "Counts the rows processed by a Cortex function"
        ],
        "answer": 1,
        "explanation": "COUNT_TOKENS returns the number of tokens that a specified model would use for the given input text.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/count_tokens-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does TRY_COMPLETE do compared to COMPLETE?",
        "options": [
            "It uses a different model architecture",
            "It returns NULL instead of raising an error on failure",
            "It provides streaming output",
            "It is faster but less accurate"
        ],
        "answer": 1,
        "explanation": "TRY_COMPLETE is a non-error-raising variant of COMPLETE that returns NULL on failure instead of an error.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/try_complete-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the purpose of SPLIT_TEXT_RECURSIVE_CHARACTER?",
        "options": [
            "To tokenize text for embedding",
            "To split large text into smaller chunks recursively using character separators",
            "To separate multilingual text by language",
            "To parse JSON strings into arrays"
        ],
        "answer": 1,
        "explanation": "SPLIT_TEXT_RECURSIVE_CHARACTER splits large text into smaller chunks using recursive character-based splitting, useful for preparing text for embeddings or LLM processing.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/split_text_recursive_character-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does COMPLETE Structured Outputs enable?",
        "options": [
            "Generating responses in markdown format",
            "Returning LLM responses as structured JSON matching a specified schema",
            "Creating tabular outputs from LLM responses",
            "Compiling LLM outputs into SQL tables"
        ],
        "answer": 1,
        "explanation": "COMPLETE Structured Outputs allows you to get LLM responses as structured JSON conforming to a user-defined schema.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/complete-structured-outputs"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the Cortex Analyst Verified Query Repository (VQR)?",
        "options": [
            "A database of pre-built SQL queries",
            "A collection of verified question-SQL pairs that improve Analyst accuracy",
            "A query cache for frequently asked questions",
            "A version control system for SQL queries"
        ],
        "answer": 1,
        "explanation": "VQR contains verified question-to-SQL mappings that help Cortex Analyst generate more accurate SQL for known question patterns.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/verified-query-repository"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does the custom_instructions field do in a Cortex Analyst semantic model?",
        "options": [
            "Defines the database connection string",
            "Provides natural language guidance to influence SQL generation behavior",
            "Sets the LLM model to use",
            "Configures cross-region inference"
        ],
        "answer": 1,
        "explanation": "The custom_instructions field allows you to provide natural language instructions that guide how Cortex Analyst generates SQL.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the Suggested Questions feature in Cortex Analyst?",
        "options": [
            "Pre-defined questions that users must choose from",
            "Auto-generated follow-up questions based on the semantic model and conversation context",
            "A list of frequently asked questions from all users",
            "Template questions for building VQR entries"
        ],
        "answer": 1,
        "explanation": "Suggested Questions automatically generates relevant follow-up questions based on the semantic model and current conversation.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/suggested-questions"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the primary role of memory in a multi-turn chat conversation using a Gen AI model in Snowflake Cortex?",
        "options": [
            "To securely store user credentials",
            "To increase the speed of response generation",
            "To maintain context throughout multiple requests",
            "To limit the number of tokens processed for each request"
        ],
        "answer": 2,
        "explanation": "Memory in multi-turn conversations maintains context across multiple interactions so the model can provide relevant follow-up responses.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "When building a chat interface with Streamlit and Cortex, which is typically required?",
        "options": [
            "ACCOUNTADMIN role",
            "Appropriate privileges to call Cortex functions",
            "A dedicated compute pool",
            "An external API integration"
        ],
        "answer": 1,
        "explanation": "Users need appropriate privileges (via RBAC) to invoke Cortex functions within Streamlit applications.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In a data pipeline, which Cortex function would you use to extract structured information from unstructured text like transcripts?",
        "options": [
            "TRANSLATE",
            "SENTIMENT",
            "COMPLETE",
            "SUMMARIZE"
        ],
        "answer": 2,
        "explanation": "COMPLETE can be prompted to extract structured data from unstructured text like transcripts, invoices, or reports.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is PARSE_DOCUMENT used for?",
        "options": [
            "Parsing SQL queries for optimization",
            "Extracting text and layout information from documents (PDF, images)",
            "Parsing JSON files into tables",
            "Converting YAML semantic models to SQL"
        ],
        "answer": 1,
        "explanation": "PARSE_DOCUMENT extracts text and layout information from documents like PDFs and images.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/parse_document-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which Snowpark Container Services component defines the container configuration?",
        "options": [
            "Docker Compose file",
            "Kubernetes manifest",
            "Specification file",
            "Container policy"
        ],
        "answer": 2,
        "explanation": "SPCS uses specification files to define container configuration including image, resources, endpoints, and environment.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What SQL command creates a compute pool for SPCS?",
        "options": [
            "CREATE WAREHOUSE",
            "CREATE COMPUTE POOL",
            "CREATE RESOURCE POOL",
            "ALTER ACCOUNT SET COMPUTE_POOL"
        ],
        "answer": 1,
        "explanation": "CREATE COMPUTE POOL creates the GPU/CPU compute resources needed for Snowpark Container Services.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/sql/create-compute-pool"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is an image repository in SPCS?",
        "options": [
            "A Git repository for container code",
            "A Snowflake-managed registry for storing Docker images",
            "A stage for storing model artifacts",
            "A catalog of pre-built container templates"
        ],
        "answer": 1,
        "explanation": "An image repository in SPCS is a Snowflake-managed Docker image registry for storing and managing container images.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-registry-repository"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "How do you log a model to the Snowflake Model Registry?",
        "options": [
            "Using CREATE MODEL SQL command",
            "Using snowflake.ml.registry.Registry.log_model()",
            "Using PUT command to upload to a stage",
            "Using ALTER MODEL ADD VERSION"
        ],
        "answer": 1,
        "explanation": "The Python API snowflake.ml.registry.Registry.log_model() is used to log models to the Snowflake Model Registry.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which key factor should you consider when choosing between different LLM models in Cortex?",
        "options": [
            "The color of the Snowsight theme",
            "Capability, latency, and cost trade-offs",
            "The geographic location of the data",
            "The programming language used in queries"
        ],
        "answer": 1,
        "explanation": "When choosing an LLM model, consider the trade-offs between capability (quality), latency (speed), and cost.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "How can Cortex Analyst be integrated with Cortex Search?",
        "options": [
            "They cannot be used together",
            "Cortex Search can provide additional context to improve Cortex Analyst responses",
            "Cortex Analyst replaces Cortex Search entirely",
            "They share the same REST API endpoint"
        ],
        "answer": 1,
        "explanation": "Cortex Search can enhance Cortex Analyst by providing relevant unstructured context (literal search) to improve SQL generation accuracy.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/improve-literal-search"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the SUMMARIZE function used for?",
        "options": [
            "Summarizing query execution plans",
            "Generating concise summaries of input text",
            "Summarizing table statistics",
            "Creating summary views of databases"
        ],
        "answer": 1,
        "explanation": "SUMMARIZE generates a concise summary of the provided input text.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/summarize-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "When using Cortex functions in a data pipeline for data enrichment, which approach is typical?",
        "options": [
            "Call Cortex functions from external Python scripts via API",
            "Use Cortex functions directly in SQL SELECT statements on table data",
            "Export data to CSV, process externally, then re-import",
            "Use Cortex functions only in Streamlit apps"
        ],
        "answer": 1,
        "explanation": "Cortex functions can be called directly in SQL SELECT statements to enrich, augment, or transform data in pipelines.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which function generates vector embeddings for text in Snowflake Cortex?",
        "options": [
            "COMPLETE",
            "VECTOR_COSINE_SIMILARITY",
            "EMBED_TEXT_768 or EMBED_TEXT_1024",
            "CLASSIFY_TEXT"
        ],
        "answer": 2,
        "explanation": "EMBED_TEXT_768 and EMBED_TEXT_1024 generate vector embeddings of different dimensionalities for text.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/embed_text-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In SPCS, what is the first step to deploy a custom model?",
        "options": [
            "Create a compute pool",
            "Build and push a Docker image to an image repository",
            "Create a specification file",
            "Grant USAGE on the database"
        ],
        "answer": 1,
        "explanation": "The first step is to build a Docker image and push it to a Snowflake image repository, then create a spec file and compute pool.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does the Cortex Analyst semantic model specification define?",
        "options": [
            "The physical storage layout of tables",
            "Tables, columns, relationships, metrics, and time dimensions for text-to-SQL",
            "Network security policies for API access",
            "The LLM model to use for inference"
        ],
        "answer": 1,
        "explanation": "The semantic model specification defines tables, columns, joins, metrics, time dimensions, and other metadata for text-to-SQL generation.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/semantic-model-spec"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "How do you call a model that has been logged in the Snowflake Model Registry?",
        "options": [
            "Using CALL MODEL_NAME.PREDICT() SQL syntax",
            "Using the model version's predict() or run() method via Python API",
            "Using a dedicated REST endpoint auto-created for each model",
            "Using EXECUTE MODEL command"
        ],
        "answer": 1,
        "explanation": "Logged models can be called via the Python API using methods like predict() on the model version object.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the benefit of using fine-tuning over prompt engineering with COMPLETE?",
        "options": [
            "Fine-tuning is always cheaper",
            "Fine-tuning can improve accuracy for domain-specific tasks without long prompts",
            "Fine-tuning works without any training data",
            "Fine-tuning is required for all Cortex functions"
        ],
        "answer": 1,
        "explanation": "Fine-tuning customizes the model for specific domains, reducing the need for lengthy prompts while improving accuracy.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-finetuning"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which Cortex Analyst feature can integrate with Cortex Search to enhance literal value matching in SQL generation?",
        "options": [
            "VQR (Verified Query Repository)",
            "Literal search integration",
            "custom_instructions",
            "Suggested Questions"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst can use Cortex Search for literal search to improve matching of specific values (names, codes) in generated SQL.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/improve-literal-search"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is a key performance consideration when choosing between a larger and smaller LLM in Cortex?",
        "options": [
            "Larger models always produce better results",
            "Smaller models have lower latency but may sacrifice capability",
            "Model size doesn't affect performance",
            "Larger models are always cheaper"
        ],
        "answer": 1,
        "explanation": "Smaller models offer lower latency and cost but may have reduced capability; larger models are more capable but slower and more expensive.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "When enriching a table with sentiment scores using Cortex, which SQL pattern is most appropriate?",
        "options": [
            "CREATE TABLE ... AS SELECT SNOWFLAKE.CORTEX.SENTIMENT(text_col) FROM source",
            "INSERT INTO target SELECT CORTEX.ML.SENTIMENT(text_col) FROM source",
            "UPDATE source SET sentiment = EXTERNAL_FUNCTION('sentiment', text_col)",
            "CALL SNOWFLAKE.CORTEX.BATCH_SENTIMENT('source', 'text_col')"
        ],
        "answer": 0,
        "explanation": "Cortex functions are called inline in SQL: SELECT SNOWFLAKE.CORTEX.SENTIMENT(column) FROM table.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/sentiment-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What does the Cortex Agents REST API enable?",
        "options": [
            "Only SQL query execution",
            "Orchestrating multi-step AI workflows that combine tools and LLMs",
            "Managing Snowflake user accounts",
            "Monitoring warehouse performance"
        ],
        "answer": 1,
        "explanation": "Cortex Agents enable orchestrating multi-step AI workflows that combine LLMs with various tools and data sources.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agent"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which Cortex function would you use to process a scanned invoice PDF?",
        "options": [
            "EXTRACT_ANSWER",
            "PARSE_DOCUMENT",
            "SUMMARIZE",
            "CLASSIFY_TEXT"
        ],
        "answer": 1,
        "explanation": "PARSE_DOCUMENT extracts text and layout from documents like scanned PDFs and images.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/parse_document-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is required to create a service in Snowpark Container Services?",
        "options": [
            "A Docker image, a specification file, and a compute pool",
            "A Python script and a virtual warehouse",
            "A Kubernetes cluster and helm chart",
            "An external function and API integration"
        ],
        "answer": 0,
        "explanation": "Creating an SPCS service requires a Docker image in an image repository, a specification file, and a compute pool.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In a multi-turn chat architecture, how is conversation history typically managed?",
        "options": [
            "Stored in a Snowflake table automatically",
            "Passed as part of the messages array in each COMPLETE call",
            "Managed by Snowflake's internal session cache",
            "Stored in browser cookies"
        ],
        "answer": 1,
        "explanation": "In multi-turn chat, conversation history is passed as an array of messages in each COMPLETE call to maintain context.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which approach uses Cortex for data transformation in a pipeline?",
        "options": [
            "Using COMPLETE to reformat or restructure text data in SQL queries",
            "Exporting data to Python, transforming, and re-importing",
            "Using only TRANSLATE for all transformation tasks",
            "Creating external functions for each transformation"
        ],
        "answer": 0,
        "explanation": "COMPLETE can be used directly in SQL to transform, restructure, or augment text data within data pipelines.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What is the snowflake.ml.registry.Registry class used for?",
        "options": [
            "Managing Snowflake user roles",
            "Logging, versioning, and managing ML models in Snowflake",
            "Creating Cortex Search services",
            "Configuring Cortex Analyst semantic models"
        ],
        "answer": 1,
        "explanation": "The Registry class in snowflake.ml.registry is the Python API for logging, versioning, and managing ML models.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview"
    },
    # =========================================================================
    # DOMAIN 3: Snowflake Gen AI Governance (26%) — ~23 questions
    # =========================================================================
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "A Gen AI Specialist needs to analyze the daily costs incurred for AI services in Snowflake. Which query retrieves credit consumption from Snowflake's metadata?",
        "options": [
            "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY WHERE SERVICE_TYPE='AI_SERVICES'",
            "SELECT * FROM SNOWFLAKE.INFORMATION_SCHEMA.METERING_HISTORY WHERE SERVICE_TYPE='AI_SERVICES'",
            "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_HISTORY WHERE SERVICE_TYPE='AI_SERVICES'",
            "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.METERING_DAILY_HISTORY WHERE SERVICE_TYPE='AI_SERVICES'"
        ],
        "answer": 3,
        "explanation": "METERING_DAILY_HISTORY in ACCOUNT_USAGE provides daily credit consumption data for AI services.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/account-usage/metering_daily_history"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which view tracks per-function usage of Cortex LLM functions?",
        "options": [
            "QUERY_HISTORY",
            "CORTEX_FUNCTIONS_USAGE_HISTORY",
            "METERING_DAILY_HISTORY",
            "WAREHOUSE_METERING_HISTORY"
        ],
        "answer": 1,
        "explanation": "CORTEX_FUNCTIONS_USAGE_HISTORY tracks usage details for individual Cortex LLM functions.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_functions_usage_history"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What does the CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view provide?",
        "options": [
            "Aggregate monthly costs for all Cortex functions",
            "Per-query token usage and cost details for Cortex function calls",
            "A list of all available Cortex functions",
            "Query execution plans for Cortex functions"
        ],
        "answer": 1,
        "explanation": "CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY provides per-query details on token usage and costs for Cortex function calls.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_functions_query_usage_history"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What is Cortex Guard used for?",
        "options": [
            "Encrypting LLM model weights",
            "Filtering harmful or unsafe content from LLM responses",
            "Guarding against SQL injection in Cortex Analyst",
            "Protecting API keys for REST endpoints"
        ],
        "answer": 1,
        "explanation": "Cortex Guard is a guardrail feature that filters harmful, unsafe, or inappropriate content from LLM responses.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "How is Cortex Guard enabled in a COMPLETE call?",
        "options": [
            "By setting a separate GUARD parameter on the account",
            "By passing guardrails configuration as arguments to the COMPLETE function",
            "By creating a separate Cortex Guard service",
            "Cortex Guard is always enabled by default"
        ],
        "answer": 1,
        "explanation": "Cortex Guard is enabled by passing guardrails arguments within the COMPLETE function call.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which parameter restricts access to specific LLMs within Snowflake?",
        "options": [
            "NETWORK_POLICY",
            "SAML_IDENTITY_PROVIDER",
            "CORTEX_MODELS_ALLOWLIST",
            "CORTEX_ENABLED_CROSS_REGION"
        ],
        "answer": 2,
        "explanation": "CORTEX_MODELS_ALLOWLIST restricts which LLM models can be used in the account.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/parameters#cortex-models-allowlist"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "CORTEX_MODELS_ALLOWLIST applies to which of the following? (Select all that apply conceptually)",
        "options": [
            "COMPLETE, TRY_COMPLETE, Cortex LLM REST API, and LLM Playground",
            "Only COMPLETE and TRY_COMPLETE SQL functions",
            "Only the Cortex LLM REST API",
            "Only the Cortex LLM Playground"
        ],
        "answer": 0,
        "explanation": "CORTEX_MODELS_ALLOWLIST applies to COMPLETE, TRY_COMPLETE, the Cortex LLM REST API, and the LLM Playground.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/parameters#cortex-models-allowlist"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Does data leave Snowflake when using Cortex LLM functions?",
        "options": [
            "Yes, data is always sent to external LLM providers",
            "No, Cortex LLM functions run within Snowflake's security perimeter",
            "Only when cross-region inference is enabled",
            "Only for fine-tuning jobs"
        ],
        "answer": 1,
        "explanation": "Cortex LLM functions run within Snowflake's infrastructure, so data does not leave Snowflake's security perimeter.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What are the three types of costs associated with Cortex Search?",
        "options": [
            "Compute, storage, and networking",
            "Virtual warehouse, EMBED_TEXT, and Serving",
            "Indexing, querying, and caching",
            "CPU, GPU, and memory"
        ],
        "answer": 1,
        "explanation": "Cortex Search incurs costs for virtual warehouse (indexing), EMBED_TEXT (embedding generation), and Serving (query processing).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-cost"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which view tracks daily usage specifically for Cortex Search services?",
        "options": [
            "CORTEX_FUNCTIONS_USAGE_HISTORY",
            "METERING_DAILY_HISTORY",
            "CORTEX_SEARCH_DAILY_USAGE_HISTORY",
            "QUERY_HISTORY"
        ],
        "answer": 2,
        "explanation": "CORTEX_SEARCH_DAILY_USAGE_HISTORY specifically tracks daily usage metrics for Cortex Search services.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_search_daily_usage_history"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "How can you minimize token costs when using Cortex LLM functions?",
        "options": [
            "Use the largest model available for best results",
            "Minimize input/output tokens by using concise prompts and appropriate models",
            "Always enable cross-region inference",
            "Use only the REST API instead of SQL"
        ],
        "answer": 1,
        "explanation": "Minimizing tokens through concise prompts and selecting appropriately-sized models helps reduce LLM costs.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What is the Snowflake Service Consumption Table used for in the context of Cortex Analyst?",
        "options": [
            "Tracking query execution times",
            "Monitoring credit consumption for Cortex Analyst usage",
            "Listing available LLM models",
            "Storing semantic model definitions"
        ],
        "answer": 1,
        "explanation": "The Snowflake Service Consumption Table tracks credit consumption for services including Cortex Analyst.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/cortex-analyst/cortex-analyst-costs"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What authentication method is used for the Cortex LLM REST API?",
        "options": [
            "API keys only",
            "OAuth or key-pair authentication",
            "Basic username/password",
            "SAML SSO only"
        ],
        "answer": 1,
        "explanation": "The Cortex LLM REST API supports standard Snowflake authentication methods including OAuth and key-pair authentication.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-llm-rest-api"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What is the Trulens SDK used for in Snowflake?",
        "options": [
            "Building Streamlit applications",
            "Implementing AI observability: evaluation, tracing, and logging",
            "Managing Snowflake user roles",
            "Creating fine-tuning datasets"
        ],
        "answer": 1,
        "explanation": "The Trulens SDK provides AI observability capabilities including evaluation metrics, tracing, and logging for AI applications.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which AI observability feature stores telemetry data for Cortex AI applications?",
        "options": [
            "Query history tables",
            "Event tables",
            "Information schema views",
            "Audit logs"
        ],
        "answer": 1,
        "explanation": "Event tables store AI observability telemetry data including traces, logs, and evaluation results.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which method helps reduce LLM hallucinations?",
        "options": [
            "Increasing the temperature parameter",
            "Using RAG with Cortex Search to ground responses in factual data",
            "Using the largest model available",
            "Disabling guardrails"
        ],
        "answer": 1,
        "explanation": "RAG (using Cortex Search) grounds LLM responses in factual, retrieved data, reducing hallucinations.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What does snowflake.cortex.CompleteOptions allow you to configure?",
        "options": [
            "The Snowflake warehouse size",
            "Options for the COMPLETE function such as temperature, max_tokens, and guardrails",
            "Database and schema for model storage",
            "Cross-region routing preferences"
        ],
        "answer": 1,
        "explanation": "CompleteOptions lets you configure COMPLETE function parameters including temperature, max_tokens, guardrails, and more.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/complete-options"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What type of warehouse is recommended for running heavy ML workloads in Snowflake?",
        "options": [
            "Standard warehouse",
            "Snowpark-optimized warehouse",
            "Multi-cluster warehouse",
            "Serverless warehouse"
        ],
        "answer": 1,
        "explanation": "Snowpark-optimized warehouses provide more memory per node, suitable for heavy ML and data-intensive workloads.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/warehouses-snowpark-optimized"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which AI observability feature allows you to compare different model configurations or prompts?",
        "options": [
            "Tracing",
            "Logging",
            "Comparisons",
            "Event tables"
        ],
        "answer": 2,
        "explanation": "The Comparisons feature in AI observability lets you compare different model configurations, prompts, or versions.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What is the purpose of usage quotas in the context of Cortex functions?",
        "options": [
            "To limit the number of users who can access Cortex",
            "To control and limit token/credit consumption for Cortex functions",
            "To restrict the number of SQL queries per day",
            "To limit the size of input documents"
        ],
        "answer": 1,
        "explanation": "Usage quotas help control and limit token or credit consumption for Cortex LLM functions to manage costs.",
        "doc_url": "https://docs.snowflake.com/en/sql-reference/account-usage/cortex_functions_usage_history"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What is tracing in the context of Snowflake AI observability?",
        "options": [
            "Tracking network packets between Snowflake and clients",
            "Recording the step-by-step execution flow of AI application calls",
            "Monitoring warehouse query performance",
            "Logging user authentication events"
        ],
        "answer": 1,
        "explanation": "Tracing records the step-by-step execution flow of AI application calls for debugging and optimization.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "How can administrators monitor Cortex Analyst usage?",
        "options": [
            "Through the Cortex Analyst administrator monitoring dashboard",
            "Only through raw SQL query logs",
            "By checking the Model Registry",
            "Through Snowflake Copilot analytics"
        ],
        "answer": 0,
        "explanation": "Snowflake provides Cortex Analyst administrator monitoring for tracking usage and performance.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/cortex-analyst-costs"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What evaluation metrics are available in Snowflake's AI observability?",
        "options": [
            "Only accuracy and F1 score",
            "Custom metrics defined via Trulens SDK including relevance, groundedness, and more",
            "Only latency and throughput metrics",
            "Only cost-based metrics"
        ],
        "answer": 1,
        "explanation": "Snowflake AI observability supports custom evaluation metrics via the Trulens SDK including relevance, groundedness, and user-defined metrics.",
        "doc_url": "https://docs.snowflake.com/en/developer-guide/snowflake-cortex/ai-observability"
    },
    # =========================================================================
    # V2: Doc-grounded questions from live Snowflake docs + community exam intel
    # =========================================================================
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "A security administrator wants to ensure that all users in the account can use Cortex AI functions by default, without any additional configuration. Which statement about the SNOWFLAKE.CORTEX_USER database role is correct?",
        "options": [
            "CORTEX_USER must be explicitly granted to each user before they can use Cortex AI functions",
            "CORTEX_USER is granted to the PUBLIC role by default, giving all users access",
            "CORTEX_USER is granted to SYSADMIN by default, and SYSADMIN must propagate it",
            "CORTEX_USER is only available after enabling the ENABLE_CORTEX_AI account parameter"
        ],
        "answer": 1,
        "explanation": "SNOWFLAKE.CORTEX_USER is granted to PUBLIC by default. Since PUBLIC is automatically granted to all users and roles, all users can use Cortex AI functions without additional configuration.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "An admin needs to grant SNOWFLAKE.CORTEX_ANALYST_USER to a specific analyst named 'jane'. Which approach is correct?",
        "options": [
            "GRANT DATABASE ROLE SNOWFLAKE.CORTEX_ANALYST_USER TO USER jane",
            "GRANT DATABASE ROLE SNOWFLAKE.CORTEX_ANALYST_USER TO ROLE analyst_role, then GRANT ROLE analyst_role TO USER jane",
            "GRANT ROLE SNOWFLAKE.CORTEX_ANALYST_USER TO USER jane",
            "ALTER USER jane SET DEFAULT_SECONDARY_ROLES = ('SNOWFLAKE.CORTEX_ANALYST_USER')"
        ],
        "answer": 1,
        "explanation": "Database roles cannot be granted directly to users in Snowflake. They must be granted to account-level roles first, then those roles are granted to users.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "A company wants only 'ml_engineers' to use Cortex Agents and only 'analysts' to use Cortex Analyst — after revoking CORTEX_USER from PUBLIC. Which database roles should be granted?",
        "options": [
            "Grant CORTEX_AGENT_USER to ml_engineers and CORTEX_USER to analysts",
            "Grant CORTEX_AGENT_USER to ml_engineers and CORTEX_ANALYST_USER to analysts",
            "Grant CORTEX_USER to both but set CORTEX_MODELS_ALLOWLIST differently per role",
            "Grant CORTEX_AGENT_USER to ml_engineers and set ENABLE_CORTEX_ANALYST = TRUE for analysts"
        ],
        "answer": 1,
        "explanation": "CORTEX_AGENT_USER, CORTEX_ANALYST_USER, and CORTEX_EMBED_USER are separate database roles for fine-grained access. Each grants access only to its specific feature.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "A Snowflake account was created in AWS US-East-1 in January 2026. The admin has not changed any cross-region settings. What is the default value of CORTEX_ENABLED_CROSS_REGION?",
        "options": [
            "ANY_REGION",
            "DISABLED",
            "AWS_US",
            "The account's home region only"
        ],
        "answer": 1,
        "explanation": "For most existing accounts, CORTEX_ENABLED_CROSS_REGION defaults to DISABLED. ANY_REGION is only the default for new accounts in new organizations within commercial regions created after March 9, 2026.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "An ORGADMIN tries to enable cross-region inference by running ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'ANY_REGION'. What happens?",
        "options": [
            "The setting is applied to all accounts in the organization",
            "The command fails because only ACCOUNTADMIN can set this parameter",
            "The setting is applied but only for the ORGADMIN's own account",
            "The command succeeds but requires SECURITYADMIN to activate it per-account"
        ],
        "answer": 1,
        "explanation": "CORTEX_ENABLED_CROSS_REGION can only be set at the account level by ACCOUNTADMIN. The ORGADMIN role cannot set this parameter.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "A compliance officer requires cross-region inference only in AWS US and EU regions. Which statement is correct?",
        "options": [
            "ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'AWS_US | AWS_EU'",
            "ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'AWS_US,AWS_EU'",
            "ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'ANY_REGION' EXCLUDE 'AZURE,GCP'",
            "ALTER ACCOUNT SET CORTEX_CROSS_REGION_ALLOWLIST = ['AWS_US', 'AWS_EU']"
        ],
        "answer": 1,
        "explanation": "Valid values for CORTEX_ENABLED_CROSS_REGION include DISABLED, ANY_REGION, or specific regions like AWS_US, AWS_EU separated by commas in a single string.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "When cross-region inference is enabled and both source and processing regions are in AWS, how is data transmitted?",
        "options": [
            "Data traverses the public internet using HTTPS/TLS",
            "Data stays within the AWS global network, encrypted at the physical layer",
            "Data is routed through Snowflake's dedicated private link across regions",
            "Data is replicated to the target region before processing begins"
        ],
        "answer": 1,
        "explanation": "If both regions are in AWS, data stays within the AWS global network with automatic encryption at the physical layer. mTLS is used only when crossing cloud providers.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "A developer building a Cortex Agent needs to maintain conversation context between API calls without managing state client-side. Which feature should they use?",
        "options": [
            "Pass the full message history in each API request",
            "Use Cortex Agent threads to persist conversation context",
            "Store conversation state in a Snowflake session variable",
            "Enable the PERSIST_CONTEXT parameter in the agent configuration"
        ],
        "answer": 1,
        "explanation": "Cortex Agents use threads to persist interaction context. A thread object is created and its ID referenced in subsequent interactions, removing the need for client-side state management.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "A Cortex Agent needs real-time internet access during conversations. Which statement about web search is true?",
        "options": [
            "Web search uses Google Custom Search API and stores queries for 30 days",
            "Web search uses the Brave Web Search API with zero data retention (ZDR)",
            "Web search requires configuring an external access integration and API key per agent",
            "Web search is automatically enabled for all agents without account-level configuration"
        ],
        "answer": 1,
        "explanation": "Cortex Agents use the Brave Web Search API with zero data retention (ZDR) — no queries, results, or metadata are stored by Brave. An ACCOUNTADMIN must enable web search at the account level first.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "When creating a Cortex Agent, which model selection does Snowflake recommend?",
        "options": [
            "Always use claude-3-5-sonnet for highest accuracy",
            "Select 'auto' so Cortex automatically selects the highest quality model and improves over time",
            "Use llama3.1-70b for the best cost-to-performance ratio",
            "Use mistral-large2 as the only model supporting agent orchestration"
        ],
        "answer": 1,
        "explanation": "Snowflake recommends selecting 'auto' for the model. Cortex then automatically selects the highest quality available model, and quality improves as new models are added.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "An admin wants to completely disable Cortex Analyst, even for ACCOUNTADMIN users. Which approach achieves this?",
        "options": [
            "Revoke SNOWFLAKE.CORTEX_ANALYST_USER from all roles including ACCOUNTADMIN",
            "Set ENABLE_CORTEX_ANALYST = FALSE using ALTER ACCOUNT",
            "Set CORTEX_MODELS_ALLOWLIST = 'None' to block all models",
            "Revoke SNOWFLAKE.CORTEX_USER from the PUBLIC role"
        ],
        "answer": 1,
        "explanation": "ENABLE_CORTEX_ANALYST = FALSE prevents even ACCOUNTADMIN from using Analyst. This is one of the few AI features gated by a parameter rather than RBAC.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 1: Gen AI Overview",
        "question": "Which combination of search techniques does Cortex Search use under the hood?",
        "options": [
            "Vector search only with automatic query expansion",
            "Keyword search with TF-IDF scoring and BM25 ranking",
            "Vector search, keyword search, and semantic reranking",
            "Dense passage retrieval with cross-encoder scoring only"
        ],
        "answer": 2,
        "explanation": "Cortex Search uses a hybrid approach: vector search (semantic similarity) + keyword search (lexical matching) + semantic reranking for high quality results.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A data engineer provisions an XL warehouse for AI_COMPLETE calls on a large table expecting faster throughput. What is the likely outcome?",
        "options": [
            "The XL warehouse processes calls significantly faster than a MEDIUM warehouse",
            "The XL warehouse provides no performance improvement over MEDIUM but costs more",
            "The XL warehouse fails because AI functions have a maximum warehouse size of MEDIUM",
            "The XL warehouse improves only AI_COMPLETE but not other AI functions"
        ],
        "answer": 1,
        "explanation": "Snowflake recommends MEDIUM or smaller for Cortex AI functions. Larger warehouses do not increase performance but incur higher costs.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A team is setting up Cortex Analyst. What is the recommended approach for defining business metrics, dimensions, and relationships?",
        "options": [
            "Create a YAML file and upload it to a Snowflake stage",
            "Create semantic views — native Snowflake schema-level objects",
            "Define the semantic model inline in each REST API request",
            "Create a data dictionary table that Cortex Analyst reads automatically"
        ],
        "answer": 1,
        "explanation": "Semantic views are the recommended approach for Cortex Analyst. They provide native RBAC, sharing, advanced features like derived metrics, and access modifiers.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A role only has access to claude-3-5-sonnet and llama3.1-70b via model-level RBAC. When using Cortex Analyst, which model is selected?",
        "options": [
            "llama3.1-70b because it is the most cost-effective",
            "claude-3-5-sonnet because it is the highest-ranked in Cortex Analyst's preference order",
            "A random selection between the two per request",
            "The request fails because neither model supports Cortex Analyst"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst selects models in preference order: Claude Sonnet 4 > 3.7 > 3.5 > GPT 4.1 > Arctic Text2SQL > Mistral+Llama. claude-3-5-sonnet is the highest-ranked available model.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In a multi-turn Cortex Analyst conversation, a user asks 'What are our top 5 products?' then 'Show me the monthly trend for the third one.' What happens?",
        "options": [
            "Cortex Analyst retrieves first query results and uses the third product for follow-up SQL",
            "Cortex Analyst fails because it cannot access results of previous SQL queries",
            "Cortex Analyst caches all SQL results and auto-joins them with follow-up queries",
            "Cortex Analyst re-executes the first query internally to resolve the reference"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst cannot access results of previous SQL queries in multi-turn conversations. It can reference conversation text and SQL but not actual data returned. The user must specify the product name explicitly.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "When passing conversation history to Cortex Analyst for multi-turn, which role values are valid in the messages array?",
        "options": [
            "'user' and 'assistant'",
            "'user' and 'analyst'",
            "'human' and 'ai'",
            "'user' and 'system'"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst uses roles 'user' (for questions) and 'analyst' (for responses). Analyst responses contain both text and SQL content types.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A user asks Cortex Analyst: 'What trends do you observe in our Q4 sales data?' What is the expected response?",
        "options": [
            "SQL calculating quarter-over-quarter growth rates",
            "SQL with AI-generated insights appended",
            "Cortex Analyst indicates it cannot answer because it only generates SQL, not insights",
            "Cortex Analyst calls AI_COMPLETE internally to generate insights"
        ],
        "answer": 2,
        "explanation": "Cortex Analyst is limited to questions resolvable with SQL. It does not generate insights for broad business questions like 'What trends do you observe?'",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "What components can a semantic view define for Cortex Analyst?",
        "options": [
            "Tables, columns, and primary keys only",
            "Logical tables, dimensions, facts, metrics, and relationships",
            "Tables, views, stored procedures, and UDFs",
            "Tables, indexes, materialized views, and constraints"
        ],
        "answer": 1,
        "explanation": "Semantic views define: logical tables (business entities), dimensions (categorical context), facts (quantitative data), metrics (aggregated KPIs), and relationships (join paths).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A multilingual Cortex Search Service needs to index English, French, and Japanese documents. Which embedding model should be selected?",
        "options": [
            "snowflake-arctic-embed-m-v1.5 (default) — it supports all languages",
            "snowflake-arctic-embed-l-v2.0 — the multilingual model with 1024 dimensions",
            "e5-base-v2 — widest language support",
            "voyage-multilingual-2 — only model supporting non-Latin scripts"
        ],
        "answer": 1,
        "explanation": "snowflake-arctic-embed-m-v1.5 (default) is English-only. snowflake-arctic-embed-l-v2.0 is multilingual with 1024 dimensions, supporting both English and non-English datasets.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A developer uses snowflake-arctic-embed-l-v2.0-8k (8,192 token context) for Cortex Search. Documents average 2,000 tokens. What chunk size does Snowflake recommend?",
        "options": [
            "Use the full 8,192-token window for maximum context",
            "Split into chunks of no more than 512 tokens for best search results",
            "Use 2,000-token chunks since documents fit within the window",
            "Use 4,096-token chunks as a middle ground"
        ],
        "answer": 1,
        "explanation": "Snowflake recommends 512-token chunks even with longer-context models. Research shows smaller chunks yield higher retrieval and downstream LLM response quality.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In CREATE CORTEX SEARCH SERVICE, what does the ON clause specify versus the ATTRIBUTES clause?",
        "options": [
            "ON = primary key column; ATTRIBUTES = search columns",
            "ON = column to be searched; ATTRIBUTES = columns available as filter columns",
            "ON = embedding model; ATTRIBUTES = columns to embed",
            "ON = target lag; ATTRIBUTES = warehouse size"
        ],
        "answer": 1,
        "explanation": "ON specifies the search column that queries will match against. ATTRIBUTES specifies columns that can be used as filter columns when querying.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A Cortex Search Service needs precise lexical matching on product SKUs AND semantic matching on descriptions. Which feature should be used?",
        "options": [
            "Create two separate services and query independently",
            "Use multi-index Cortex Search with text indexes for SKUs and vector indexes for descriptions",
            "Concatenate SKUs and descriptions into a single ON column",
            "Set HYBRID_MODE = TRUE on the service"
        ],
        "answer": 1,
        "explanation": "Multi-index Cortex Search supports multiple index types. Text indexes handle lexical matching (SKUs, codes), while vector indexes handle semantic matching (descriptions, reviews).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A Cortex Search Service source query includes UNION ALL and creation fails. What is the most likely cause?",
        "options": [
            "UNION ALL is not valid SQL",
            "The source query must support dynamic table incremental refresh",
            "Cortex Search only supports single-table source queries",
            "Total row count exceeds the 1 billion row limit"
        ],
        "answer": 1,
        "explanation": "Cortex Search source queries must be candidates for dynamic table incremental refresh. This restriction prevents runaway embedding costs. Not all SQL constructs support incremental refresh.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A product catalog has 150 million rows. What happens when creating a Cortex Search Service over it?",
        "options": [
            "The service creates successfully — no row limit exists",
            "Creation fails because it exceeds the 100 million row limit",
            "The service creates but queries are throttled",
            "The service auto-partitions data into sub-100M shards"
        ],
        "answer": 1,
        "explanation": "Cortex Search materialized query results must be < 100M rows. Exceeding this causes creation to fail. Contact Snowflake to increase the limit.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In Snowflake AI Observability, what are applications represented as?",
        "options": [
            "CORTEX SERVICE objects",
            "EXTERNAL AGENT objects",
            "MONITORING PIPELINE objects",
            "AI APPLICATION objects in the Model Registry"
        ],
        "answer": 1,
        "explanation": "Applications are represented as EXTERNAL AGENT objects in Snowflake. These store application and evaluation metadata (not the code itself).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "Which Python packages are required for AI Observability with Cortex?",
        "options": [
            "trulens-core, trulens-connectors-snowflake, trulens-providers-cortex (>= 2.1.2)",
            "snowflake-ml-python, snowflake-telemetry, snowflake-observability",
            "mlflow, opentelemetry-sdk, snowflake-connector-python",
            "langchain, ragas, snowflake-cortex-observability"
        ],
        "answer": 0,
        "explanation": "AI Observability requires trulens-core, trulens-connectors-snowflake, and trulens-providers-cortex (version >= 2.1.2).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "In AI Observability, a 'run' consists of two stages. What are they?",
        "options": [
            "Training stage and inference stage",
            "Invocation stage (generate output) and computation stage (compute metrics)",
            "Collection stage and aggregation stage",
            "Execution stage and evaluation stage"
        ],
        "answer": 1,
        "explanation": "AI Observability runs have an invocation stage (application generates output and traces) and a computation stage (evaluation metrics are computed).",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "AI Observability uses which technique for evaluating AI application output quality?",
        "options": [
            "Human-in-the-loop evaluation",
            "Statistical hypothesis testing on output distributions",
            "LLM-as-judge technique",
            "Ground truth comparison using labeled datasets"
        ],
        "answer": 2,
        "explanation": "AI Observability uses the LLM-as-judge technique — LLMs (via COMPLETE function calls) evaluate the quality of outputs rather than requiring human annotations.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 2: Gen AI & LLM Functions",
        "question": "A data pipeline calls COMPLETE() on 50,000 rows but occasionally some rows have malformed input that causes errors, breaking the query. Which function should be used?",
        "options": [
            "AI_COMPLETE with error_handling = 'skip'",
            "TRY_COMPLETE, which returns NULL on failure instead of throwing an error",
            "COMPLETE with TRY_CAST on the input",
            "COMPLETE wrapped in a TRY...CATCH block"
        ],
        "answer": 1,
        "explanation": "TRY_COMPLETE returns NULL on failure instead of raising an error, preventing individual row failures from breaking batch queries. No cost is incurred for NULL returns.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "A team processed 500 Cortex Analyst messages today: 480 returned HTTP 200 and 20 returned errors. How many messages are billed?",
        "options": [
            "500 — all API calls are billable regardless of status",
            "480 — only successful responses (HTTP 200) are counted",
            "Based on total tokens across all 500 messages",
            "480 plus a reduced rate for the 20 error responses"
        ],
        "answer": 1,
        "explanation": "Cortex Analyst billing is per-message, and only successful responses (HTTP 200) count. Token count does not affect cost unless invoked via Cortex Agents.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "When Cortex Analyst is invoked through Cortex Agents rather than directly, how does billing change?",
        "options": [
            "Billing remains per-message regardless of invocation method",
            "Billing changes to per-token when invoked via Cortex Agents",
            "There is no additional Analyst charge when used through Agents",
            "Billing switches to per-query based on SQL complexity"
        ],
        "answer": 1,
        "explanation": "Directly, Cortex Analyst bills per-message. When invoked via Cortex Agents, the number of tokens affects cost as part of the agent orchestration cost model.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which is the most complete list of Cortex Search Service cost components?",
        "options": [
            "Warehouse compute and EMBED_TEXT token costs only",
            "Warehouse compute, EMBED_TEXT tokens, serving compute (per GB/mo), storage, and cloud services",
            "Serving compute and storage only — warehouse is not used after creation",
            "A flat per-query fee plus storage costs"
        ],
        "answer": 1,
        "explanation": "Cortex Search has 5 cost components: warehouse compute (for refreshes), EMBED_TEXT tokens (for embeddings), serving (per GB/mo indexed data), storage, and cloud services.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "A team's Cortex Search Service is only needed during business hours. How can they reduce off-hours costs?",
        "options": [
            "Drop and recreate the service each morning",
            "Suspend the service to stop serving costs while suspended",
            "Set TARGET_LAG to '999 days' during off-hours",
            "Serving costs cannot be reduced — they are fixed based on indexed data"
        ],
        "answer": 1,
        "explanation": "Cortex Search Services can be suspended using ALTER CORTEX SEARCH SERVICE ... SUSPEND, which stops serving costs. The service can be resumed when needed.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which view should be queried to monitor Cortex Analyst credit consumption?",
        "options": [
            "CORTEX_FUNCTIONS_USAGE_HISTORY",
            "CORTEX_ANALYST_USAGE_HISTORY",
            "METERING_DAILY_HISTORY with SERVICE_TYPE = 'CORTEX_ANALYST'",
            "CORTEX_SEARCH_DAILY_USAGE_HISTORY"
        ],
        "answer": 1,
        "explanation": "CORTEX_ANALYST_USAGE_HISTORY in SNOWFLAKE.ACCOUNT_USAGE is specifically for monitoring Cortex Analyst credit consumption.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "An admin sees both CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY and CORTEX_FUNCTIONS_USAGE_HISTORY views. What is the relationship?",
        "options": [
            "QUERY_USAGE tracks per-query costs; USAGE tracks per-function costs",
            "They log essentially the same events; monitoring both is unnecessary",
            "QUERY_USAGE is for REST API calls only; USAGE is for SQL calls only",
            "USAGE is a summary aggregated from QUERY_USAGE"
        ],
        "answer": 1,
        "explanation": "Per the documentation, these two views log essentially the same events. It is not necessary to monitor both.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "An admin revokes CORTEX_USER from PUBLIC. A user with ACCOUNTADMIN tries to use AI_COMPLETE. What happens?",
        "options": [
            "The call fails because CORTEX_USER has been revoked from PUBLIC",
            "ACCOUNTADMIN can still use AI_COMPLETE — it always has complete access to all features",
            "ACCOUNTADMIN must explicitly re-grant CORTEX_USER to themselves first",
            "ACCOUNTADMIN can only use AI_COMPLETE through the REST API, not SQL"
        ],
        "answer": 1,
        "explanation": "ACCOUNTADMIN always has complete access to all Snowflake features including AI features. Revoking CORTEX_USER from PUBLIC does not affect ACCOUNTADMIN.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "ENABLE_CORTEX_ANALYST = FALSE is set. An ACCOUNTADMIN user tries to call the Cortex Analyst API. What happens?",
        "options": [
            "The call succeeds because ACCOUNTADMIN overrides all parameters",
            "The call fails — this parameter prevents even ACCOUNTADMIN from using Analyst",
            "The call succeeds but returns a warning about the disabled parameter",
            "The call fails unless the user also has CORTEX_ANALYST_USER"
        ],
        "answer": 1,
        "explanation": "ENABLE_CORTEX_ANALYST = FALSE blocks Cortex Analyst for everyone, including ACCOUNTADMIN. However, ACCOUNTADMIN can always set it back to TRUE.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "To allow a role to create fine-tuned models using Cortex Fine-tuning, which privilege is needed?",
        "options": [
            "SNOWFLAKE.CORTEX_FINETUNE_USER database role",
            "CREATE MODEL privilege on the target schema",
            "CORTEX_USER database role plus TRAIN MODEL on the account",
            "CREATE CORTEX FINE_TUNE SERVICE privilege"
        ],
        "answer": 1,
        "explanation": "Cortex Fine-tuning is controlled by the CREATE MODEL privilege on the schema, not a database role. Revoke CREATE MODEL to prevent fine-tuning.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "After revoking CORTEX_USER from PUBLIC, an admin wants roles to only use embedding functions and create Cortex Search Services. Which database role should be granted?",
        "options": [
            "SNOWFLAKE.CORTEX_USER (re-grant selectively)",
            "SNOWFLAKE.CORTEX_EMBED_USER",
            "SNOWFLAKE.CORTEX_SEARCH_USER",
            "SNOWFLAKE.CORTEX_ANALYST_USER"
        ],
        "answer": 1,
        "explanation": "CORTEX_EMBED_USER provides privileges for embedding functions (AI_EMBED, EMBED_TEXT_768/1024) and creating Cortex Search Services with managed embeddings, without other Cortex AI features.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Which statement about the SNOWFLAKE.COPILOT_USER database role is correct?",
        "options": [
            "COPILOT_USER is the same role as CORTEX_USER — they are aliases",
            "COPILOT_USER is a separate role from CORTEX_USER and is also granted to PUBLIC by default",
            "COPILOT_USER must be explicitly granted by ACCOUNTADMIN before use",
            "COPILOT_USER is deprecated and replaced by CORTEX_USER"
        ],
        "answer": 1,
        "explanation": "COPILOT_USER is a separate database role from CORTEX_USER. Both are granted to PUBLIC by default. To revoke Copilot access, you must revoke COPILOT_USER independently.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/opting-out"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "Cross-region inference: a request originates from us-east-2 and is processed in us-west-2. In which region are credits consumed?",
        "options": [
            "Processing region (us-west-2)",
            "Requesting region (us-east-2)",
            "Split 50/50 between both regions",
            "Both — origination fee plus processing fee"
        ],
        "answer": 1,
        "explanation": "Credits are consumed in the requesting region, not the processing region. There are no data egress charges for cross-region inference.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "What are the cost components of AI Observability when using TruLens with Cortex?",
        "options": [
            "A flat per-evaluation fee based on number of runs",
            "COMPLETE function calls for LLM judges, warehouse compute, and storage for traces/metrics",
            "Only warehouse compute for running the evaluation pipeline",
            "Per-token charges for observability models plus storage"
        ],
        "answer": 1,
        "explanation": "AI Observability pricing includes COMPLETE function calls for LLM-as-judge evaluations (token-based), warehouse compute for evaluations, and storage for traces and metrics.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability"
    },
    {
        "domain": "Domain 3: Gen AI Governance",
        "question": "A Cortex Agent uses Cortex Analyst, a Cortex Search Service, and a custom UDF. Which cost components apply?",
        "options": [
            "Only orchestration token costs — tool costs are included in the agent fee",
            "Orchestration tokens + Analyst per-token + Search index/serving + warehouse for custom UDF",
            "A flat per-agent-call fee covering all tools",
            "Orchestration tokens + Analyst per-message + Search query costs only"
        ],
        "answer": 1,
        "explanation": "Cortex Agents incur orchestration tokens cost, plus each tool's own costs: Analyst per-token (when via Agents), Search index/serving, and warehouse for custom tool (UDF/SP) execution.",
        "doc_url": "https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents"
    },
]

TOTAL_QUESTIONS = len(QUESTIONS)

def init_state():
    st.session_state.setdefault("quiz_started", False)
    st.session_state.setdefault("current_index", 0)
    st.session_state.setdefault("score", 0)
    st.session_state.setdefault("answered", 0)
    st.session_state.setdefault("submitted", False)
    st.session_state.setdefault("selected_option", None)
    st.session_state.setdefault("shuffled_questions", [])
    st.session_state.setdefault("quiz_complete", False)
    st.session_state.setdefault("answers_log", [])

def start_quiz():
    questions = QUESTIONS.copy()
    random.shuffle(questions)
    st.session_state.shuffled_questions = questions
    st.session_state.quiz_started = True
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answered = 0
    st.session_state.submitted = False
    st.session_state.selected_option = None
    st.session_state.quiz_complete = False
    st.session_state.answers_log = []

def submit_answer():
    st.session_state.submitted = True
    q = st.session_state.shuffled_questions[st.session_state.current_index]
    selected = st.session_state.selected_option
    if selected is not None and selected == q["answer"]:
        st.session_state.score += 1
        st.session_state.answers_log.append(True)
    else:
        st.session_state.answers_log.append(False)
    st.session_state.answered += 1

def next_question():
    st.session_state.current_index += 1
    st.session_state.submitted = False
    st.session_state.selected_option = None
    if st.session_state.current_index >= TOTAL_QUESTIONS:
        st.session_state.quiz_complete = True

init_state()

st.title("SnowPro Gen AI exam prep")
st.caption(f"GES-C01 | {TOTAL_QUESTIONS} questions | Domains weighted by exam distribution")

if not st.session_state.quiz_started:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Domain 1", "30%", help="Gen AI Overview")
    with col2:
        st.metric("Domain 2", "44%", help="Gen AI & LLM Functions")
    with col3:
        st.metric("Domain 3", "26%", help="Gen AI Governance")

    st.write("")

    d1 = sum(1 for q in QUESTIONS if "Domain 1" in q["domain"])
    d2 = sum(1 for q in QUESTIONS if "Domain 2" in q["domain"])
    d3 = sum(1 for q in QUESTIONS if "Domain 3" in q["domain"])
    st.caption(f"Question distribution: Domain 1 ({d1}), Domain 2 ({d2}), Domain 3 ({d3})")

    st.write("")
    st.button("Start quiz", on_click=start_quiz, type="primary", icon=":material/play_arrow:")

elif st.session_state.quiz_complete:
    pct = (st.session_state.score / TOTAL_QUESTIONS) * 100
    passed = pct >= 70

    if passed:
        st.success(f"Score: {st.session_state.score}/{TOTAL_QUESTIONS} ({pct:.0f}%) — Pass", icon=":material/check_circle:")
    else:
        st.error(f"Score: {st.session_state.score}/{TOTAL_QUESTIONS} ({pct:.0f}%) — Needs improvement", icon=":material/error:")

    st.caption("70% is typically the passing threshold for SnowPro exams.")
    st.write("")

    d1_correct = sum(1 for i, q in enumerate(st.session_state.shuffled_questions) if "Domain 1" in q["domain"] and i < len(st.session_state.answers_log) and st.session_state.answers_log[i])
    d1_total = sum(1 for q in st.session_state.shuffled_questions if "Domain 1" in q["domain"])
    d2_correct = sum(1 for i, q in enumerate(st.session_state.shuffled_questions) if "Domain 2" in q["domain"] and i < len(st.session_state.answers_log) and st.session_state.answers_log[i])
    d2_total = sum(1 for q in st.session_state.shuffled_questions if "Domain 2" in q["domain"])
    d3_correct = sum(1 for i, q in enumerate(st.session_state.shuffled_questions) if "Domain 3" in q["domain"] and i < len(st.session_state.answers_log) and st.session_state.answers_log[i])
    d3_total = sum(1 for q in st.session_state.shuffled_questions if "Domain 3" in q["domain"])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Domain 1", f"{d1_correct}/{d1_total}")
    with col2:
        st.metric("Domain 2", f"{d2_correct}/{d2_total}")
    with col3:
        st.metric("Domain 3", f"{d3_correct}/{d3_total}")

    st.write("")
    st.button("Restart quiz", on_click=start_quiz, type="primary", icon=":material/refresh:")

else:
    q = st.session_state.shuffled_questions[st.session_state.current_index]
    idx = st.session_state.current_index

    progress = (idx + 1) / TOTAL_QUESTIONS
    st.progress(progress, text=f"Question {idx + 1} of {TOTAL_QUESTIONS}")

    col_score, col_domain = st.columns([1, 2])
    with col_score:
        st.caption(f"Score: {st.session_state.score}/{st.session_state.answered}")
    with col_domain:
        st.badge(q["domain"], icon=":material/category:")

    st.subheader(q["question"])

    if not st.session_state.submitted:
        for i, opt in enumerate(q["options"]):
            label = f"{chr(65 + i)}. {opt}"
            if st.button(label, key=f"opt_{idx}_{i}", use_container_width=True):
                st.session_state.selected_option = i
                st.rerun()

        if st.session_state.selected_option is not None:
            st.caption(f"Selected: {chr(65 + st.session_state.selected_option)}. {q['options'][st.session_state.selected_option]}")
            st.button("Submit answer", on_click=submit_answer, type="primary", icon=":material/check:")
    else:
        selected = st.session_state.selected_option
        correct = q["answer"]

        for i, opt in enumerate(q["options"]):
            prefix = chr(65 + i)
            if i == correct and i == selected:
                st.success(f"{prefix}. {opt}", icon=":material/check_circle:")
            elif i == correct:
                st.success(f"{prefix}. {opt}", icon=":material/check_circle:")
            elif i == selected:
                st.error(f"{prefix}. {opt}", icon=":material/cancel:")
            else:
                st.write(f"{prefix}. {opt}")

        if selected == correct:
            st.info(q["explanation"], icon=":material/lightbulb:")
        else:
            st.warning(q["explanation"], icon=":material/lightbulb:")
            st.markdown(f":material/link: [Study this topic]({q['doc_url']})")

        if idx + 1 < TOTAL_QUESTIONS:
            st.button("Next question", on_click=next_question, type="primary", icon=":material/arrow_forward:")
        else:
            st.button("See results", on_click=next_question, type="primary", icon=":material/flag:")
