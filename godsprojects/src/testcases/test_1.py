# -*- encoding=utf-8 -*-
import pytest # 引入pytest包
print("222222222266666222")

x = 1

def  ccc():
    global  x
    x= 3
    print(x)

ccc()
print(x)


def test_a(): # test开头的测试函数
    print("------->test_a")
    #assert 1 # 断言成功
def test_b():
    print("------->test_b")
    #assert 0 # 断言失败

if __name__ == '__main__':
       pytest.main(["-s","test_1.py"]) # 调用pytest的main函数执行测试