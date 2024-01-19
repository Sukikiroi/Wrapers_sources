import csv,re
 
import pandas as pd
from datetime import datetime
import psycopg2


connection_string = "dbname=postgres user=postgres password=Tpisd2024@@ host=db.hgakideicubdkaqbydqg.supabase.co port=5432"

def infer_data_type(value):
    try:
        # Try to parse the value as a timestamp
        datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z')
        return 'TIMESTAMP WITH TIME ZONE'
    except ValueError:
        # If parsing fails, treat it as a regular string
        return 'VARCHAR(255)'
    

    
csv_file_path = 'C:\\Users\\rabeh\\Desktop\\TP Ala\\codeing\\offresemploi.csv'
table_name = 'job_offers'
# Read the first few rows of the CSV file to infer data types
num_rows_to_read = 5  # You can adjust this number based on your data
df = pd.read_csv(csv_file_path, nrows=num_rows_to_read, encoding='utf-8')

# Generate the SQL CREATE TABLE statement
# create_table_sql = f"CREATE TABLE {table_name} (\n"

# # Dynamically create columns based on inferred data types
# for column_name, data_type in zip(df.columns, df.dtypes):
#     if data_type == 'object':
#         inferred_data_type = infer_data_type(df[column_name].iloc[0])
#     else:
#         inferred_data_type = data_type

#     create_table_sql += f"    {column_name} {inferred_data_type},\n"

# # Remove the trailing comma and newline
# create_table_sql = create_table_sql.rstrip(',\n') + '\n'

# # Close the CREATE TABLE statement
# create_table_sql += ');'

# # Print or use the generated SQL statement
# print(create_table_sql)



def extract_columns_from_sql(sql_query):
    # Use regular expressions to find all column names
    column_pattern = re.compile(r'\b(\w+)\s*,')

    matches = column_pattern.findall(sql_query)

    return matches





 

def check_columns_in_csv(file_path, target_columns):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        first_row = next(reader, None)  # Get the first row (header) or None if the file is empty

        if first_row:
            # Check if all target columns are present in the first row
            return all(column in first_row for column in target_columns)
        else:
            return False  # File is empty, no header to check against
 



view= "SELECT intitule,id FROM job_offers ;"


def excute_sql_mysql(connection_string, view):
    data=[]
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(connection_string)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(view)

        # Fetch all rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(str(row)+"'\n'")

    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()




    return data



excute_sql_mysql(connection_string,view)