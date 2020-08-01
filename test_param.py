import pytest


def add(x, y):
    return x + y


@pytest.mark.skip("跳过加法测试")
def test_add():
    print("测试加法")
    assert add(1, 2) == 3


class TestDemo:
    # # 传递参数方式1: fixture中的params的每一个值,fixture都不调用运行一次
    # @pytest.fixture(params=[1, 2, 3])
    # def data(self, request):
    #     return request.param
    #
    # def test_one(self, data):
    #     print(f"获取测试数据{data}")
    #     assert data >= 2

    # 传递参数方式2 :遍历列表中的元祖,元祖中前一个对应input,后一个对应expected
    # @pytest.mark.parametrize("test_input,expected", [("1+1", 2), ("3+2", 4)])
    # def test_eval(self, test_input, expected):
    #     # eval 可将字符型公式转化为数字计算
    #     assert eval(test_input) == expected

    # 参数组合,每一个x和每一个y比较
    # @pytest.mark.parametrize("x", [1, 2, 3, 4])
    # @pytest.mark.parametrize("y", [4, 5])
    # # 三个
    # def test_fix(self, x, y):
    #     print(f"y是{y},x是{x}")
    #     assert y > x

    # 传参方式3: 方法名字做为参数
    @pytest.fixture(scope="module")
    @pytest.mark.login
    def login(self, request):
        name = request.param
        print(f"获取测试数据{name}")
        return name

    test_name = ["fkey", "nineo"]

    # 本次步骤完成给调用的登录函数传参;inderect = True 可以吧传过来的参数当函数执行,此处为"login"  如果不加函数login不会被调用
    @pytest.mark.parametrize("login", test_name, indirect=True)
    # 本次步骤调用登录函数
    def test_case(self, login):
        a = login
        print(f"登录函数获取{a}测试数据")
        assert a != ""


# def test_two(self, open):
#     print("测试方法2")
#     x = "this"
#     assert 'x' in x
#
# def test_three(self, open):
#     print("测试方法3")
#     x = "this"
#     assert 'i' in x


if __name__ == '__main__':
    pytest.main("-v")
