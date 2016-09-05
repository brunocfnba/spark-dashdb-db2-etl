# Spark ETL to move data from DB2 and DashDB

This code show how to use Spark to access a DB2 source table in a partitioned fashion taking advantage of the Spark distributed capabilities and insert into a DashDb database.

We came up with this need since we had several tables with many rows including CLOB fields and we needed to run it into an acceptable time (less than 30 minutes) so we decided to use Spark and its distributed capabilities.

##Accessing data in parallel mode 

The most important piece is how we read data from the database.
We need to use the jdbc driver option form the Dataframereader class.
