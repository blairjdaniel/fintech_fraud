# filepath: ~/airflow/dags/crypto_etl_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'crypto_etl',
    default_args=default_args,
    description='Run ETL script for crypto data ingestion',
    schedule_interval='@daily',  # Run every day
    start_date=datetime(2025, 4, 29),
    catchup=False,
)

# Define the Python function to run the ETL script
def run_etl():
    subprocess.run(["/Users/blairjdaniel/fintech_fraud/scripts/crypto_etl_dag.py", "/Users/blairjdaniel/fintech_fraud/scripts/load_data.py"])

# Define the task
etl_task = PythonOperator(
    task_id='run_crypto_etl',
    python_callable=run_etl,
    dag=dag,
)