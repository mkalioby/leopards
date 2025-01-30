# Usage 

This document covers how to use leopards with different file types

## CSV

`DictReader` from `csv` module can be used to read csv files as dictionaries as shown below.

```python
import csv
from leopards import Q

data = csv.DictReader(open("data.csv"))
res = Q(data, {"age__gt": 15})
```

## TSV
`DictReader` from `csv` module can be used to read tsv files as dictionaries as shown below.

```python
import csv
from leopards import Q

data = csv.DictReader(open("data.csv"), delimiter="\t")
res = Q(data, {"age__gt": 15})
```

## JSON
`json.load` can be used to read json files as dictionaries as shown below.

```python

import json
from leopards import Q

data = json.load(open("data.json"))
res = Q(data, {"age__gt": 15})
```

## XLS

`xlrd` library can be used to read xls files as dictionaries as shown below.

```python
import xlrd
from leopards import Q

wb = xlrd.open_workbook("data.xls")
sh = wb.sheets()[0]
keys = sh.row_values(0)
data =[]
for n in range(1, sh.nrows):
    data.append({key: sh.row_values(n)[n2] for n2, key in enumerate(keys)})
res = Q(data, {"age__gt": 15})                
```

## ClickHouse
'clickhouse_driver' library can be used to read data from ClickHouse as dictionaries as shown below.
```python
import clickhouse_connect
client = clickhouse_connect.get_client( host='localhost',  username='default',password='' )
rows = client.execute("SELECT * FROM TABLE")
data = rows.named_results()
res = Q(data, {"age__gt": 15})
```

## MySQL

`mysql-client` library can be used to read data from MySQL as dictionaries as shown below.

```python
import MySQLdb
from MySQLdb.cursors import DictCursor
from leopards import Q

db=MySQLdb.connect(user='root',password='PASS', database="db", cursorclass=DictCursor)
cursor = db.cursor()
cursor.execute("SELECT * FROM TABLE")
data = cursor.fetchall()
res = Q(data, {"age__gt": 15})
```