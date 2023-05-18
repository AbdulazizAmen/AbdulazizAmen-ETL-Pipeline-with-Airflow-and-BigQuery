## ETL-Pipeline-with-Airflow-and-BigQuery
The pipeline is built using Apache Airflow and Google Cloud Platform, and includes data validation and transformation steps to ensure data quality, as well as SQL statements to transform the data into a format suitable for analysis and reporting.


## Code Description
This python code involves the use of Airflow operators to load a CSV file into a BigQuery table, check the number of rows in the table, and execute a SQL script to create another dataset in BigQuery. Here is a breakdown of each of the operators:

* __GCSToBigQueryOperator__

This operator loads a CSV file from a Google Cloud Storage (GCS) bucket into a BigQuery table. The operator has several parameters including the task ID, the GCS bucket name, the source CSV file path, the destination BigQuery table, the write disposition, source format, and schema fields.

* __BigQueryCheckOperator__

This operator checks the number of rows in the previously loaded BigQuery table. The operator has several parameters including the task ID, the SQL statement to execute, and whether to use legacy SQL.

* __BigQueryOperator__

This operator executes a SQL script to create a new dataset in BigQuery. The operator has several parameters including the task ID, the SQL script file path, and whether to use legacy SQL.

In summary, this code loads a CSV file into a BigQuery table, checks the number of rows in the table, and executes a SQL script to create a new dataset in BigQuery.
