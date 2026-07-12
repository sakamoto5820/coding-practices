"""問13 add_commas のテスト。"""

from solutions import add_commas


class TestQ13AddCommas:
    def test_examples(self):
        assert add_commas("1234567") == "1,234,567"
        assert add_commas("-1234567.891") == "-1,234,567.891"
        assert add_commas("100") == "100"
        assert add_commas("-0.5") == "-0.5"
        assert add_commas("1000000") == "1,000,000"

    def test_additional(self):
        assert add_commas("1000") == "1,000"
        assert add_commas("999") == "999"
        assert add_commas("+12345") == "+12,345"
        assert add_commas("0.123456") == "0.123456"  # 小数部は区切らない
        assert add_commas("1234.5678") == "1,234.5678"
        assert add_commas("1") == "1"
