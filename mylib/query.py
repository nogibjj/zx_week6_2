"""Query the database"""

from dotenv import load_dotenv
from databricks import sql
import os

complex_query = """
WITH deparment_sals AS (
  SELECT department, 
    COUNT(employee_id) AS dep_emp,
    AVG(salary) AS dep_salary 
  FROM default.jmt_employees 
  GROUP BY department 
)

SELECT * FROM default.jmt_employees  
JOIN deparment_sals 
ON default.jmt_employees.department = deparment_sals.department 
ORDER BY deparment_sals.dep_salary DESC;
"""


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SERVER_HOSTNAME"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:

            cursor.execute(complex_query)
            result = cursor.fetchall()

            for row in result:
                print(row)

            cursor.close()
            connection.close()
    return "query sucessful"


if __name__ == "__main__":
    query()
