import json

def Add_unit():

    try:
        with open("units.json", "r") as file:
            units = json.load(file)
    except:
        units = {}

    name = input("Unit Name: ")

    unit = {
        "M": int(input("M: ")),
        "T": int(input("T: ")),
        "SV": int(input("SV: ")),
        "W": int(input("W: ")),
        "LD": int(input("LD: ")),
        "OC": int(input("OC: ")),
        "Weapons":{
            input("Weapon name: "):{
                "A": int(input("A: ")),
                "BS": int(input("BS: ")),
                "S": int(input("S: ")),
                "D": int(input("D: ")),
                "AP": int(input("AP: "))
            }
        }
    }

    units[name] = unit

    with open("units.json", "w") as file:
        json.dump(units, file, indent=4)
