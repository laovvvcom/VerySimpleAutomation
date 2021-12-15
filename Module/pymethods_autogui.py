# coding=utf-8
import pyautogui
import pyperclip
import time


class method_autogui(object):
    def __init__(self):
        pass

    def moveto(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)

    def moverel(self, x, y):
        pyautogui.moveRel(x, y, 1, pyautogui.easeInQuad)

    def leftclick(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
        pyautogui.PAUSE = 0.5
        pyautogui.click(button='left')

    def leftclick_down(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
        pyautogui.PAUSE = 0.5
        pyautogui.mouseDown(button='left')

    def leftclick_up(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
        pyautogui.PAUSE = 0.5
        pyautogui.mouseUp(button='left')

    def rightclick(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
        pyautogui.PAUSE = 0.5
        pyautogui.click(button='right')

    def middleclick(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
        pyautogui.PAUSE = 0.5
        pyautogui.click(button='middle')

    def doubleclick(self, x, y):
        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
        pyautogui.PAUSE = 0.5
        pyautogui.doubleClick(button='left')

    def keydown(self, key):
        pyautogui.keyDown(key)

    def press(self, key):
        pyautogui.press(key)

    def keyup(self, key):
        pyautogui.keyUp(key)

    def hotkey(self, key1, key2):
        pyautogui.hotkey(key1, key2)

    def TBhotkey(self, key1, key2, key3):
        pyautogui.hotkey(key1, key2, key3)

    def copy(self,content):
        key1 = 'ctrl'
        key2 = 'v'
        pyperclip.copy(content)
        time.sleep(1)
        pyautogui.hotkey(key1, key2)

    def write(self, content):
        pyautogui.typewrite(content, 0.1)
        time.sleep(1)