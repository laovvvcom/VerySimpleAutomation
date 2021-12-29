# coding = utf-8
from Module.pymethods_lackey import method_lackey
from Module.pymethods_autogui import method_autogui
import unittest
import lackey
import pyautogui
import time
import os
from ddt import ddt, data, unpack
from xlrd import open_workbook

# 自动化保护措施，鼠标置顶左上角暂停自动化
pyautogui.FAILSAFE = True


def getExcelTestData():
    openExcelFile = open_workbook("./ExcelTestData.xlsx")
    getSheet = openExcelFile.sheet_by_name("Sheet1")
    rowNumber = getSheet.nrows
    dataList = []
    for i in range(1, rowNumber):
        dataList.append(getSheet.row_values(i))
    return dataList


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("==========开始测试==========")

    def tearDown(self):
        print("==========结束测试==========")

    @data(*getExcelTestData())
    # @data(["公式测试计划", 1])
    @unpack
    def test_case(self, case, *content):
        try:
            img_list = os.listdir("./action/case%s" % (content[0]))
            dir_list = sorted(img_list,
                              key=lambda x: os.path.getmtime(os.path.join("./action/case%s", x) % (content[0])))
            t = int(content[3])
            casenum = 3
            while casenum <= 10004:
                for i in dir_list:
                    ni = i.split(".")[0]
                    if ni.isdigit():
                        method_lackey().leftclick("./action/case%s/%s.png" % (content[0], ni))
                        time.sleep(t)
                        continue
                    elif ni.islower():
                        casenum += 1
                        method_lackey().leftclick("./action/case%s/%s.png" % (content[0], ni))
                        time.sleep(t)
                        method_autogui().copy(content[casenum])
                        time.sleep(t)
                        continue
                    else:
                        r = lackey.Screen()
                        self.assertTrue(
                            r.exists(lackey.Pattern(target="./expectation/case%s/1.png" % content[1]).similar(0.85)))
                        self.assertTrue(
                            r.exists(
                                lackey.Pattern(target="./expectation/case%s/%s.png" % (content[1], content[2])).similar(
                                    0.85)))
                break

        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()
