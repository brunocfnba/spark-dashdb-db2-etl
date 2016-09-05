from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *

conf = SparkConf().setAppName("spark_db2_dash")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

#Query to run against DB2
sql1 = "(SELECT CLICODE, NAME, BIRTHDAY, DESCRIPTION from CLIENT_TABLE) as tableClient"

#Client dataframe creation from DB2 data using 300 partitions on CLICODE column
dfClient = sqlContext.read.format("jdbc").options(url="jdbc:db2://123.13.321.31:50000/DBNAME", user="dbuser", password="dbpassword",partitionColumn="CLICODE", lowerBound=0L, upperBound=100000L, dbtable=sql1, numPartitions=300L, driver="com.ibm.db2.jcc.DB2Driver").load()

#Replacing client dataframe schema names with the ones in the target table
finalDF = dfClient.select(dfClient.CLICODE.alias("CLIENT_CODE"),dfCLient.NAME,dfClient.BIRTHDAY.alias("DATE_OF_BIRTH"),dfCLient.DESCRIPTION.alias("GENERAL_INFO"))

#DashDB access information
propertiesDBDash = {
                    "user":"dashUser",
                    "password":"dashPassword"}

#Writing data into target DashDB database
joinedFinal.write.mode("append").jdbc("jdbc:db2://youraddress.com:50000/DBNAME", "CLIENT_TABLE_TARGET",properties=propertiesDBDash)
