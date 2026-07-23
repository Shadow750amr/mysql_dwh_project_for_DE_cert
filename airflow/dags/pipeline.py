from airflow.decorators import dag,task
import datetime

@dag(
    dag_id='process_web_log',
    schedule_interval='@daily',
    start_date=datetime.date(2026, 7, 22),
    catchup=False
)
def my_pipeline():

    @task()
    def extract_data():
        with open('/airflow/dags/acceslog.txt','r') as file:
            file.read()


    @task()
    def transform_data(extracted_data: dict):
        # Data flows automatically from extract() via XComs
        return [x * 2 for x in extracted_data["data"]]

    @task()
    def load_data(transformed_data: list):
        print(f"Loading data: {transformed_data}")

    # Set dependencies by calling functions directly
    extracted = extract()
    transformed = transform(extracted)
    load(transformed)

# Instantiate the DAG
my_dag = my_pipeline()