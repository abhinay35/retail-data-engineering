from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, to_date, year

# -----------------------------
# 1. Spark Session
# -----------------------------
spark = SparkSession.builder \
    .appName("Retail Data Engineering Project") \
    .getOrCreate()

# -----------------------------
# 2. Read Raw Data
# -----------------------------
df_sales = spark.read.csv(
    "data/AdventureWorks_Sales.csv",
    header=True,
    inferSchema=True
)

df_calendar = spark.read.csv(
    "data/AdventureWorks_Calendar.csv",
    header=True,
    inferSchema=True
)

df_products = spark.read.csv(
    "data/AdventureWorks_Products.csv",
    header=True,
    inferSchema=True
)

# -----------------------------
# 3. Data Cleaning
# -----------------------------
df_sales = df_sales.dropDuplicates()

df_sales = df_sales.filter(
    col("SalesAmount").isNotNull()
)

# -----------------------------
# 4. Convert Date
# -----------------------------
df_calendar = df_calendar.withColumn(
    "Date",
    to_date(col("FullDateAlternateKey"))
)

# -----------------------------
# 5. Join Tables
# -----------------------------
df_joined = df_sales \
    .join(df_calendar,
          df_sales["OrderDateKey"] == df_calendar["DateKey"],
          "inner") \
    .join(df_products,
          df_sales["ProductKey"] == df_products["ProductKey"],
          "inner")

# -----------------------------
# 6. Transformations
# -----------------------------

# Extract Year
df_joined = df_joined.withColumn(
    "Year",
    year(col("Date"))
)

# Total Sales by Year
yearly_sales = df_joined.groupBy("Year") \
    .agg(sum("SalesAmount").alias("TotalSales"))

# Sales by Product
product_sales = df_joined.groupBy("EnglishProductName") \
    .agg(sum("SalesAmount").alias("TotalSales"))

# -----------------------------
# 7. Show Results (Debug)
# -----------------------------
yearly_sales.show()
product_sales.show()

# -----------------------------
# 8. Write Output
# -----------------------------
yearly_sales.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("output/yearly_sales")

product_sales.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("output/product_sales")

# -----------------------------
# 9. Stop Spark
# -----------------------------
spark.stop()
