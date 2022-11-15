from functools import partial
try:
    from Q import get_key_op, convert_value,check
except ModuleNotFoundError:
    from .Q import get_key_op, convert_value,check

def Q(data:list, query:dict=None, convert_types=True, **kwargs):
    """
     Query a list of dictionary or objects by a query dict.
    :param data: the iterable of dicts
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
    return filter(p, data)