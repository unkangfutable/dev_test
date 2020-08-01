import pytest


class Test:
    def test_one(self):
        print("开始执行1")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("开始执行2")
        x = "this"
        assert "s" in x


if __name__ == '__main__':
    # pytest.main("-v -x Test")
    pytest.main()