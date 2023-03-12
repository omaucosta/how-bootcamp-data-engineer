import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
}

dag = DAG(
    dar_id='dag_datas_sandbox',
    default_args=args,
    schedule_interval='@daily',
    dagrun_timeout=timedelta(minutes=60)
)

t1 = BashOperator(
    task_id='task_datas_sandbox',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep_10s',
    bash_command='sleep 10',
    retires=3,
    dag=dag
)

t3 = BashOperator(
    task_id='saida',
    bash_command='date >/opt/airflow/logs/date_output.txt',
    retires=3,
    dag=dag
)

t1 >> t2 >> t3