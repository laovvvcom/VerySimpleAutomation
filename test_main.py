# coding = utf-8
from Module.pymethods_lackey import method_lackey
import unittest
import lackey
import pyautogui
import time
import pytesseract
from PIL import Image
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
    def test_case(self, case, *pathid):
        try:
            i = 0
            t = int(pathid[3])
            while True:
                i += 1
                res = pytesseract.image_to_string(Image.open("./action/case%s/%s.png" % (pathid[0], i)))
                if res != "The end":
                    method_lackey().leftclick("./action/case%s/%s.png" % (pathid[0], i))
                    time.sleep(t)
                else:
                    r = lackey.Screen()
                    self.assertTrue(
                        r.exists(lackey.Pattern(target="./expectation/case%s/1.png" % pathid[1]).similar(0.85)))
                    self.assertTrue(
                        r.exists(lackey.Pattern(target="./expectation/case%s/%s.png" % (pathid[1], pathid[2])).similar(0.85)))
                    break
        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()
