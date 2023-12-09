import json
import os

def inputs():
    pos_1 = input("Ingresar posición principal: ").lower()
    champ_1 = input("Ingresar campeon principal: ").lower()
    ban_1 = input("Ingrese baneo principal: ").lower()

    pos_2 = input("Ingresar posición secundaria: ").lower()
    champ_2 = input("Ingresar campeon secundario: ").lower()
    ban_2 = input("Ingrese baneo secundario: ").lower()

    return {"pos":pos_1, "champ":champ_1, "ban":ban_1}, {"pos":pos_2, "champ":champ_2, "ban":ban_2}

def select_preset():
    with open("presets.json", "r") as file:
        data = json.load(file)

    if len(data) == 0:
        print("No hay presets")
        return 1
    
    os.system("cls")

    for preset in data:
        print(f"Preset id: {data.index(preset)}")
        print(f"Pos principal: {preset['pos']}")
        print(f"Champ principal: {preset['champ']}")
        print(f"Ban principal: {preset['ban']}")
        print(f"Pos secundario: {preset['pos2']}")
        print(f"Champ secundario: {preset['champ2']}")
        print(f"Ban secundario: {preset['ban2']}")
        print("--------------------------------")

    id = int(input("Ingrese el id del preset: "))
    preset = data[id]
    return {"pos": preset["pos"], "champ": preset["champ"], "ban":preset["ban"]}, {"pos": preset["pos2"], "champ": preset["champ2"], "ban":preset["ban2"]}, id

def crear_preset():

    principal, secundario = inputs()    

    new = {"pos":principal["pos"],
           "champ":principal["champ"], 
           "ban":principal["ban"], 
           "pos2":secundario["pos"], 
           "champ2":secundario["champ"], 
           "ban2":secundario["ban"]}

    with open("presets.json", "r+") as file:
        file_data = json.load(file)
        file_data.append(new)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def delete_preset(id):
    with open("presets.json", "r+") as file:
        file_data = json.load(file)
        file_data.pop(id)

    with open("presets.json", "w") as file:
        json.dump(file_data, file, indent=4)

def print_presets():
    with open("presets.json", "r") as file:
        data = json.load(file)

    if len(data) == 0:
        print("No hay presets")
        return 1
    
    os.system("cls")

    for preset in data:
        print(f"Preset id: {data.index(preset)}")
        print(f"Pos principal: {preset['pos']}")
        print(f"Champ principal: {preset['champ']}")
        print(f"Ban principal: {preset['ban']}")
        print(f"Pos secundario: {preset['pos2']}")
        print(f"Champ secundario: {preset['champ2']}")
        print(f"Ban secundario: {preset['ban2']}")
        print("--------------------------------")