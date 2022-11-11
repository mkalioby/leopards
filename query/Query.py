from functools import partial
from Q import get_key_op, convert_value,item_match

def Q(data:list, query:dict=None, convert_types=True, **kwargs):
    """

    :param data: the iterable of dicts
    :param query: dictionary holding your query
    :param convert_types: try to convert the field in data to match query type
    :return:
    """
    def filter_list(item, **kwargs):
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
            if not item_match(value, op, v):
                return False
        return True
    if query is None: query={}
    query.update(kwargs)
    p = partial(filter_list, **query)
    return list(filter(p, data))