import unittest
from Test_Case.RC import RC_login_resolution


def return_suite():
    """ 组装并返回 登录模块的测试套件

    :return: 测试套件
    """
    # 创建一个测试套件对象
    suite = unittest.TestSuite()
    # 创建一个加载器对象
    loader = unittest.TestLoader()

    # 通过加载器将测试用例加载到测试套件中
    #suite.addTests(loader.loadTestsFromTestCase(login_test_resolve.Auto_Test))
    #suite.addTests(loader.loadTestsFromTestCase(login_test_resolve_channel.Auto_Test))
    suite.addTests(loader.loadTestsFromTestCase(RC_login_resolution.Auto_Test))
    #suite.addTests(loader.loadTestsFromTestCase(login_test_resolution_portal.Auto_Test))

    # 返回组装好的测试套件
    return suite
