import json
from tkinter.filedialog import askopenfilename
import time


# FUNZT !!
# ______________________________________________________________________________________
# searchString = "RessGruppe"
# result = {}

# with open ("gmbh_ressource.json", "r", encoding="utf-8") as readFile:
#     with open("newArrangedRessource.json", "w", encoding="utf-8") as writeFile:
#         data = json.load(readFile)       

#         for item in data:
#             if searchString in item:
#                 key_value = item[searchString]

#                 if key_value in result:
#                     result[key_value].append(item)
#                 else:
#                     result[key_value] = [item]
#         json.dump(result, writeFile, indent=True, ensure_ascii=False)

#______________________________________________________________________________________


# Nur als Admin ausgeführt ausführbar!
# GLOBALS
searchString = ""
def welcome():
    print("""\ 
        
  _______                                  _____                       
 |___  (_)                                / ____|                      
    / / _ _ __ ___  _ __ ___   ___ _ __  | |  __ _ __ ___  _   _ _ __  
   / / | | '_ ` _ \| '_ ` _ \ / _ \ '__| | | |_ | '__/ _ \| | | | '_ \ 
  / /__| | | | | | | | | | | |  __/ |    | |__| | | | (_) | |_| | |_) |
 /_____|_|_| |_| |_|_| |_| |_|\___|_|     \_____|_|  \___/ \__,_| .__/ 
                                                                | |    
                                                                |_|    

    """)
    #global searchString 
    print(f'+{"-"*28}+')
    print(f'|{" "*28}|')
    print(f'|{"JSON Sorter":^28}|')
    print(f'|{"Type in key to sort":^28}|')
    print(f'|{" "*28}|')
    print(f'|{" ":<28}|')
    print(f'|{"STRG + C to quit":^28}|')
    print(f'|{" "*28}|')
    print(f'+{"-"*28}+')
    
   # searchString = input("JSON-key to sort after: ")


def giveFileName(filePath):
    indexOfFile = filePath.rfind("/")
    fileName = filePath[indexOfFile:]
    filePath = filePath[:indexOfFile]
    cutToRename = fileName.rfind(".")
    print(filePath + fileName[:cutToRename] + "_sorted" + ".json")

    return filePath + fileName[:cutToRename] + "_sorted" + ".json"


def sorter(jsonObj):
    result = {}
    for item in jsonObj:
        if searchString in item:
            key_value = item[searchString]

            if key_value in result:
                result[key_value].append(item)
            else:
                result[key_value] = [item]
    print("\nDone!\n\nWriting in file...")
    return result


def fileHandler():
    global searchString
    print("\nSelect a .json file to sort....\n")
    time.sleep(1)
    file = askopenfilename()

    with open(file, "r", encoding="utf-8") as readFile:
        with open(giveFileName(file), "w", encoding="utf-8") as writeFile:
            
            rFile = json.load(readFile)
            print("Possible sorting keys:\n")
            for k, v in rFile[0].items():
                print(k)

            searchString = input("\nJSON-key to sort after: ")
            #data = json.load(readFile)
            sortedJson = sorter(rFile)
            json.dump(sortedJson, writeFile, indent=True, ensure_ascii=False)
            time.sleep(5)


def main():
    welcome()
    fileHandler()

if __name__ == "__main__":
    main()