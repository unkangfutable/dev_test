import pytest


def add(x, y):
    return x + y


def test_add():
    print("测试加法")
    assert add(1, 2) == 3


class TestDemo:
    # 同一模块中加入yield关键字,第一次调用返回结果,第二次调用执行yield后面的代码

    def test_one(self, login):
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

    def test_three(self,logout):
        print("测试方法3")
        x = "this"
        assert 'i' in x


if __name__ == '__main__':
    pytest.main()
