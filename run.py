# coding=utf-8
import unittest
import time
from BeautifulReport import BeautifulReport
import threading
import Module.globalassertion


def main():
    time.sleep(5)
    name = '测试报告' + time.strftime("%Y%m%d%H%M%S", time.localtime())
    suite_tests = unittest.defaultTestLoader.discover(".", pattern="test_*.py", top_level_dir=None)
    BeautifulReport(suite_tests).report(filename=name, description="测试报告", report_dir="./")


if __name__ == "__main__":
    main_th = threading.Thread(target=main, args=())
    # assertion_th = threading.Thread(target=Module.globalassertion.run, args=())

    main_th.start()
    # assertion_th.start()
