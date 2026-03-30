# SnowPro Specialty: Gen AI Certification Exam Prep (GES-C01)

Interactive Streamlit quiz app with **132 scenario-based questions** mapped to live Snowflake documentation for the SnowPro Specialty: Generative AI certification exam.

## Exam Domains (post March 1, 2026)

| Domain | Weight | Questions |
|--------|--------|-----------|
| Domain 1: Snowflake for Gen AI Overview | 30% | 39 |
| Domain 2: Snowflake Gen AI & LLM Functions | 44% | 56 |
| Domain 3: Snowflake Gen AI Governance | 26% | 37 |

## Features

- 132 doc-grounded, scenario-based questions
- Randomized question order each attempt
- Instant feedback with explanations and doc links
- Domain-by-domain score breakdown
- Progress tracking during quiz

## Deploy to Snowflake (Streamlit in Snowflake)

### Prerequisites

- [Snowflake CLI](https://docs.snowflake.com/en/developer-guide/snowflake-cli/index) v3.14.0+
- A Snowflake account with a configured CLI connection
- A compute pool (CPU, any size) with USAGE granted to your role
- CREATE STREAMLIT privilege on the target schema

### Step 1: Clone the repo

```bash
git clone https://github.com/sfc-gh-akelkar/gen-ai-specialty-exam-prep.git
cd gen-ai-specialty-exam-prep
```

### Step 2: Edit `snowflake.yml`

Update the values to match your account:

```yaml
definition_version: 2
entities:
  snowpro_genai_quiz:
    type: streamlit
    identifier:
      name: SNOWPRO_GENAI_QUIZ
      database: <YOUR_DATABASE>       # e.g. SANDBOX
      schema: <YOUR_SCHEMA>           # e.g. PUBLIC
    query_warehouse: <YOUR_WAREHOUSE> # e.g. COMPUTE_WH
    runtime_name: SYSTEM$ST_CONTAINER_RUNTIME_PY3_11
    compute_pool: <YOUR_COMPUTE_POOL> # e.g. XS_COMPUTE_POOL
    main_file: streamlit_app.py
    artifacts:
      - streamlit_app.py
      - pyproject.toml
```

**Finding your values:**

```sql
-- List compute pools you have access to
SHOW COMPUTE POOLS;

-- If you need to create one (requires SYSADMIN or equivalent)
CREATE COMPUTE POOL MY_STREAMLIT_POOL
  MIN_NODES = 1
  MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_XS
  AUTO_SUSPEND_SECS = 300
  AUTO_RESUME = TRUE;

GRANT USAGE ON COMPUTE POOL MY_STREAMLIT_POOL TO ROLE <YOUR_ROLE>;
```

### Step 3: Deploy

```bash
snow streamlit deploy --replace --connection <YOUR_CONNECTION>
```

The CLI will print the Snowsight URL when complete. You can also find it under **Projects > Streamlit** in Snowsight.

### Step 4: Share with others

Once deployed, grant access to teammates:

```sql
GRANT USAGE ON DATABASE <YOUR_DATABASE> TO ROLE <TEAM_ROLE>;
GRANT USAGE ON SCHEMA <YOUR_DATABASE>.<YOUR_SCHEMA> TO ROLE <TEAM_ROLE>;
GRANT USAGE ON WAREHOUSE <YOUR_WAREHOUSE> TO ROLE <TEAM_ROLE>;
GRANT USAGE ON STREAMLIT <YOUR_DATABASE>.<YOUR_SCHEMA>.SNOWPRO_GENAI_QUIZ TO ROLE <TEAM_ROLE>;
```

## Run Locally (optional)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Question Sources

Questions are grounded in official Snowflake documentation covering:

- Cortex AI SQL Functions (COMPLETE, CLASSIFY_TEXT, SENTIMENT, etc.)
- Cortex Search (hybrid search, embedding models, costs)
- Cortex Analyst (semantic views, model selection, multi-turn)
- Cortex Agents (tools, threads, web search, orchestration)
- RBAC & Database Roles (CORTEX_USER, CORTEX_ANALYST_USER, etc.)
- Cross-Region Inference
- AI Observability & TruLens
- Cortex Guard & Governance
- Cost Monitoring & Usage Views
- Fine-tuning, Model Registry, SPCS

## Disclaimer

This is an unofficial study tool. Questions are based on publicly available Snowflake documentation and community resources. Always refer to the [official exam guide](https://learn.snowflake.com/en/certifications/snowpro-specialty-genai/) for the most current exam objectives.
