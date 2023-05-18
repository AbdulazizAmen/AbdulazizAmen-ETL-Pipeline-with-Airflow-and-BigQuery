from datetime import timedelta, datetime

from airflow import DAG 
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator


GOOGLE_CONN_ID = "google_cloud_default"
PROJECT_ID="gcp-project-386421"
GS_PATH = "recipe/"
BUCKET_NAME = 'abdulaziz_recipefinal'
STAGING_DATASET = "recipe_staging_dataset"
DATASET = "recipe_dataset"
LOCATION = "us-east1"


default_args = {
    'owner': 'Abdulaziz Amen',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'start_date':  days_ago(2),
    'retry_delay': timedelta(minutes=5),
}


with DAG('RecipeeWarehouse', schedule_interval=timedelta(days=1), default_args=default_args) as dag:
    start_pipeline = DummyOperator(
        task_id = 'start_pipeline',
        dag = dag
        )

    load_staging_dataset = DummyOperator(
        task_id = 'load_staging_dataset',
        dag = dag
        )    
    
       
    load_dataset_ayam = GCSToBigQueryOperator(
        task_id = 'load_dataset_ayam',
        bucket = BUCKET_NAME,
        source_objects = ['recipe/ayam.csv'],
        destination_project_dataset_table = f'{PROJECT_ID}:{STAGING_DATASET}.dataset_ayam',
        write_disposition='WRITE_TRUNCATE',
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
        {'name': 'Title', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'Ingredients', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Steps', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Loves', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'URL', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        )

    load_dataset_ikan = GCSToBigQueryOperator(
        task_id = 'load_dataset_ikan',
        bucket = BUCKET_NAME,
        source_objects = ['recipe/ikan.csv'],
        destination_project_dataset_table = f'{PROJECT_ID}:{STAGING_DATASET}.dataset_ikan',
        write_disposition='WRITE_TRUNCATE',
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
        {'name': 'Title', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'Ingredients', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Steps', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Loves', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'URL', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        )

    load_dataset_tahu = GCSToBigQueryOperator(
        task_id = 'load_dataset_tahu',
        bucket = BUCKET_NAME,
        source_objects = ['recipe/tahu.csv'],
        destination_project_dataset_table = f'{PROJECT_ID}:{STAGING_DATASET}.dataset_tahu',
        write_disposition='WRITE_TRUNCATE',
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
        {'name': 'Title', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'Ingredients', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Steps', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Loves', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'URL', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        )
    
    load_dataset_telur = GCSToBigQueryOperator(
        task_id = 'load_dataset_telur',
        bucket = BUCKET_NAME,
        source_objects = ['recipe/telur.csv'],
        destination_project_dataset_table = f'{PROJECT_ID}:{STAGING_DATASET}.dataset_telur',
        write_disposition='WRITE_TRUNCATE',
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
        {'name': 'Title', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'Ingredients', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Steps', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Loves', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'URL', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        )   

    load_dataset_tempe = GCSToBigQueryOperator(
        task_id = 'load_dataset_tempe',
        bucket = BUCKET_NAME,
        source_objects = ['recipe/tempe.csv'],
        destination_project_dataset_table = f'{PROJECT_ID}:{STAGING_DATASET}.dataset_tempe',
        write_disposition='WRITE_TRUNCATE',
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
        {'name': 'Title', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'Ingredients', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Steps', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Loves', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'URL', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        )

    load_dataset_udang = GCSToBigQueryOperator(
        task_id = 'load_dataset_udang',
        bucket = BUCKET_NAME,
        source_objects = ['recipe/udang.csv'],
        destination_project_dataset_table = f'{PROJECT_ID}:{STAGING_DATASET}.dataset_udang',
        write_disposition='WRITE_TRUNCATE',
        source_format = 'csv',
        allow_quoted_newlines = 'true',
        skip_leading_rows = 1,
        schema_fields=[
        {'name': 'Title', 'type': 'STRING', 'mode': 'REQUIRED'},
        {'name': 'Ingredients', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Steps', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'Loves', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'URL', 'type': 'STRING', 'mode': 'NULLABLE'},
            ]
        )
    
    check_dataset_ayam = BigQueryCheckOperator(
        task_id = 'check_dataset_ayam',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{STAGING_DATASET}.dataset_ayam`'
        )

    check_dataset_ikan = BigQueryCheckOperator(
        task_id = 'check_dataset_ikan',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{STAGING_DATASET}.dataset_ikan`'
        )

    check_dataset_tahu = BigQueryCheckOperator(
        task_id = 'check_dataset_tahu',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{STAGING_DATASET}.dataset_tahu`'
        ) 

    check_dataset_telur = BigQueryCheckOperator(
        task_id = 'check_dataset_telur',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{STAGING_DATASET}.dataset_telur`'
        )

    check_dataset_tempe = BigQueryCheckOperator(
        task_id = 'check_dataset_tempe',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{STAGING_DATASET}.dataset_tempe`'
        )               

    check_dataset_udang = BigQueryCheckOperator(
        task_id = 'check_dataset_udang',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{STAGING_DATASET}.dataset_udang`'
        ) 

    create_D_Table = DummyOperator(
        task_id = 'Create_D_Table',
        dag = dag
        )

    create_D_dataset_ayam = BigQueryOperator(
        task_id = 'create_D_dataset_ayam',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/D_dataset_ayam.sql'
        )

    create_D_dataset_ikan = BigQueryOperator(
        task_id = 'create_D_dataset_ikan',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/D_dataset_ikan.sql'
        )   

    create_D_dataset_tahu = BigQueryOperator(
        task_id = 'create_D_dataset_tahu',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/D_dataset_tahu.sql'
        )

    create_D_dataset_telur = BigQueryOperator(
        task_id = 'create_D_dataset_telur',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/D_dataset_telur.sql'
        )

    create_D_dataset_tempe = BigQueryOperator(
        task_id = 'create_D_dataset_tempe',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/D_dataset_tempe.sql'
        )         

    create_D_dataset_udang = BigQueryOperator(
        task_id = 'create_D_dataset_udang',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/D_dataset_udang.sql'
        )

    create_F_dataset_recipe = BigQueryOperator(
        task_id = 'create_F_dataset_recipe',
        use_legacy_sql = False,
        location = LOCATION,
        sql = './SQL/F_dataset_recipe.sql'
        )

    check_F_dataset_recipe = BigQueryCheckOperator(
        task_id = 'check_F_dataset_recipe',
        use_legacy_sql=False,
        location = LOCATION,
        sql = f'SELECT count(*) FROM `{PROJECT_ID}.{DATASET}.F_dataset_recipe`'
        ) 

    finish_pipeline = DummyOperator(
        task_id = 'finish_pipeline',
        dag = dag
        ) 
start_pipeline >> load_staging_dataset

load_staging_dataset >> [load_dataset_ayam, load_dataset_ikan, load_dataset_tahu, load_dataset_telur, load_dataset_tempe, load_dataset_udang]

load_dataset_ayam >> check_dataset_ayam
load_dataset_ikan >> check_dataset_ikan
load_dataset_tahu >> check_dataset_tahu
load_dataset_telur >> check_dataset_telur
load_dataset_tempe >> check_dataset_tempe
load_dataset_udang >> check_dataset_udang

[check_dataset_ayam, check_dataset_ikan, check_dataset_tahu, check_dataset_telur, check_dataset_tempe, check_dataset_udang] >> create_D_Table

create_D_Table >> [create_D_dataset_ayam, create_D_dataset_ikan, create_D_dataset_tahu, create_D_dataset_telur, create_D_dataset_tempe, create_D_dataset_udang]

[create_D_dataset_ayam, create_D_dataset_ikan, create_D_dataset_tahu, create_D_dataset_telur, create_D_dataset_tempe, create_D_dataset_udang] >> create_F_dataset_recipe

create_F_dataset_recipe >> check_F_dataset_recipe >> finish_pipeline