import pytest
import yaml


@pytest.mark.parametrize("a,b", yaml.safe_load(open("demo.yml")))
def test_add(a, b):
    print(f"测试{a}加{b}")
    assert a + b < 10

