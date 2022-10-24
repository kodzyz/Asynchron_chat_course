import unittest


def sum_kv_ij(i, j):
    return i * i + j * j


class TestSumKv(unittest.TestCase):
    def setUp(self):
        print('Подготовка к запуску теста')

    def tearDown(self):
        print('Тест выполнен')

    def testnotequal(self):
        self.assertNotEqual(sum_kv_ij(2, 3), 23)

    def testequal(self):
        self.assertEqual(sum_kv_ij(2, 3), 13)


if __name__ == '__main__':
    unittest.main()

# python3 service.py
# Подготовка к запуску теста
# Тест выполнен
# Подготовка к запуску теста
# Тест выполнен
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
