from functools import partial
try:
    from Q import get_key_op, convert_value,check
except ModuleNotFoundError:  # pragma: no cover
    from .Q import get_key_op, convert_value,check # pragma: no cover

def Q(iterable:list, query:dict=None, convert_types=True, **kwargs):
    """
     Query a list of dictionary or objects by a query dict.
    :param iterable: the iterable of dicts
    :param query: dictionary holding your query
    :param convert_types: try to convert the field in data to match query type
    :return: Iterable of type filter
    """
    def filter_list(item, **kwargs):
        if type(item)  in (str, int, float, list, tuple):
            raise TypeError("The item in the list shall be dict or object")
        if type(item) is not dict:
            item= item.__dict__
        for k,v in kwargs.items():
            if k in("OR" , "__or__"):
                for q in v:
                    if filter_list(item,**q):
                        return True
                return False
            elif k in("AND","__and__"):
                for q in v:
                    if not filter_list(item,**q):
                        return False
                return True
            elif k in ("NOT", "__not__"):
               return  not filter_list(item,**v)
            key, op = get_key_op(k)
            value = item[key]
            if convert_types and type(v) != type(value):
                value = convert_value(value, type(v))
            if not check(value, op, v):
                return False
        return True
    if query is None: query={}
    query.update(kwargs)
    p = partial(filter_list, **query)
    return filter(p, iterable)

def Count(iterable:list, cols:list=None, col_name:str='count'):
    """
    :param iterable: iterable to count
    :param cols: columns used to aggregated
    :param col_name: the name of count column, default: count
    :return: iterable of dicts
    """
    new_dict={}

    for item in iterable:
        if type(item) is not dict:
            item=item.__dict__
        if cols:
            d={k:v for k,v in item.items() if k in cols}
            k = ":".join(d.values())
        else:
            k="ALL"
            d={}
        if not k in new_dict:
            new_dict[k]=d
            new_dict[k][col_name]=0
        new_dict[k][col_name]+=1
    return  new_dict.values()



def Max(iterable:list, col_name:str, cols:list=None, dtype=str):
    """

    :param iterable: iterable to loop through
    :param col_name: the name of the column that Max shall be computed against
    :param cols: columns to aggregate on
    :return: iterable of dicts
    """
    new_dict={}

    for item in iterable:
        if type(item) is not dict:
            item=item.__dict__
        if cols:
            d={k:v for k,v in item.items() if k in cols}
            k = ":".join(d.values())
        else:
            k='ALL'
            d={}
        v: str = item[col_name]
        if dtype!=str:
            v = dtype(v)
        if not k in new_dict:
            new_dict[k]=d
            new_dict[k][col_name]=v
        if v>new_dict[k][col_name]:
            new_dict[k][col_name] = v
    return new_dict.values()


def Min(iterable:list, col_name:str, cols:list=None, dtype=str):
    """

    :param iterable: iterable to loop through
    :param col_name: the name of the column that Min shall be computed against
    :param cols: columns to aggregate on
    :param dtype: data type of the cols

    :return: iterable of dicts
    """
    new_dict={}

    for item in iterable:
        if type(item) is not dict:
            item=item.__dict__
        if cols:
            d={k:v for k,v in item.items() if k in cols}
            k = ":".join(d.values())
        else:
            k="ALL"
            d={}
        v:str=item[col_name]
        if v != str:
            v=dtype(v)
        if not k in new_dict:
            new_dict[k]=d
            new_dict[k][col_name]=v
        if v<new_dict[k][col_name]:
            new_dict[k][col_name] = v
    return new_dict.values()

def Sum(iterable:list, col_name:str, cols:list=None):
    """

    :param iterable: iterable to loop through
    :param col_name: the name of the column that Sum shall be computed against
    :param cols: columns to aggregate on
    :return: iterable of dicts
    """
    new_dict={}

    for item in iterable:
        if type(item) is not dict:
            item=item.__dict__
        if cols:
            d={k:v for k,v in item.items() if k in cols}
            k = ":".join(d.values())
        else:
            k="ALL"
            d={}
        if not k in new_dict:
            new_dict[k]=d
            new_dict[k][col_name]=float(0)
        new_dict[k][col_name] += float(item[col_name])
    return new_dict.values()


def Avg(iterable:list, col_name:str, cols:list=None):
    """

    :param iterable: iterable to loop through
    :param col_name: the name of the column that Average shall be computed against
    :param cols: columns to aggregate on
    :return: iterable of dicts
    """
    new_dict={}

    for item in iterable:
        if type(item) is not dict:
            item=item.__dict__
        if cols:
            d={k:v for k,v in item.items() if k in cols}
            k = ":".join(d.values())
        else:
            k='ALL'
            d={}
        if not k in new_dict:
            new_dict[k]=d
            new_dict[k][col_name+"__sum"]=float(0)
            new_dict[k][col_name+"__count"]=float(0)
        new_dict[k][col_name+"__sum"] += float(item[col_name])
        new_dict[k][col_name+"__count"] += 1

    res = []
    for d,v in new_dict.items():
        v[col_name] = v.pop(col_name+"__sum")/ v.pop(col_name+"__count")
        res.append(v)
    return res