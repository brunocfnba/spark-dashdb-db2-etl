# Spark ETL to move data from DB2 and DashDB

This code show how to use Spark to access a DB2 source table in a partitioned fashion taking advantage of the Spark distributed capabilities and insert into a DashDb database.

We came up with this need since we had several tables with many rows including CLOB fields and we needed to run it into an acceptable time (less than 30 minutes) so we decided to use Spark and its distributed capabilities.

##Accessing data in parallel mode 

The most important piece is how we read data from the database.
We need to use the jdbc driver option from the Dataframereader class for class details and methods acceess here [here](https://spark.apache.org/docs/2.0.0/api/java/org/apache/spark/sql/DataFrameReader.html)

```
dfClient = sqlContext.read.format("jdbc")
        .options(url="jdbc:db2://123.13.321.31:50000/DBNAME", user="dbuser", password="dbpassword",
        partitionColumn="CLICODE", lowerBound=0L, upperBound=100000L, dbtable=sql1, numPartitions=300L, driver="com.ibm.db2.jcc.DB2Driver").load()
```

In order to use more than one partition to read from the table, you need a numeric column (integer, float, etc) to be used as the partitioning hash. In this code I'm using CLICODE, a sequence generated number, the column name is added to the "partitionColumn" attribute.
> It's good to avoid low-cardinality columns since you'd get most of your data mapped into the same partition

The lower and upperBound attributes defines the values the "WHERE" created withing each minor query should start and end respectively.
> That's why it's important to check your column data distribution in order to provide proper values for these attributes

The "dbtable" attribute only accepts a table as an attribute, but if you need to extract more complex queries from your source database without using Spark processing, generate the query you want to (with all the joins and complexities you require) and wrap it as a table.

numPartitions is where you define how many partitions should be created (how many queries are going to be generated to query the table).
> Avoid too large numbers since you could bring your database down due to several simultaneous connections.

Provide the DB2 driver in the driver attribute.

## Adjusting column names
To use the native jdbc connector, you need to ensure the schema has the same column names as the target table. For this the spark dataframe alias can be used.
```
finalDF = dfClient.select(dfClient.CLICODE.alias("CLIENT_CODE"),dfCLient.NAME,dfClient.BIRTHDAY.alias("DATE_OF_BIRTH"),dfCLient.DESCRIPTION.alias("GENERAL_INFO"))
```

To write the data the default dataframewriter class is used.

## Run the job
To run the job, the spark-submit is used. It's required to specify the driver path in the command call, otherwise Spark is not able to find it and can't share the driver among the executors.
I have added the DB2/DashDB driver to the repo. Assuming you are runnning all from the same folder this is the most basic way to run your spark job:
```
spark-submit --master spark://bldbz172235:7077  --jars db2jcc4.jar --conf spark.executor.extraClassPath=db2jcc4.jar --driver-class-path db2jcc4.jar spark_sr.py
```
There are more options to use in the spark-submit command to fine tune and change its behavior. Check [here](http://spark.apache.org/docs/latest/submitting-applications.html) for details.
