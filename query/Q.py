from decimal import Decimal

NULL_VALUES =('','.',None,"None","null")

def get_key_op(key):
    if "__" in key:
        cols = key.split("__")
        k = cols[0]
        op = cols[1]
    else:
        k = key
        op = "eq"
    return k, op


def convert_value(v,value_type):
    if value_type is float:
        return float(v)
    elif value_type is int:
        return int(v)
    elif value_type is bytes:
        return bytes(v,'ascii')
    elif value_type is Decimal:
        return Decimal(v)
    return str(v)

def item_match(value, op, qv):
    if op == "eq":
        return value == qv
    elif op == "neq":
        return value != qv
    elif op == "gt":
        return value > qv
    elif op == "gte":
        return value >= qv
    elif op == "lt":
        return value < qv
    elif op == "lte":
        return value <= qv
    elif op == "in":
        return value in qv
    elif op == "nin":
        return value not in qv
    elif op == "contains":
        return qv in value
    elif op == "ncontains":
        return qv not in value
    elif op == "icontains":
        return qv.lower() in value.lower()
    elif op == "nicontains":
        return qv.lower() not in value.lower()
    elif op == "null":
        res = value in NULL_VALUES
        return res == qv




