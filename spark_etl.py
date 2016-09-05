from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *

conf = SparkConf().setAppName("spark_change_dash")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

#read data from dashDB
propertiesDBMaximo = {"user":"r",
                      "password": ""}

sql1 = "(SELECT w.WORKORDERID, w.WONUM, w.STATUS, w.WORKTYPE, w.DESCRIPTION, w.REPORTDATE, w.SCHEDSTART, w.SCHEDFINISH, w.OWNER, w.OWNERGROUP, TRIM(w.PLUSPCUSTOMER) AS PLUSPCUSTOMER, w.PMCHGTYPE, w.WOCLASS, w.ACTSTART, w.ACTFINISH, w.ITDCLOSURECODE, w.FAILURECODE, w.BACKOUTPLAN,w.COMMODITY, w.CINUM, w.PMCHGAPPROVALSTATE, w.ITDCHGPRETSTDTL, cd.LDTEXT AS CHANGE_DESCRIPTION, ca.LDTEXT AS CAUSE, pdd.LDTEXT AS PRETEST_DETAIL_DESCRIPTION,fr.DESCRIPTION AS FAILURE_DESCRIPTION, bp.LDTEXT AS BACK_OUT_PLAN_DESCRIPTION,w.ITDCHCREATEDBY AS CREATED_BY FROM MAXIMO.WORKORDER w left outer join (select LDKEY, LDTEXT from maximo
