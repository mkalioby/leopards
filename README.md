# Leopards

[![PyPI version](https://badge.fury.io/py/leopards.svg)](https://badge.fury.io/py/leopards)
[![Python Versions](https://img.shields.io/pypi/pyversions/leopards.svg)](https://img.shields.io/pypi/pyversions/leopards.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-success)
![build status](https://github.com/mkalioby/leopards/actions/workflows/workflow.yml/badge.svg)

Leopards is a way to query list of dictionaries or objects as if you are filtering in  DBMS. 
You can get dicts/objects that are matched by OR, AND or NOT or all of them.
As you can see in the comparison they are much faster than Pandas.


## Installation

```shell
pip install leopards
```

## Usage

```python
from leopards import Q
l = [{"name":"John","age":"16"}, {"name":"Mike","age":"19"},{"name":"Sarah","age":"21"}]
filtered= Q(l,{'name__contains':"k", "age__lt":20})
print(list(filtered))
```
output
```python
[{'name': 'Mike', 'age': '19'}]
```

The above filtration can be written as

```python
from leopards import Q

l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"}]
filtered = Q(l, name__contains="k", age__lt=20)

```

**Notes:** 
1. `Q` returns an iterator which can be converted to a list by calling `list`.
2. Even though, age was `str` in the dict, as the value of in the query dict was `int`, Leopards converted the value in dict automatically to match the query data type. This behaviour can be stopped by passing `False` to `convert_types` parameter.

## Supported filters
* `eq`: equals and this default filter
* `gt`: greater than.
* `gte`: greater than or equal.
* `lt`: less than 
* `lte`: less than or equal 
* `in`: the value in a list of a tuple.
    * e.g.  age__in=[10,20,30]
* `contains`: contains a substring as in the example.
* `icontains`: case-insensitive `contains`.
* `startswith`: checks if a value starts with a query strings.
* `istartswith`: case-insensitive `startswith`.
* `endswith`: checks if a value ends with a query strings.
* `iendswith`: case-insensitive `endswith`.
* `isnull`:  checks if the value matches any of NULL_VALUES which are `('', '.', None, "None", "null", "NULL")`
  * e.g. `filter__isnull=True` or `filter__isnull=False`

For `eq`,`gt`,`gte`,`lt`,`lte`, `in`, `contains`, `icontains`, `startswith`,`istartswith`, `endswith` and `iendswith`, you can add a `n` to negate the results. e.g  `nin` which is equivalent to `not in` 

   
## Advanced examples
This section will cover the use of `OR`, `AND` and `NOT`

### Usage of `OR`
`OR` or `__or__` takes a list of dictionaries to evaluate and returns with the first `True`.

```python
from leopards import Q

l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"}]
filtered = Q(l, {"OR": [{"name__contains": "k"}, {"age__gte": 21}]})
print(list(filtered))
```
output
```python
[{'name': 'Mike', 'age': '19'}, {'name': 'Sarah', 'age': '21'}]
```

### Usage of `NOT`
`NOT` or `__not__` takes a dict for query run.

```python
from leopards import Q

l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"}]
filtered = Q(l, {"age__gt": 15, "NOT": {"age__eq": 19}})
print(list(filtered))
```
output
```python
[{'name': 'John', 'age': '16'}, {'name': 'Sarah', 'age': '21'}]
```

### Usage of `AND`
`AND` or `__and__` takes a list of dict for query run, returns with the first `False`.

```python
from leopards import Q

l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"}]
filtered = Q(l, {"__and__": [{"age__gte": 15}, {"age__lt": 21}]})
print(list(filtered))
```
output
```python
[{'name': 'John', 'age': '16'}, {'name': 'Mike', 'age': '19'}]
```

## Aggregating Data

You  can run the following aggregations
* Count
* Max
* Min
* Sum
* Avg

### Count

Find the count of certain aggregated column
```python
l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"},{"name":"John","age":"19"}]
from leopards import Count
count = Count(l,['age'])
```
output
```python
[{"age":"16","count":1},{"age":"19","count":2}, {"age":"21","count":1}]
```

### Max

Find the Max value for a certain column in  certain aggregated columns
```python
l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"},{"name":"Joh","age":"19"}]
from leopards import Max
count = Max(l,"age",['name'],dtype=int)
```
output
```python
[{'name': 'John', 'age': '19'}, {'name': 'Mike', 'age': '19'}, {'name': 'Sarah', 'age': '21'}]
```

**Notes:**
* If you don't pass the aggregation columns, the maximum will be found across dataset.
* You can pass the datatype of the column to convert it on the fly while evaluating
```python
l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"},{"name":"Joh","age":"19"}]
from leopards import Max
m = Max(l,"age",dtype=int)
```

output
```python
[{'age': 21}]
```


### Min

Find the Max value for a certain column in  certain aggregated columns
```python
l = [{"name": "John", "age": "16"}, {"name": "Mike", "age": "19"}, {"name": "Sarah", "age": "21"},{"name":"Joh","age":"19"}]
from leopards import Min
m = Min(l,"age",['name'])
```
output
```python
[{'name': 'John', 'age': '16'}, {'name': 'Mike', 'age': '19'}, {'name': 'Sarah', 'age': '21'}]
```
**Note:** 
* If you don't pass the aggregation columns, the min will be found across dataset.
* You can pass the datatype of the column to convert it on the fly while evaluating


## Sum and Avg

Like Min and Max but only works with integers and floats.

## Comparison with Pandas

This is done on Python 3.8 running on Ubuntu 22.04 on i7 11th generation and 32 GB of RAM.

| Comparison                                                  | Pandas   | Leopards    |
|-------------------------------------------------------------|----------|-------------|
| Package Size     <br/> (Lower is better)                    | 29.8 MB  | **7.5 KB**  |
| import Time (Worst) <br/> (Lower is better)                 | 146 ms   | **1.05 ms** |
| load 10k CSV lines<br/> (Lower is better) <sup>[1]</sup>    | 0.295s   | **0.138s**  |
| get first matched record<br/> (Lower is better)             | 0.310s   | **0.017s**  |
| print all filtered records (10/10k) <br/> (Lower is better) | 0.310s   | **0.137s**  | 
| filter by integers <br/>(Lower is better)                   | 0.316s   | **0.138s**  |

<sup>[1]</sup> This was loading the whole csv in memory which was for sake of fair comparison. 
Nevertheless,  Leopards can work with DictReader as an iterable which executes in **0.014s**, then it handles line by line.

Thanks for [Asma Tahir](https://github.com/tahirasma) for Pandas stats.