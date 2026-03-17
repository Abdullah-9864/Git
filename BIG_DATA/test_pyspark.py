from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").master("local[1]").config("spark.driver.memory", "512m").getOrCreate()
print("Spark version:", spark.version)  # Print Spark version
spark.stop()  # Stop Spark
