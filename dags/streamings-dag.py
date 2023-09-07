from datetime import timedelta, datetime
import os
from airflow import DAG

from airflow.operators.bash_operator import BashOperator


DAGS_DIR = os.path.dirname(__file__)
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 6),
    'email': ['danielbcuadros@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False
}

dag = DAG(
    'streamings-dag',
    default_args=default_args,
    schedule_interval='30 20 * * *',
    description='Twitter ETL about Streamings Platforms',
    catchup = False,
    tags=['streaming-insights']
)

twitter_crawler = BashOperator(
    dag=dag,
    task_id='twitter_crawler',
    retry_delay=timedelta(minutes=35),
    retries=2,
    bash_command=' '.join([ 
        os.path.join(DAGS_DIR, "../../Streaming-insights/venv/bin/python"),
        os.path.join(DAGS_DIR, '../../Streaming-insights/etls/twitter-crawler.py')
    ]),
)

data_management = BashOperator(
    dag=dag,
    task_id='data_management',
    retry_delay=timedelta(seconds=30),
    retries=2,
    bash_command=' '.join([ 
        os.path.join(DAGS_DIR, "../../Streaming-insights/venv/bin/python"),
        os.path.join(DAGS_DIR, '../../Streaming-insights/etls/data-management.py')
    ]),
)


twitter_crawler >> data_management