# coding = utf-8
import os
import lackey


def globalassertion():
    filepath = "./globalassertion"
    name = os.listdir(filepath)
    Reg = lackey.Region(0, 0).setSize(1920, 1080)
    for i in name:
        try:
            Reg.find("./globalassertion/%s" % i)
            return 1
        except:
            pass
    return 2


def run():
    while True:
        assert globalassertion() == 2
