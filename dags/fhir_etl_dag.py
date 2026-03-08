from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_fhir_data():
    """Extract FHIR JSON bundles from source system."""
    import shutil
    shutil.copy("data/sample_fhir.json", "/tmp/fhir.json")
    print("Extracted sample FHIR data to /tmp/fhir.json")

def transform_to_csv():
    """Transform FHIR JSON into normalized CSV format."""
    pass

def load_to_s3():
    """Load transformed CSV files into AWS S3."""
    pass

def run_data_quality_checks():
    """Run data quality validation on ingested data."""
    pass

with DAG(
    dag_id="fhir_etl_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    extract = PythonOperator(task_id="extract", python_callable=extract_fhir_data)
    transform = PythonOperator(task_id="transform", python_callable=transform_to_csv)
    load = PythonOperator(task_id="load", python_callable=load_to_s3)
    dq = PythonOperator(task_id="dq", python_callable=run_data_quality_checks)

    extract >> transform >> load >> dq
