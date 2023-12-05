import pyautogui
import time

def click_accept_button():
    accept_button_location = None

    print("Esperando partida...")

    while accept_button_location == None:
        accept_button_location = pyautogui.locateOnScreen("accept.png", confidence = 0.7)
        time.sleep(1)
    
    print("Partida encontrada!")

    pyautogui.click(pyautogui.center(accept_button_location))

def select_champ(champ):
    center = [0,0]

    center[0], center[1] = pyautogui.size()
    center[0] = center[0] / 2
    center[1] = center[1] / 2

    selecting = None
    champ_location = None

    while selecting == None:
        selecting = pyautogui.locateOnScreen("select.png", confidence = 0.7)
        time.sleep(1)

    pyautogui.moveTo(center[0],center[1], 0)

    while champ_location == None:
        champ_location = pyautogui.locateOnScreen("./champs/" + champ + ".png", confidence = 0.7)
        pyautogui.scroll(-100)
        time.sleep(1)

    pyautogui.click(pyautogui.center(champ_location))
    time.sleep(1)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("select_button.png", confidence = 0.7)))

def ban_champ(champ):
    center = [0,0]

    center[0], center[1] = pyautogui.size()
    center[0] = center[0] / 2
    center[1] = center[1] / 2

    selecting = None
    champ_location = None

    while selecting == None:
        selecting = pyautogui.locateOnScreen("ban.png", confidence = 0.7)
        time.sleep(1)

    pyautogui.moveTo(center[0],center[1], 0)

    while champ_location == None:
        champ_location = pyautogui.locateOnScreen("./champs/" + champ + ".png", confidence = 0.7)
        pyautogui.scroll(-100)
        time.sleep(1)

    pyautogui.click(pyautogui.center(champ_location))
    time.sleep(1)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("ban_button.png", confidence = 0.7)))


click_accept_button()
select_champ("ekko")
ban_champ("ekko")
