# DB Reader

**Keyword:** `DB`

**Functions:** 7

## Description

This is a Reader that enables FRIDA to connect and perform queries in databases. You must only supply a valid ADO.NET connection string, and your SQL script. The supported database types are SQL_Server, MySQL, ORACLE, SAP Hana and DB2.

## Quick Reference

| Function | Description |
|----------|-------------|
| [Connect](#connect) | Connect to a DB using a connection string. |
| [QueryToCsv](#querytocsv) | Execute a SQL query using a file and save the result in a CSV file. |
| [RunInputQuery](#runinputquery) | Execute a SQL query (Insert, Update, CreateTable, etc.) using a file. |
| [RunMultipleInputQueries](#runmultipleinputqueries) | Execute many DML and DDL SQL instructions (Insert, Update, CreateTable, etc.)... |
| [RunOutputQuery](#runoutputquery) | Executes a SQL query (Select) using a file. |
| [RunStoredProcedure](#runstoredprocedure) | Execute a Stored Procedure. |
| [ShowQueryInfo](#showqueryinfo) | Logs the query to execute, fields, and query result |

---

## Functions

### Connect

> Connect to a DB using a connection string.

Adds a db connection string to the dictionary of available databases. By default, all connections string are assumed as SQL_Server, unless you specify the type (SQL_SERVER, MY_SQL, ORACLE, SAP_HANA, DB2). SAP_HANA > Requires to install driver > SAP_HANA Client for Windows.

**Parameters:**
- `conString`
- `dbKey`
- `sqlType`

**Syntax:**

```
Connect to DB connectionstring={<conString>} name={<dbKey>}
Connect to DB connectionstring={<conString>} name={<dbKey>} type={<sqlType:SQL_SERVER|MY_SQL|ORACLE|SAP_HANA|DB2>}
```

**Options:**

- `sqlType`: `SQL_SERVER`, `MY_SQL`, `ORACLE`, `SAP_HANA`, `DB2`

**Examples:**

```
Connect to DB connectionstring={Server=tcp:server,1433;Initial Catalog=thecat;Persist Security Info=False;User ID=*****;Password=*****;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;} name={myDB}
Connect to DB connectionstring={Server=tcp:server,1433;Initial Catalog=thecat;Persist Security Info=False;User ID=*****;Password=*****;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;} name={myDB} type={MY_SQL}
Connect to DB connectionstring={Server=tcp:server;UserName=*****;Password=*****;} name={myDB} type={SAP_HANA}
```

*Added: 2019-Oct-01*

---

### QueryToCsv

> Execute a SQL query using a file and save the result in a CSV file.

Executes a SQL query (Like RunOutputQuery), based on a separate txt file (for legibility) that must be included in the process' files. The output data will be saved in a CSV file on the given path. Alternatively, you can write an inline query instead of giving a txt.

**Parameters:**
- `script`
- `dbkey`
- `csvfilepath`

**Syntax:**

```
QueryToCsv {<script>} in {<dbkey>} save as {<csvfilepath>}
```

**Examples:**

```
QueryToCsv {GetPersons.sql} in {mybd} save as {persons}
QueryToCsv {GetProducts.txt} in {mybd} save as {products}
QueryToCsv {MyQuery.txt} in {mybd} save as {C:\Users\MyUser\Desktop\QueryResults\Result.csv}
```

*Added: 2012-Jun-12*

---

### RunInputQuery

> Execute a SQL query (Insert, Update, CreateTable, etc.) using a file.

Executes a SQL query (Insert, Update, CreateTable, etc.), based on a separate txt or sql file (for legibility) that must be included in the process' files. Alternatively, you can write an inline query instead of giving a txt. 
Note: semicolons at the end must be removed.

**Parameters:**
- `script`
- `dbkey`

**Syntax:**

```
RunInputQuery {<script>} in {<dbkey>}
```

**Examples:**

```
RunInputQuery {UpdateProduct.sql} in {mybd}
RunInputQuery {InsertProduct.txt} in {mybd}
RunInputQuery {update users set name = 'Joe' where iduser = 3} in {mybd}
```

*Added: 2019-Oct-21*

---

### RunMultipleInputQueries

> Execute many DML and DDL SQL instructions (Insert, Update, CreateTable, etc.) using a file.

Executes many DML and DDL SQL instructions (Insert, Update, CreateTable, etc.), based on a separate txt file (for legibility) that must be included in the process' files. The instructions must end with ";". Comments are allowed. **NOTE** Currently only Oracle DB can be used.

**Parameters:**
- `script`
- `dbkey`

**Syntax:**

```
RunInputQuery {<script>} in {<dbkey>}
```

**Examples:**

```
RunMultipleInputQueries {UpdateProducts.sql} in {mybd}
RunMultipleInputQueries {InsertProducts.txt} in {mybd}
```

*Added: 2021-Aug-06*

---

### RunOutputQuery

> Executes a SQL query (Select) using a file.

Execute an SQL (Select) query or multiple queries separated by ";", based on a separate txt or sql file (for readability) that should be included in the process files. The output data will be stored in a 2D list and when there are multiple queries, a counter will be added. In addition, an automatic variable "query_field_names", "query_field_names2", etc will be saved, containing the names of the query fields, dynamically depending on your specific query. Alternatively, you can write a query online instead of providing a txt or sql. (Optional). You can specify the output format of a date or an integer 

**Parameters:**
- `script`
- `dbkey`
- `varName`

**Syntax:**

```
RunOutputQuery {<script>} in {<dbkey>} as {<varName>}
```

**Examples:**

```
RunOutputQuery {Query.sql} in {mybd} as {products}
RunOutputQuery {GetProducts.txt} in {mybd} as {products}
RunOutputQuery {Select * from users} in {mybd} as {products}
```

*Added: 2019-Oct-01*

---

### RunStoredProcedure

> Execute a Stored Procedure.

Executes a Stored Procedure, based on a separate txt or sql file that must be included in the process' files. VarName will contain a 2D list with the query returned. Field names can be read in variable 'query_field_names'. 
When "single value" syntax is used, VarName will be a string variable, use this whenever the store procedure only returns one value.

**Parameters:**
- `script`
- `dbkey`
- `varName`

**Syntax:**

```
RunStoredProcedure {<script>} in {<dbkey>} as {<varname>}
RunStoredProcedure {<script>} in {<dbkey>} as single value {<varname>}
```

**Examples:**

```
RunStoredProcedure {SP_Users.sql} in {mybd} as {users}
RunStoredProcedure {SPProduct.txt} in {mybd} as {resultado}
RunStoredProcedure {RegisterProduct.sql} in {mybd} as single value {idRegistered}
```

*Added: 2020-May-21*

---

### ShowQueryInfo

> Logs the query to execute, fields, and query result

Prints the result of the queries in the registry, as well as query to execute and name of fields. By default, it is disabled. You can activate any of the options separately

**Parameters:**
- `printscript`
- `printfieldsname`
- `printresults`

**Syntax:**

```
ShowQueryInfo script={<printscript:true|false>} fieldNames={<printfieldsname:true|false>} results={<printresults:true|false>}
```

**Options:**

- `printscript`: `true`, `false`
- `printfieldsname`: `true`, `false`
- `printresults`: `true`, `false`

**Examples:**

```
ShowQueryInfo script={true}
ShowQueryInfo fieldNames={true}
ShowQueryInfo results={true}
```

*Added: 2021-Aug-20*

---
