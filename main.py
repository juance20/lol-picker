import pyautogui
import time
import art
import os

def click_accept_button():
    accept_button_location = None

    print("Esperando partida...")

    while accept_button_location == None:
        accept_button_location = pyautogui.locateOnScreen("./images/accept.png", confidence = 0.7)
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
        selecting = pyautogui.locateOnScreen("./images/select.png", confidence = 0.7)
        time.sleep(1)

    pyautogui.moveTo(center[0],center[1], 0)

    while champ_location == None:
        champ_location = pyautogui.locateOnScreen("./champs/" + champ + ".png", confidence = 0.7)
        if champ_location == None:
            pyautogui.scroll(-100)
        time.sleep(1)

    pyautogui.click(pyautogui.center(champ_location))
    button = pyautogui.locateOnScreen("./images/select_button.png", confidence = 0.7)
    time.sleep(1)
    pyautogui.click(pyautogui.center(button))

def ban_champ(champ):
    center = [0,0]

    center[0], center[1] = pyautogui.size()
    center[0] = center[0] / 2
    center[1] = center[1] / 2

    selecting = None
    champ_location = None

    while selecting == None:
        selecting = pyautogui.locateOnScreen("./images/ban.png", confidence = 0.7)
        time.sleep(1)

    pyautogui.moveTo(center[0],center[1], 0)

    while champ_location == None:
        champ_location = pyautogui.locateOnScreen("./champs/" + champ + ".png", confidence = 0.7)
        if champ_location == None:
            pyautogui.scroll(-100)
        time.sleep(1)

    pyautogui.click(pyautogui.center(champ_location))
    time.sleep(1)
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("./images/ban_button.png", confidence = 0.7)))

def verify_pos():
    Top = None
    Mid = None
    Jgl = None
    Sup = None
    Adc = None

    while Top == None and Mid == None and Jgl == None and Sup == None and Adc == None:
        
        Top = pyautogui.locateOnScreen("./images/top.png", confidence = 0.9)
        #Mid = pyautogui.locateOnScreen("./images/mid.png", confidence = 0.9)
        #Jgl = pyautogui.locateOnScreen("./images/jgl.png", confidence = 0.9)
        Sup = pyautogui.locateOnScreen("./images/sup.png", confidence = 0.9)
        Adc = pyautogui.locateOnScreen("./images/adc.png", confidence = 0.9)

        time.sleep(1)
    
    if Top != None:
        return "top"

    elif Mid != None:
        return "mid"

    elif Jgl != None:
        return "jgl"

    elif Sup != None:
        return "sup"

    elif Adc != None:
        return "adc"

os.system("cls")

print(art.text2art("Gordo LoL Time"))

pos_1 = input("Ingresar posición principal: ").lower()
champ_1 = input("Ingresar campeon principal: ").lower()
ban_1 = input("Ingrese baneo principal: ").lower()

pos_2 = input("Ingresar posición secundaria: ").lower()
champ_2 = input("Ingresar campeon secundario: ").lower()
ban_2 = input("Ingrese baneo secundario: ").lower()

principal = {"pos":pos_1, "champ":champ_1, "ban":ban_1}
secundario = {"pos":pos_2, "champ":champ_2, "ban":ban_2}

click_accept_button()

print("Buscando posición...")
pos = verify_pos()
print(f"Posición encontrada: {pos}")

if pos == principal["pos"]:
    champ, ban = principal["champ"], principal["ban"]
else:
    champ, ban = secundario["champ"], secundario["ban"]

print(f"Champ: {champ}")
print(f"Ban: {ban}")

ban_champ(ban)
select_champ(champ)