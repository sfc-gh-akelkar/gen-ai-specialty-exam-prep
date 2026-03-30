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

## Quick Start

```bash
pip install -r requirements.txt
streamlit run snowpro_genai_quiz.py
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
