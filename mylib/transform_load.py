"""
Transforms and Loads data into the local databricks database

"""

import csv
import os
from dotenv import load_dotenv
from databricks import sql


# load the csv file and insert into a new databricks database
def load(dataset="data/employees.csv"):
    """ "Transforms and Loads data into the local databricks database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    # print(*payload)
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            # employee_id,first_name,last_name,email,hire_date,salary,department

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS jmt_employees 
                           (employee_id INT, first_name STRING, last_name STRING, 
                           email STRING, hire_date DATE, salary FLOAT,
                           department STRING);
                """
            )

            cursor.execute("SELECT * FROM jmt_employees")
            result = cursor.fetchall()
            if not result:
                print("here")
                string_sql = "INSERT INTO jmt_employees VALUES"
                for i in payload:
                    string_sql += "\n" + str(tuple(i)) + ","
                string_sql = string_sql[:-1] + ";"
                print(string_sql)

                cursor.execute(string_sql)
                # result = cursor.fetchall()

                # for row in result:
                #     print(row)

            cursor.close()
            connection.close()
    return "db loaded or already loaded"


if __name__ == "__main__":
    load()
