from lib.CFGtoCNF import readCFG
from lib.CFGtoCNF import converter
from lib.CYKparser import CYKParser
from lib.reader import read
import sys
import os


def readFile(path):
    with open(path, "r") as file:
        isi = file.read()
    return isi

def ASCIIart():
    print()
    print("     ____.                                       .__        __    _________                       .__.__                ")
    print("    |    |____ ___  _______    ______ ___________|__|______/  |_  \_   ___ \  ____   _____ ______ |__|  |   ___________ ")
    print("    |    \__  \\  \/ /\__  \  /  ___// ___\_  __ \  \____ \   __\ /    \  \/ /  _ \ /     \\____ \|  |  | _/ __ \_  __ \ ")
    print("/\__|    |/ __ \\   /  / __ \_\___ \\  \___|  | \/  |  |_> >  |   \     \___(  <_> )  Y Y  \  |_> >  |  |_\  ___/|  | \/")
    print("\________(____  /\_/  (____  /____  >\___  >__|  |__|   __/|__|    \______  /\____/|__|_|  /   __/|__|____/\___  >__|   ")
    print("              \/           \/     \/     \/         |__|                  \/             \/|__|                \/       ")
    print("\n")

if __name__ == "__main__":
    ASCIIart()
    # fungsi baca grammar taruh disini
    CFG = readCFG("data\\cfg.txt")
    CNF = converter(CFG)
    
    # masukkan input file yang diuji
    fileName = input("Masukkan nama file yang akan diuji: ")

    # Check file exist
    while os.path.isfile(fileName) == False:
        fileName = input("File tidak ditemukan! Masukkan ulang nama file yang valid: ")

    # Input
    if (len(sys.argv) < 2):
        dir = "./test/"
        path = dir + fileName
    else:
        path = sys.argv[1]

    try:
        input = read(path)
    except Exception as e:
        print("Error:" + str(e))
        print("Menggunakan testcase default: 'inputAcc1.py'\n")
        try:
            path = "./test/inputAcc1.py"
            input = read(path)
        except Exception as e:
            print("Error:" + str(e))
            print("Menutup program...\n")
            exit(0)
    
    # Waiting message
    print("Compiling " + str(path) + "...\n")
    print("Menunggu hasil compile...\n")

    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%% RESULT %%%%%%%%%%%%%%%%%%%%%%%%%%")
    # Parse
    if (len(input)==0):
        print("Accepted. No errors detected.")
    else :
        CYKParser(input, CNF)
        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        exit(0)