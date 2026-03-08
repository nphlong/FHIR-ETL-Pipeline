# Usage Guide

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Airflow with Docker:

```bash
docker-compose up
```

3. Trigger the DAG `fhir_etl_dag.py` from the Airflow UI.

4. Check data quality reports in `dq_checker/reports/`.

5. Connect BI tools to the warehouse for dashboards.