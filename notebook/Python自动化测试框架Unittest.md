### Python自动化测试框架Unittest

#### Unittest 框架：

- test fixture

  ```python
  准备测试活动前的一些准备工作，或者执行测试活动的相关清理工作。如：接口测试需要登陆的情况
  def setUp(self):
      pass
  
  def tearDown(self):
      pass
  
  @classmethod
  def setUpClass(cls):
      pass
  
  @classmethod
  def tearDownClass(cls):
      pass
  ```

- test case

  ```python
  测试用例：是测试活动的最小单元，它用来检查特定的集合输入，是否达到了预期结果。
  unittest框架提供了一个测试类(TestCase)，可以让我们创建属于自己的测试用例。且测试方法以test开头
  class TestStringMethods(unittest.TestCase):
  
      def test_upper(self):
          self.assertEqual('foo'.upper(), 'FOO')
  ```

- test suite

  ```python
  测试套件：是测试用例或者测试套件的一个集合，常用于聚合执行测试用例
  suite = unittest.TestSuite()
  suite.addTest(TestStringMethods('test_isupper')) #参数有测试类以及 测试方法组成
  ```

- test runner

  ```python
  测试运行器：协调测试的执行并且给出执行结果，并通过图形/文本界面来显示测试的执行结果
  runner = unittest.TextTestRunner()
  runner.run(suite)
  ```

#### mock模块的使用

`模拟对象：主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为`

前后端联调/单元测试/第三方接口依赖

```python
def zhifu():
    '''假设这里是一个支付的功能,未开发完
    支付成功返回：{"result": "success", "reason":"null"}
    支付失败返回：{"result": "fail", "reason":"余额不足"}
    reason返回失败原因
    '''
    pass

def zhifu_statues():
    '''根据支付的结果success or fail，判断跳转到对应页面'''
    result = zhifu()
    print(result)
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            print("失败原因：%s" % result["reason"])
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常!"
    
#单元测试
from unittest import mock
import unittest
import temple

class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''
    def test_01(self):
        '''测试支付成功场景'''
        # mock一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    def test_02(self):
        '''测试支付失败场景'''
        # mock一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")

if __name__ == "__main__":
    unittest.main()
```

单元测试需要保证函数的每个分支都能测试到。

TDD的总体流程：

```python
首先编写一个测试，运行这个测试看着它失败。然后编写最少量的代码取得一些进展，再运行测试。
如此不断重复，直到测试通过为止。最后，或许还要重构代码，测试能确保不破坏任何功能。
```

