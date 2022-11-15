import unittest
from decimal import Decimal


from test_file import *

def Q(data,query=None,convert_types=True,**kwargs):
    from Query import Q
    return list(Q(data,query,convert_types,**kwargs))
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

employees = [Employee('Ahmed',12),Employee('Mohamed',24)]
class TestConditions(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos': '114372214', 'end pos': '114372214'})), 1)

    def test_neq(self):
        self.assertEqual(len(Q(l, chromosome__neq='chr1')), 24)

    def test_neq2(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__neq': '114372214'})), 3)

    def test_gt(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__gt': '114372214', 'end pos__gt': '114372214'})), 2)

    def test_gte(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__gte': '114372214', 'end pos__gte': '114372214'})),
                         3)

    def test_lt(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__lt': '114372214'})), 1)

    def test_lte(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'end pos__lte': '114372214'})), 2)

    def test_in(self):
        self.assertEqual(len(Q(l, chromosome__in=('chr1', 'chr22'))), 5)

    def test_nin(self):
        self.assertEqual(len(Q(l, chromosome__nin=('chr1', 'chr22'))), 23)

    def test_contains(self):
        self.assertEqual(len(Q(l, chromosome__contains='chr2')), 3)

    def test_ncontains(self):
        self.assertEqual(len(Q(l, chromosome__ncontains='chr1')), 16)

    def test_contains2(self):
        self.assertEqual(len(Q(l, chromosome__contains='Chr2')), 0)

    def test_ncontains2(self):
        self.assertEqual(len(Q(l, chromosome__ncontains='Chr2')), 28)

    def test_icontains(self):
        self.assertEqual(len(Q(l, chromosome__icontains='Chr2')), 3)

    def test_icontains2(self):
        self.assertEqual(len(Q(l, chromosome__icontains='chr2')), 3)

    def test_nicontains(self):
        self.assertEqual(len(Q(l, chromosome__nicontains='Chr2')), 25)

    def test_nicontains2(self):
        self.assertEqual(len(Q(l, chromosome__nicontains='chr2')), 25)

    def test_null(self):
        self.assertEqual(len(Q(l, filter__isnull=True)), 16)

    def test_null2(self):
        self.assertEqual(len(Q(l, {"filter__isnull": False})), 12)

    def test_startswith(self):
        self.assertEqual(len(Q(l, {"reference__startswith": 'T'})), 7)

    def test_istartswith(self):
        self.assertEqual(len(Q(l, {"reference__istartswith": 't'})), 7)

    def test_nstartswith(self):
        self.assertEqual(len(Q(l, {"reference__nstartswith": 'T'})), 21)

    def test_endswith(self):
        self.assertEqual(len(Q(l, {"observed__endswith": 'C'})), 5)

    def test_iendsswith(self):
        self.assertEqual(len(Q(l, {"observed__iendswith": 'C'})), 5)

    def test_nendswith(self):
        self.assertEqual(len(Q(l, {"observed__nendswith": 'C'})), 23)

class TestConverations(unittest.TestCase):
    def test_int(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos': 114372214, 'end pos': 114372214})), 1)

    def test_bytes(self):
        self.assertEqual(len(Q(l, {"chromosome": b'chr1', 'start pos': 114372214, 'end pos': 114372214})), 1)

    def test_float(self):
        res = Q(l, {"quality__gte": 133.47, "quality__lt": 142.39})
        self.assertEqual(len(res), 1)

    def test_decimal(self):
        res = Q(l, {"quality__gte": Decimal(133.47), "quality__lte": Decimal(142.39)})
        self.assertEqual(len(res), 1)


class TestCombination(unittest.TestCase):
    def test_or(self):
        res = Q(l, {"OR": [{"chromosome": 'chr1', 'start pos': 114372214, 'end pos': 114372214},
                           {"reference": 'C', 'observed': 'A'}]})

        self.assertEqual(len(res), 2)

    def test_and(self):
        res = Q(l, {"__and__": [{"chromosome": 'chr1', 'start pos': 114372214, 'end pos': 114372214},
                                {"reference__neq": 'G'}]})
        self.assertEqual(len(res), 1)

    def test_not(self):
        self.assertEqual(len(Q(l, {"reference": "T", "NOT": {"observed": "C"}})), 4)


class TestObjects(unittest.TestCase):
    def test_obj(self):
        self.assertEqual(len(Q(employees,age__gt=13)),1)

class TestException(unittest.TestCase):
    def testInt(self):
        self.assertRaises(TypeError, Q, [1,2,3],{"i__gt":1})

if __name__ == '__main__':
    unittest.main()
