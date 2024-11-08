# Complex SQL Query Project

## Overview

This project implements a complex SQL query on a MySQL database involving joins, aggregations, and sorting, as specified by the assignment. The repository includes all necessary files to set up and run the project, as well as explanations for each component and the query functionality.

## Repository Structure

- **.devcontainer/**: Contains configuration files for a development container.
  - `Dockerfile`: Defines the container environment.
  - `devcontainer.json`: Configures development container settings.

- **.github/workflows/**: Holds the configuration file for CI/CD.
  - `cicd.yml`: Sets up the CI/CD pipeline to test the SQL query and validate project requirements.

- **data/**: Folder containing sample CSV files used for testing and development.
  - `GroceryDB_lgFPro.csv`: Sample data file for the grocery database.
  - `employees.csv`: Sample data file for employee information.

- **mylib/**: Custom Python library for handling data extraction, querying, and transformation.
  - `__init__.py`: Initializes the `mylib` package.
  - `extract.py`: Handles data extraction logic.
  - `query.py`: Contains the complex SQL query.
  - `transform_load.py`: Processes data transformations and loads it into the database.

- **Root Files**:
  - `.gitignore`: Specifies files and directories ignored by Git.
  - `Dockerfile`: Builds the project environment.
  - `LICENSE`: Project license file.
  - `Makefile`: Defines commands for setting up, testing, and running the project.
  - `README.md`: Project documentation (this file).
  - `main.py`: Main script to run the project.
  - `requirements.txt`: Lists required Python packages.
  - `setup.sh`: Script for setting up the environment.
  - `test_main.py`: Contains tests for the project components.

## Requirements

To run this project, you need:
- Docker
- Python 3.8+
- A MySQL database instance (or any other SQL/NoSQL database, such as DynamoDB, Databricks, or Neo4j, if swapping is needed).

Install dependencies by running:

```bash
pip install -r requirements.txt
```

## Complex SQL Query

### Query Description

The complex SQL query is located in `mylib/query.py`. It involves:
- **Joins**: To connect data from multiple tables, such as grocery data and employee information.
- **Aggregations**: Using functions like `SUM`, `AVG`, and `COUNT` to get summarized insights.
- **Sorting**: Ordering the results based on specified columns to present data meaningfully.

This query retrieves information on employee sales performance, total sales per product category, and average sales by region, sorted by the highest-performing categories.

### Query Explanation

The query is designed to provide insights into:
- **Top-performing products and categories** based on total sales.
- **Sales performance by employee** to identify the most effective team members.
- **Regional sales trends** to guide marketing and logistics decisions.

#### Expected Results
The query output will include:
- Product categories with the highest total sales.
- Individual employee sales records ranked by performance.
- Summary of average sales across different regions.

For more details on how the query is structured, refer to `mylib/query.py`.

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions and can be found in `.github/workflows/cicd.yml`. This pipeline automatically:
1. Tests the SQL query for functionality and performance.
2. Validates data loading and extraction scripts.
3. Ensures code formatting and documentation standards are met.

## How to Run

1. **Set up the Database**: Populate your MySQL database (or the chosen alternative) with the provided CSV files in the `data` folder.

2. **Run the Query**: Use `main.py` to execute the query and view the results.

   ```bash
   python main.py
   ```

3. **Testing**: Run tests with the following command:

   ```bash
   pytest test_main.py
   ```

## Deliverables

1. **SQL Query**: Located in `mylib/query.py`.
2. **Explanation**: Descriptions provided in the README and inline comments in `query.py`.
3. **CI/CD Pipeline**: Configured in `.github/workflows/cicd.yml`.
4. **Documentation**: This `README.md`.
