from pyspark.sql import SparkSession

# Step 1 - Create Spark Session with SIMPLE name
spark = SparkSession.builder.appName("Taxi Data App").getOrCreate()

df = spark.read.csv("taxi_zone_lookup.csv",header=True,inferSchema=True)


