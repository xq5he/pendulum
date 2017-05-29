from pendulum import Period, DateTime

from .. import AbstractTestCase


class ArithmeticTestCase(AbstractTestCase):

    def test_multiply(self):
        dt1 = DateTime(2016, 8, 7, 12, 34, 56)
        dt2 = dt1.add(days=6, seconds=34)
        it = Period(dt1, dt2)
        mul = it * 2
        self.assertIsInstanceOfDuration(mul)
        self.assertDuration(mul, 1, 5, 0, 1, 8)

        dt1 = DateTime(2016, 8, 7, 12, 34, 56)
        dt2 = dt1.add(days=6, seconds=34)
        it = Period(dt1, dt2)
        mul = it * 2
        self.assertIsInstanceOfDuration(mul)
        self.assertDuration(mul, 1, 5, 0, 1, 8)

    def test_divide(self):
        dt1 = DateTime(2016, 8, 7, 12, 34, 56)
        dt2 = dt1.add(days=2, seconds=34)
        it = Period(dt1, dt2)
        mul = it / 2
        self.assertIsInstanceOfDuration(mul)
        self.assertDuration(mul, 0, 1, 0, 0, 17)

        dt1 = DateTime(2016, 8, 7, 12, 34, 56)
        dt2 = dt1.add(days=2, seconds=35)
        it = Period(dt1, dt2)
        mul = it / 2
        self.assertIsInstanceOfDuration(mul)
        self.assertDuration(mul, 0, 1, 0, 0, 17)

    def test_floor_divide(self):
        dt1 = DateTime(2016, 8, 7, 12, 34, 56)
        dt2 = dt1.add(days=2, seconds=34)
        it = Period(dt1, dt2)
        mul = it // 2
        self.assertIsInstanceOfDuration(mul)
        self.assertDuration(mul, 0, 1, 0, 0, 17)

        dt1 = DateTime(2016, 8, 7, 12, 34, 56)
        dt2 = dt1.add(days=2, seconds=35)
        it = Period(dt1, dt2)
        mul = it // 3
        self.assertIsInstanceOfDuration(mul)
        self.assertDuration(mul, 0, 0, 16, 0, 11)
