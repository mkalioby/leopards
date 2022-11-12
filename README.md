# QyPy

Query list of dictionaries or objects as if you are filtering in  DBMS. You can have dicts objects) that are matched by OR, AND or NOT or all of them.

## Installation

```shell
pip install QyPy
```

## Usage

```python
from query import Q
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
from query import Q
l = [{"name":"John","age":"16"}, {"name":"Mike","age":"19"},{"name":"Sarah","age":"21"}]
filtered= Q(l,name__contains="k", age__lt = 20)

```

**Notes:** 
1. `Q` returns an iterator which can be converted to a list by calling `list`.
2. Even though, age was `str` in the dict, as the value of in the query dict was int, QyPy converted the value in dict automatically to match the query data type. This behaviour can be stopped by passing `False` to `convert_types` parameter.

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
from query import Q
l = [{"name":"John","age":"16"}, {"name":"Mike","age":"19"},{"name":"Sarah","age":"21"}]
filtered= Q(l,{"OR":[{"name__contains":"k"}, {"age__gte":21}]})
print(list(filtered))
```
output
```python
[{'name': 'Mike', 'age': '19'}, {'name': 'Sarah', 'age': '21'}]
```

### Usage of `NOT`
`NOT` or `__not__` takes a list of dictionaries to evaluate and returns with the first `True`.  
```python
from query import Q
l = [{"name":"John","age":"16"}, {"name":"Mike","age":"19"},{"name":"Sarah","age":"21"}]
filtered= Q(l,{"age__gt":15, "NOT":{"age__eq":19}})
print(list(filtered))
```
output
```python
[{'name': 'John', 'age': '16'}, {'name': 'Sarah', 'age': '21'}]
```
