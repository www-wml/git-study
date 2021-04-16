import pytest
class Test_Demo6():
    @pytest.mark.demo
    def test_Demo6(self):
        a = 5
        b = -1
        assert a != b
    print("我的第⼀个测试⽤例")
    @pytest.mark.smoke
    def test_two(self):
        a = 2
        b = -1
        assert a != b
        print("我的第⼆个测试⽤例")