# retail-data-engineering
Retail data engineering project using pyspark
## 🏗️ Architecture Diagram

                            +----------------------+
                            |   Data Source (API)  |
                            +----------+-----------+
                                      |
                                      v
                            +----------------------+
                            | Azure Data Factory   |
                            |  (Data Ingestion)    |
                            +----------+-----------+
                                       |
                                       v
                            +----------------------+
                            |  Azure Data Lake     |
                            |   (Bronze Layer)     |
                            +----------+-----------+
                                       |
                                       v
                              +----------------------+
                              | Azure Databricks     |
                              |  (PySpark Transform) |
                              +----------+-----------+
                                         |
               +------------------------+-------------------------+
               |                                                  |
               v                                                  v
     +----------------------+                         +----------------------+
     | Silver Layer (Clean) |                         | Gold Layer (Curated) |
     +----------+-----------+                         +----------+-----------+
           |                                                |
           +----------------------+-------------------------+
                                  |
                                  v
                        +----------------------+
                         | Azure Synapse       |
                         | (Data Warehouse)    |
                        +----------+-----------+
                                   |
                                   v
                         +----------------------+
                         |  Analytics / BI      |
                         +----------------------+


------------------------------------------------------------
----->Architecture Explanation

* **Azure Data Factory** → Extracts data from API
* **ADLS Gen2** → Stores raw data (Bronze)
* **Databricks (PySpark)** → Transforms data
* **Silver Layer** → Cleaned data
* **Gold Layer** → Business-ready data
* **Synapse Analytics** → Data warehousing
* **BI Tools** → Reporting & insights
----------------------------------------------------------
----->The project follows the Medallion Architecture:

Bronze Layer → Raw data ingestion
Silver Layer → Cleaned and transformed data
Gold Layer → Aggregated data for analytics
----------------------------------------------------------
----->Tech Stack

Azure Data Factory (ADF)
Azure Data Lake Storage Gen2 (ADLS)
Azure Databricks (PySpark)
Azure Synapse Analytics
Apache Spark
REST API (Data Source)
--------------------------------------------------------------------------------
---->Data Pipeline Flow
Data Ingestion
Data is extracted from API sources.
Azure Data Factory pipelines are used to load raw data into ADLS (Bronze layer).
Data Storage
Raw data is stored in Azure Data Lake Gen2.
Data Transformation
Azure Databricks is used to process and clean data using PySpark.
Data is transformed from Bronze → Silver → Gold layers.
Data Warehousing
Processed data is loaded into Azure Synapse Analytics.
Analytics & Reporting
Data is structured for querying and analysis.
--------------------------------------------------------------------------------
----->Project Structure

├── data_ingestion/
├── databricks_notebooks/
├── pipelines/
├── datasets/
├── scripts/
└── README.md
--------------------------------------------------------------------------------
---->How to Run the Project

Create Azure resources:
Data Factory
Data Lake Storage Gen2
Databricks Workspace
Synapse Analytics
Configure Linked Services in Azure Data Factory.
Set up Databricks cluster.
Run ADF pipelines to ingest data.
Execute Databricks notebooks for transformations.
Load processed data into Synapse.
-------------------------------------------------------------------------------
----->Acknowledgements

This project is inspired by a real-world Azure Data Engineering tutorial and is intended for learning
