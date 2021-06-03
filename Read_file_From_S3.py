from pyspark.sql import SparkSession
import findspark
findspark.init() 
 
spark = SparkSession.builder \
        .appName("schema_test") \
        .config('fs.s3a.access.key',"AKIAUYWYBTX76YGDLX45")\
        .config('fs.s3a.secret.key', "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")\
        .getOrCreate()
 
bucket = "buck-mumbai-hr"
data_key = "emp_data.txt"
data_location = f"s3a://{bucket}/{data_key}"
 
df = spark.read.csv(data_location, header = 'True', inferSchema = True)
 
df.limit(5).toPandas()