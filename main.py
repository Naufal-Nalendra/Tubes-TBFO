from lib.CFGtoCNF import convert_list_to_dict
from lib.CFGtoCNF import convert_grammar
from lib.CFGtoCNF import read_grammar
from lib.operatorsplit import *

keygram = {"break" : "a", "const" : "b", "case" : "c", "catch" : "d", "continue" : "e", "default" : "f", "delete" : "g", "else" : "h", "false" : "i", "finally" : "j", "for" : "k", "function" : "l", "if" : "m", "let" : "n", "null" : "o", "return" : "p", "switch" : "q", "throw" : "r", "try" : "s", "true" : "t", "var" : "u", "while" : "v"}

def checkFA(input):
    res1 = input.split('\n')
    new = ""
    for res2 in res1:
        res = []
        open1 = True
        open2 = True
        newLine = True
        newLineActive = True
        res2 = res2.translate({ord(":"): " : "})
        res2 = res2.translate({ord("("): " ( "})
        res2 = res2.translate({ord(")"): " ) "})
        res2 = res2.translate({ord("["): " [ "})
        res2 = res2.translate({ord("]"): " ] "})
        res2 = res2.translate({ord('"'): ' """ '})
        res2 = res2.translate({ord('\''): ' """ '})
        res2 = res2.translate({ord(','): ' , '})
        res2 = res2.translate({ord('+'): ' + '})
        res2 = res2.translate({ord('-'): ' - '})
        res2 = res2.translate({ord('/'): ' / '})
        res2 = res2.translate({ord('%'): ' % '})
        res2 = res2.translate({ord('*'): ' * '})
        res2 = res2.translate({ord('^'): ' ^ '})
        res2 = res2.translate({ord('!'): ' ! '})
        res3 = res2.split()
        res = res3
        for i in range(len(res)):
            if(res[i] == "\n"):
                new += "\n"
                continue
            if(len(res[i]) == 1 and open2):
                j = ord(res[i])
                if(j == 95 or (j > 64 and j < 91) or (j > 96 and j < 123) and open1):
                    new += "x"
                    newLine = False
                elif(j > 47 and j < 58 and open1):
                    new += "y"
                    newLine = False
                elif(open1):
                    new += res[i]
                    newLine = False
            elif(open1):
                if(res[i] in keygram and open2):
                    new += keygram.get(res[i])
                    newLine = False
                elif(res[i] == "**" or res[i] == "==" and open2):
                    new += res[i]
                    newLine = False
                elif(res[i] == '"""' or res[i] == '\''):
                    if(open2):
                        open2 = False
                        if(newLine):
                            new += "x=x"
                            newLine = False
                            newLineActive = False
                        else:
                            new == "+x"
                    else:
                        open2 = True
                        if(newLineActive):
                            new += "x"
                        else:
                            new += "+x"
                elif(open2):
                    benar = True
                    first = True
                    angka = True
                    cekAngka = True
                    for b in res[i]:
                        j = ord(b)
                   
                        if(b == "(" or b == ")" or b == "[" or b == "]"):
                            new += b
                            newLine = False
                        elif(first and benar):
                            if(j != 95 and (j <= 64 or j >= 91) and (j <= 96 or j >= 123) and (j <= 47 or j >= 58)):
                                benar = False
                                first = False
                                angka = False
                                cekAngka = False
                                new += "R"
                                newLine = False
                            else:
                                if(j > 47 and j < 58):
                                    first = False
                                    continue
                                else:
                                    first = False
                                    cekAngka = False
                        if(cekAngka):
                            if(j <= 47 or j >= 58):
                                cekAngka = False
                               
                                benar = False
                                angka = False
                        if(benar and not first and not cekAngka):
                            if((j > 47 and j < 58)):
                                continue
                            else: 
                                angka = False
                                if(j != 95 and (j <= 64 or j >= 91) and (j <= 96 or j >= 123)):
                                 
                                    benar = False
                    if(angka or cekAngka):
                        new += "y"
                        newLine = False
                    elif(benar):
                        new += "x"
                        newLine = False
                    elif(not benar and not first and not angka):
                        new += "R"
                        newLine = False
        new += "\n"
    return (new)

if __name__ == "__main__":
    print()
    print("     ____.                                       .__        __    _________                       .__.__                ")
    print("    |    |____ ___  _______    ______ ___________|__|______/  |_  \_   ___ \  ____   _____ ______ |__|  |   ___________ ")
    print("    |    \__  \\  \/ /\__  \  /  ___// ___\_  __ \  \____ \   __\ /    \  \/ /  _ \ /     \\____ \|  |  | _/ __ \_  __ \ ")
    print("/\__|    |/ __ \\   /  / __ \_\___ \\  \___|  | \/  |  |_> >  |   \     \___(  <_> )  Y Y  \  |_> >  |  |_\  ___/|  | \/")
    print("\________(____  /\_/  (____  /____  >\___  >__|  |__|   __/|__|    \______  /\____/|__|_|  /   __/|__|____/\___  >__|   ")
    print("              \/           \/     \/     \/         |__|                  \/             \/|__|                \/       ")
    print("\n")

    CNF = convert_list_to_dict(convert_grammar(read_grammar(r'data\cfg.txt')))
    file = input("Masukkan nama file: ")
    fileName = (r"test\{}".format(file))

    output, valid = splitOperator(fileName)
    # f = open(fileName, 'r')
    # g = f.read()
    # print(g)
    n = len(output)
    dp = [[set([]) for i in range(n)] for j in range(n)]

    for i in range(n):
        for var in CNF.items():
                for termin in var[1]:
                    if len(termin) == 1 and termin[0] == output[i]:
                        dp[i][i].add(var[0])

    for l in range(2,n+1):
        for i in range (0,n-l+1):
            j = i+l-1
            for k in range (i,j):
                for var in CNF.items():
                    for prod in var[1] :
                        if len(prod) == 2 :
                            if(prod[0] in dp[i][k]) and (prod[1] in dp[k+1][j]):
                                dp[i][j].add(var[0])
    if "START" in dp[0][n-1] :
        print("Accepted")
    else :
        print("Syntax Error")