NULL_VALUES = ('', '.', None, "None", "null", "NULL")


def get_key_op(key:str):
    """Separate at the key to name and op"""
    if "__" in key:
        cols = key.split("__")
        k = cols[0]
        op = cols[1]
    else:
        k = key
        op = "eq"
    return k, op


def convert_value(v:str, value_type:type):
    """Converts str to the data type of the value"""
    from decimal import Decimal
    if value_type is float:
        return float(v)
    elif value_type is int:
        return int(v)
    elif value_type is bytes:
        return bytes(v, 'ascii')
    elif value_type is Decimal:
        return Decimal(v)
    return str(v)


def evaluate(value:type, op:str, qv:type):
    """Evaluate the current value again the query value based on type."""
    if op == "eq":
        return value == qv
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
    elif op == "contains":
        return qv in value
    elif op == "icontains":
        return qv.lower() in value.lower()
    elif op == "startswith":
        return value.startswith(qv)
    elif op == "istartswith":
        return value.lower().startswith(qv.lower())
    elif op == "endswith":
        return value.endswith(qv)
    elif op == "iendswith":
        return value.lower().endswith(qv.lower())
    elif op == "isnull":
        res = value in NULL_VALUES
        return res == qv


def check(value:type, op:str, qv:type):
    """Checks for negation"""

    if op.startswith("n"):
        op = op[1:]
        return not evaluate(value, op, qv)
    return evaluate(value, op, qv)
