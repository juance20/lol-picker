import pyautogui
import time
import art
import os
import keyboard
from presets_tools import *

def click_accept_button():
    accept_button_location = None

    print("Esperando partida...")

    while accept_button_location == None:
        try:
            accept_button_location = pyautogui.locateOnScreen("./images/accept.png", confidence = 0.7)
            time.sleep(1)
        except:
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
        try:
            selecting = pyautogui.locateOnScreen("./images/select.png", confidence = 0.7)
            time.sleep(1)
        except:
            time.sleep(1)

    pyautogui.moveTo(center[0],center[1], 0)

    while champ_location == None:
        try:
            champ_location = pyautogui.locateOnScreen("./champs/" + champ + ".png", confidence = 0.7)
        except:
            pass
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
        try:
            selecting = pyautogui.locateOnScreen("./images/ban.png", confidence = 0.7)
            time.sleep(1)
        except:
            time.sleep(1)

    pyautogui.moveTo(center[0],center[1], 0)

    while champ_location == None:
        try:
            champ_location = pyautogui.locateOnScreen("./champs/" + champ + ".png", confidence = 0.7)
        except:
            pass
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
        try:
            Top = pyautogui.locateOnScreen("./images/top.png", confidence = 0.7)
            #Mid = pyautogui.locateOnScreen("./images/mid.png", confidence = 0.7)
            #Jgl = pyautogui.locateOnScreen("./images/jgl.png", confidence = 0.7)
            Sup = pyautogui.locateOnScreen("./images/sup.png", confidence = 0.7)
            Adc = pyautogui.locateOnScreen("./images/adc.png", confidence = 0.7)
        except:
            pass
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

def main(mode="restart"):
    if mode == "select":
        iniciar = False
        while not iniciar:
            os.system("cls")

            print(art.text2art("Gordo LoL Time"))

            print("1. Ingresar datos")
            print("2. Usar preset")
            print("3. Crear preset")
            print("4. Eliminar preset")
            print("5. Mostrar presets")

            match int(input("Ingrese opción: ")):
                case 1:
                    principal, secundario = inputs()
                    iniciar = True
                case 2:                
                    principal, secundario, id = select_preset()
                    if id == -1:
                        input("Presione ENTER para continuar")
                    else:
                        iniciar = True
                case 3:
                    crear_preset()
                case 4:
                    _, _, id = select_preset()
                    if id != -1:
                        delete_preset(id)
                    else:
                        input("Presione ENTER para continuar")
                case 5:
                    print_presets()
                    input("Presione ENTER para continuar")

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

keyboard.add_hotkey("ctrl + j", main)

main(mode="select")