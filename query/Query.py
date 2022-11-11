from functools import partial
from Q import get_key_op, convert_value,item_match

def query(data:list, query:dict, convert_types=True):
    """

    :param data: the iterable of dicts
    :param query: dictionary holding your query
    :param convert_types: try to convert the field in data to match query type
    :return:
    """
    def filter_list(item, **kwargs):
        for k,v in kwargs.items():
            key, op = get_key_op(k)
            value = item[key]
            if convert_types and type(v) != type(value):
                value = convert_value(value, type(v))
            if not item_match(value, op, v):
                return False
        return True

    p = partial(filter_list, **query)
    return list(filter(p, data))