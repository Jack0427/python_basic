"""
測試都是以class定義
每一個測試類都是unittest.TestCase的子類
測試類裡的方法 都必須以test_開頭
assert檢查預測跟實際結果
測試前使用setUp()定義測試規範跟臨時變量
測試後使用tearDown()清理銷毀臨時變量等測試環境
使用python -m unittest -v test_module測試
"""
import unittest
from demo.math import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        self.assertRaises(ValueError, add, 'a', 5)


if __name__ == "__main__":
    unittest.main()
