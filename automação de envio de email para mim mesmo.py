
import pyautogui

import time

pyautogui.alert('Calma campeão, ta rodando a automação')

pyautogui.PAUSE = 0.5

pyautogui.press('winleft')

pyautogui.write('chrome')

pyautogui.press('enter')

pyautogui.write('https://mail.google.com/mail/u/0/#inbox?compose=new')

pyautogui.press('enter')

time.sleep(3)

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('enter')

pyautogui.write('victorfassini21@gmail.com')

pyautogui.press('enter')

pyautogui.press('tab')

pyautogui.write('Panqueca')

pyautogui.hotkey('ctrl','enter')

pyautogui.alert('Acabou a automação')