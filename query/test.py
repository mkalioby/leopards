import unittest
from decimal import Decimal

from Query import Q
from test_file import *


class TestConditions(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos': '114372214', 'end pos': '114372214'})), 1)

    def test_neq(self):
        self.assertEqual(len(Q(l, chromosome__neq ='chr1')), 24)

    def test_neq2(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__neq': '114372214'})), 3)

    def test_gt(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__gt': '114372214', 'end pos__gt': '114372214'})), 2)

    def test_gte(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__gte': '114372214', 'end pos__gte': '114372214'})), 3)

    def test_lt(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos__lt': '114372214'})), 1)

    def test_lte(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'end pos__lte': '114372214'})), 2)

    def test_in(self):
        self.assertEqual(len(Q(l, chromosome__in= ('chr1', 'chr22'))), 5)

    def test_contains(self):
        self.assertEqual(len(Q(l, chromosome__contains='chr2')), 3)

    def test_contains2(self):
        self.assertEqual(len(Q(l, chromosome__contains='Chr2')), 0)

    def test_icontains(self):
        self.assertEqual(len(Q(l, chromosome__icontains='Chr2')), 3)

    def test_icontains2(self):
        self.assertEqual(len(Q(l, chromosome__icontains ='chr2')), 3)

    def test_null(self):
        self.assertEqual(len(Q(l, filter__null= True)), 16)

    def test_null2(self):
        self.assertEqual(len(Q(l, {"filter__null": False})), 12)


class TestConverations(unittest.TestCase):
    def test_int(self):
        self.assertEqual(len(Q(l, {"chromosome": 'chr1', 'start pos': 114372214, 'end pos': 114372214})), 1)

    def test_bytes(self):
        self.assertEqual(len(Q(l, {"chromosome": b'chr1', 'start pos': 114372214, 'end pos': 114372214})), 1)

    def test_float(self):
        res = Q(l, {"quality__gte":133.47, "quality__lt":142.39})
        self.assertEqual(len(res), 1)

    def test_decimal(self):
        res = Q(l, {"quality__gte":Decimal(133.47), "quality__lte":Decimal(142.39)})
        self.assertEqual(len(res), 1)


if __name__ == '__main__':
    unittest.main()

