import pytest



@pytest.fixture()
def login():
    print("调用login函数")

# 用例中传入此函数名则是调用该函数
@pytest.fixture()
def logout():
    print("调用注销函数")

def pytest_configure(config):
    marker_list = ["login"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers",markers
        )