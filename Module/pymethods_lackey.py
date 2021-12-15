# coding=utf-8
import lackey
import random
import win32com.client


class method_lackey(object):
    def __init__(self):
        pass

    def leftclick(self, path):
        r = lackey.Screen(0)
        r.hover(lackey.Pattern(target=path))
        r.click()

    def rightclick(self, path):
        r = lackey.Screen(0)
        r.hover(lackey.Pattern(target=path))
        r.rightClick()

    def doubleclick(self, path):
        r = lackey.Screen(0)
        r.hover(lackey.Pattern(target=path))
        r.doubleClick()

    def ifexit(self, target):
        s = lackey.Region(57, 0).setSize(w=252, h=1036)
        # r.exists(lackey.Pattern(target=target).similar(0.9))
        s.hover(lackey.Pattern(target=target))

    def ifexit2(self, target):
        s = lackey.Region(57, 0).setSize(w=252, h=1036)
        s.exists(lackey.Pattern(target=target).similar(0.95))

    def CheckProcExistByPN(self):
        try:
            WMI = win32com.client.GetObject('winmgmts:')
            processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="chrome.exe"')
        except Exception as e:
            print("error : ", e)
        if len(processCodeCov) > 0:
            # print name + " exist"
            return 1
        else:
            # print name + " is not exist"
            return 0

    def shortname(self):
        list = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z')
        a = random.randint(0, 25)
        b = random.randint(0, 25)
        c = random.randint(0, 25)
        return list[a]+list[b]+list[c]