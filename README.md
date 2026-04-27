# Legislative Polarization Knowledge Extraction Graphs

This project builds a small data pipeline for legislative voting analysis.

In short, it:

1. Downloads public CSV datasets from the Brazilian Chamber of Deputies (deputies, themes, votes, and vote objects).
2. Loads them into a DuckDB database.
3. Provides a Jupyter notebook to run SQL queries and build vote graphs with NetworkX.

In case you only want to access the used dataset, it is available on [Mendeley Data](https://data.mendeley.com/datasets/5yv2v3ppzj/1).

## Quick Run (Docker)

### 1. Configure environment

```bash
cp .env.example .env
```

### 2. Build images

```bash
docker compose build
```

### 3. Generate raw files + DuckDB tables

```bash
docker compose run --rm database
```

### 4. Start notebook service

```bash
docker compose up analysis
```

Open <http://localhost:8888> and run [analysis/notebooks/analysis.ipynb](analysis/notebooks/analysis.ipynb).

### 5. Stop services

```bash
docker compose down
```

## Main Outputs

- Database: [data/legislative.duckdb](data/legislative.duckdb)
- Raw CSV files: [data/raw](data/raw)
- Notebook: [analysis/notebooks/analysis.ipynb](analysis/notebooks/analysis.ipynb)
- SQL queries: [analysis/queries](analysis/queries)
- Exported graphs: [analysis/graphs](analysis/graphs)
