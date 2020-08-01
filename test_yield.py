import pytest
import allure

def add(x, y):
    return x + y


def test_add():
    print("测试加法")
    assert add(1, 2) == 3


class TestDemo:
    # 同一模块中加入yield关键字,第一次调用返回结果,第二次调用执行yield后面的代码
    # scope 是作用域的意思,此处代表在该模块中使用,不指定时默认为function,在该方法中使用
    @pytest.fixture(scope="module")
    def open(self):
        print("打开浏览器")
        yield

        print("执行teardown,关闭浏览器")

    def test_one(self, open):
        print("测试方法1")
        x = "this"
        assert "i" in x

    def test_two(self, ):
        print("测试方法2")
        x = "this"
        assert 'x' in x

    def test_three(self, open):
        print("测试方法3")
        x = "this"
        assert 'i' in x


if __name__ == '__main__':
    pytest.main()
