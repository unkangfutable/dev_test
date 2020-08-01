
import pytest


def add(x, y):
    return x + y


def test_add():
    print("测试加法")
    assert add(1, 2) == 3


class TestDemo:
    # autouse 为true时,所有用例自动使用fixture装饰的函数
    @pytest.fixture(autouse=True)
    def open(self):
        print("打开浏览器")
        yield

        print("执行teardown,关闭浏览器")
    def test_one(self,):
        print("测试方法1")
        x = "this"
        #
        # pytest.assume('o' in x)
        # pytest.assume(1 == 2)
        # pytest.assume('i ' in x)
        assert "i" in x

    def test_two(self):
        print("测试方法2")
        x = "this"
        assert 'x' in x

    def test_three(self):
        print("测试方法3")
        x = "this"
        assert 'i' in x


if __name__ == '__main__':
    pytest.main()
