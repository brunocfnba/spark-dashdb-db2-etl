-- Source table CLIENT_TABLE ddl
create table CLIENT_TABLE (
  CLICODE integer,
  NAME varchar(60),
  BIRTHDAY date,
  DESCRIPTION CLOB(1000000)
)

-- target table CLIENT_TABLE_TARGET ddl
create table CLIENT_TABLE_TARGET (
  CLIENT_CODE integer,
  NAME varchar(60),
  DATE_OF_BIRTH date,
  GENERAL_INFO CLOB(1000000)
)
