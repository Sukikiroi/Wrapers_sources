import csv
import pandas as pd
import psycopg2
from datetime import datetime


def infer_data_type(value):
    try:
        # Try to parse the value as a timestamp
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
        return "TIMESTAMP WITH TIME ZONE"
    except ValueError:
        # If parsing fails, treat it as a regular string
        return "VARCHAR(255)"


def generate_simple_postgresql_schema(csv_file_path, table_name, connection_string):
    # Read the first few rows of the CSV file to infer data types
    num_rows_to_read = 5  # You can adjust this number based on your data
    df = pd.read_csv(csv_file_path, nrows=num_rows_to_read, encoding="utf-8")

    # Generate the SQL CREATE TABLE statement
    create_table_sql = f"CREATE TABLE {table_name} (\n"

    # Dynamically create columns based on inferred data types
    for column_name, data_type in zip(df.columns, df.dtypes):
        # Infer data type for object columns
        if data_type == "object":
            inferred_data_type = "TEXT"
        # Convert int to BIGINT, float to FLOAT
        elif "int" in str(data_type):
            inferred_data_type = "BIGINT"
        elif "float" in str(data_type):
            inferred_data_type = "FLOAT"
        # Use the actual data type for other types
        else:
            inferred_data_type = data_type

        # Quote column names containing dots
        if "." in column_name:
            column_name = f'"{column_name}"'

        create_table_sql += f"    {column_name} {inferred_data_type},\n"

    # Remove the trailing comma and newline
    create_table_sql = create_table_sql.rstrip(",\n") + "\n"
    create_table_sql += ");"

    # Connect to PostgreSQL and create the table
    with psycopg2.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            # Check if the table exists
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            cursor.execute(create_table_sql)
        conn.commit()


def insert_data(csv_file_path, table_name, connection_string):
    # Insert data into the table
    with psycopg2.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            with open(csv_file_path, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip the header
                for row in csv_reader:
                    # Replace empty strings with NULL for numeric columns
                    row = [value if value != "" else None for value in row]

                    insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})"
                    cursor.execute(insert_sql, row)
            conn.commit()


# Example usage:
csv_file_path = "C:\\Users\\rabeh\\Desktop\\TP Ala\\codeing\\minioffre.csv"
table_name = "job_offers"
connection_string = "dbname=postgres user=postgres password=Tpisd2024@@ host=db.hgakideicubdkaqbydqg.supabase.co port=5432"


def csv_wraper():
    generate_simple_postgresql_schema(csv_file_path, table_name, connection_string)
    insert_data(csv_file_path, table_name, connection_string)
