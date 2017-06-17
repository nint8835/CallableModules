import DefaultTestModule
import CustomNameTestModule


def test_callable_with_default_name():
    assert DefaultTestModule()

def test_callable_with_custom_name():
    assert CustomNameTestModule()

def test_access_attribute_of_default_module():
    assert DefaultTestModule.test

def test_access_attribute_of_custom_module():
    assert CustomNameTestModule.test