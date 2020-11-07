"""
COMMAND LINE FILE MANAGER
@nandan-unni
Run in a terminal tab
"""

import os, sys, platform
import pdb

from utils.designer import logo, message, signal, clear, alert, warning
from utils.handlers import dirmenu, filemenu

OS = platform.system()
base_dir = os.path.dirname(os.path.abspath(__file__))
files = []
dirs = []
docs_count = 0

def title():
    logo("COMMAND LINE FILE MANAGER")
    message("CURRENT LOCATION : ")
    loc_list = base_dir.split(os.path.sep)
    loc_list.pop(0)
    if loc_list[len(loc_list) - 1] == "": loc_list.pop(len(loc_list) - 1)
    for loc in loc_list:
        print(loc, end="")
        signal("\b>>")

def errorhandler(msg = ""):
    title()
    alert(f"\n\n  {msg}\n")
    signal("\bPress Enter to continue _")
    input()

def dir_menu():
    title()
    message("\n  CURRENT DIRECTORY : ")
    loc_list = base_dir.split(os.path.sep)
    loc_list.pop(0)
    if loc_list[len(loc_list) - 1] == "":
        loc_list.pop(len(loc_list) - 1)
    print(loc_list[len(loc_list) - 1], "\n")
    message("FILES")
    dirmenu(files, 1)
    message("DIRECTORIES")
    dirmenu(dirs, len(files) + 1)
    message("TOOLS")
    dirmenu(['Rename Directory', 'Delete Directory', 'New Directory', 'Previous Directory', 'Exit'], docs_count + 1)
    choice = input("\t\t : ")
    return choice

def file_menu():
    message("\n  TOOLS")
    filemenu(['Rename', 'Delete', 'Back'])
    choice = input("\t\t : ")
    return choice

def createdir():
    title()
    signal("\n\n\n  New Directory name : ")
    newDir = input()
    newDir = os.path.join(base_dir, newDir)
    try:
        os.mkdir(newDir)
    except FileExistsError:
        errorhandler("A directory with same name already exists.")

def getdir(dir_name = ""):
    global base_dir, docs_count
    base_dir = os.path.join(base_dir, dir_name)
    dirs.clear()
    files.clear()
    for doc in os.listdir(base_dir):
        doc_path = os.path.join(base_dir, doc)
        if os.path.isfile(doc_path): files.append(doc)
        elif os.path.isdir(doc_path): dirs.append(doc)
        else: pass
    files.sort()
    dirs.sort()
    docs_count = len(files) + len(dirs)

def renamedir(dir_name = ""):
    global base_dir
    title()
    signal("\n\n\n  Current Name : ")
    print(dir_name)
    signal("\n  Enter new name : ")
    newName = input()
    title()
    signal("\n\n\n  Do you want to rename the directory")
    print(dir_name, end="")
    signal("to")
    print(newName, end="")
    signal("?")
    filemenu(['Yes', 'No'])
    choice = input("\t\t : ")
    if choice.isnumeric():
        if int(choice) == 1:
            try:
                dir_name = os.path.join(os.path.dirname(os.path.dirname(base_dir)), dir_name)
                newName = os.path.join(os.path.dirname(os.path.dirname(base_dir)), newName)
                base_dir = os.path.dirname(os.path.dirname(base_dir))
                os.rename(dir_name, newName)
            except FileExistsError:
                errorhandler("A directory with same name already exists.")

def deletedir(dir_name = ""):
    global base_dir
    title()
    signal("\n\n\n  Do you want to delete the directory")
    print(dir_name, end="")
    signal("?")
    filemenu(['Yes', 'No'])
    choice = input("\t\t : ")
    if choice.isnumeric():
        if int(choice) == 1:
            dir_name = os.path.join(base_dir, dir_name)
            base_dir = os.path.dirname(os.path.dirname(base_dir))
            os.rmdir(dir_name)

def getfile(file_name = ""):
    title()
    message("\n  CURRENT FILE : ")
    print(file_name)
    file_loc = os.path.join(base_dir, file_name)
    with open(file_loc) as file:
        data = file.read()
        print("\n\n\b\b", data, "\n")
    file.close()

def renamefile(file_name = ""):
    title()
    signal("\n\n\n  Current Name : ")
    print(file_name)
    signal("\n  Enter new name with extension : ")
    newName = input()
    title()
    signal("\n\n\n  Do you want to rename the file")
    print(file_name, end="")
    signal("to")
    print(newName, end="")
    signal("?")
    filemenu(['Yes', 'No'])
    choice = input("\t\t : ")
    if choice.isnumeric():
        if int(choice) == 1:
            try:
                file_name = os.path.join(base_dir, file_name)
                newName = os.path.join(base_dir, newName)
                os.rename(file_name, newName)
            except FileExistsError:
                errorhandler("A directory with same name already exists")

def deletefile(file_name = ""):
    title()
    signal("\n\n\n  Do you want to delete the file")
    print(file_name, end="")
    signal("?")
    filemenu(['Yes', 'No'])
    choice = input("\t\t : ")
    if choice.isnumeric():
        if int(choice) == 1:
            file_name = os.path.join(base_dir, file_name)
            os.remove(file_name)

def filemanager():
    global base_dir
    while True:
        getdir()
        choice = dir_menu()
        if choice.isnumeric(): choice = int(choice)
        else: continue
        if choice > len(files):
            if choice <= docs_count:
                getdir(dirs[choice - len(files) - 1])
                continue
            elif choice == docs_count + 1:
                loc_list = base_dir.split(os.path.sep)
                loc_list.pop(0)
                if loc_list[len(loc_list) - 1] == "":
                    loc_list.pop(len(loc_list) - 1)
                renamedir(loc_list[len(loc_list) - 1])
                continue
            elif choice == docs_count + 2:
                deletedir()
                continue
            elif choice == docs_count + 3:
                createdir()
                continue
            elif choice == docs_count + 4:
                base_dir = os.path.dirname(os.path.dirname(base_dir))
                getdir()
                continue
            elif choice == docs_count + 5: sys.exit()
            else:
                continue
        elif choice > 0 and choice <= len(files):
            getfile(files[choice - 1])
            file_choice = file_menu()
            if file_choice.isnumeric(): file_choice = int(file_choice)
            else: continue
            if file_choice == 1:
                renamefile(files[choice - 1])
                continue
            elif file_choice == 2:
                deletefile(files[choice - 1])
                continue
            else:
                getdir()
                continue
        else:
            continue


if __name__ == "__main__":
    while True:
        try:
            filemanager()
        except UnicodeDecodeError:
            errorhandler("File cannot be opened.")
            continue
        except FileNotFoundError:
            errorhandler("File not found.")
            continue
        except OSError:
            errorhandler("Some internal error occured.")
            continue
        except ModuleNotFoundError:
            title()
            alert("Refer README.md and install the dependencies.\n")
            break
        except KeyboardInterrupt:
            title()
            warning("\n\n\n  Closing File Manager...\n")
            break
