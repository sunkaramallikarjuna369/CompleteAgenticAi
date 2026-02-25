# Data Processing Pipelines

## ETL Process
- **Extract**: Collect from databases, APIs, files
- **Transform**: Clean, validate, normalize
- **Load**: Store in target system (warehouse, vector DB)

## Data Cleaning
| Issue | Solution |
|-------|----------|
| Missing values | Imputation, deletion |
| Duplicates | Fuzzy matching dedup |
| Outliers | IQR/Z-score detection |
| Noisy text | Normalization |

## Data Validation
- Schema validation, range checks, drift detection
- Tools: Great Expectations, Pandera, Pydantic

## For Agentic AI
- RAG knowledge bases need clean data
- Agent training data requires careful curation
- Data quality directly impacts agent reliability