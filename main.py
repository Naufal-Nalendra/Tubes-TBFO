from lib.CFGtoCNF import convert_list_to_dict
from lib.CFGtoCNF import convert_grammar
from lib.CFGtoCNF import read_grammar
from lib.CYKparser import CYKParser
from lib.reader import read
import sys
import os


def readFile(path):
    with open(path, "r") as file:
        content = file.read()
    return content

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
    CNF = convert_list_to_dict(convert_grammar(read_grammar(r'data\cfg.txt')))
    
    # masukkan input file yang diuji
    namaFile = input("Masukkan nama file yang akan diuji: ")

    # Check file exist
    while os.path.isfile(namaFile) == False:
        namaFile = input("File tidak ditemukan! Masukkan ulang nama file yang valid: ")

    # Input
    if (len(sys.argv) < 2):
        dir = "./test/"
        path = dir + namaFile
    else:
        path = sys.argv[1]

    try:
        inp = read(path)
    except Exception as e:
        print("Error:" + str(e))
        print("Menggunakan testcase default: 'inputAcc1.py'\n")
        try:
            path = "./test/inputAcc1.py"
            inp = read(path)
        except Exception as e:
            print("Error:" + str(e))
            print("Menutup program...\n")
            exit(0)

    # # Preprocess
    # inp = checkFiniteAutomata(inp)
    
    # Waiting message
    print("Compiling " + str(path) + "...\n")
    print("Menunggu hasil compile...\n")

    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%% RESULT %%%%%%%%%%%%%%%%%%%%%%%%%%")
    # Parse
    if (len(inp)==0):
        print("Accepted. No errors detected.")
    else :
        CYKParser(inp, CNF)
        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        exit(0)