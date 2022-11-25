import string
def enumerateFunction():
    with open('./data/functions.txt', 'r') as f:
        lines = f.read()
    synatom = lines.split('\n')
    enum = dict(zip(synatom, [chr(ord('A')+i) for i in range(len(synatom))]))
    return enum



def read(filepath: str):
    f = open(filepath, 'r')
    w = f.read()
    alp = string.ascii_lowercase
    Alp = string.ascii_uppercase
    num = string.digits
    res = ""
    atom = enumerateFunction()

    while(w):
        # string processing
        if(w[0:3]=="\'\'\'"):
            nl = 0
            tmp = w[3:]
            while(tmp):
                if(tmp[0]=='\n'):
                    nl+=1
                if(tmp[0:3]=="\'\'\'"):
                    break
                tmp = tmp[1:]
            if(tmp):
                if(tmp[0:3]=="\'\'\'"):
                    for _ in range(nl):
                        res += 's\n'
                    res += 's'
                    w = tmp[2:]
        elif(w[0:3]=="\"\"\""):
            nl = 0
            tmp = w[3:]
            while(tmp):
                if(tmp[0]=='\n'):
                    nl+=1
                if(tmp[0:3]=="\"\"\""):
                    break
                tmp = tmp[1:]
            if(tmp):
                if(tmp[0:3]=="\"\"\""):
                    for _ in range(nl):
                        res += 's\n'
                    res += 's'
                    w = tmp[2:]
        elif(w[0]=='\"'):
            tmp = w[1:]
            while(tmp):
                if(tmp[0]=='\n' or tmp[0]=='\"'):
                    break
                tmp = tmp[1:]
            if(tmp):
                if(tmp[0]=='\n'):
                    res += w[0]
                else:
                    res += 's'
                    w = tmp
            else:
                res += w[0]
        elif(w[0]=='\''):
            tmp = w[1:]
            while(tmp):
                if(tmp[0]=='\n' or tmp[0]=='\''):
                    break
                tmp = tmp[1:]
            if(tmp):
                if(tmp[0]=='\n'):
                    res += w[0]
                else:
                    res += 's'
                    w = tmp
            else:
                res += w[0]    
        # cek comment
        elif(w[0] == '#'):
            tmp = w
            w = w[1:]
            while(w):
                if(w[0]=='\n'):
                    break
                tmp = w
                w = w[1:]
            if(not w):
                break
            else:
                w = tmp
        elif(w[0] not in (alp+Alp+num+'_')):
            res += w[0]
        else:
            if(w[0] not in (alp+Alp+'_')):
                # cek floating point dan integer kemudian disubstitusi menjadi 'n'
                # cek ada var tidak valid, kemudian di assign menjadi 'x'
                if(w[0] in num):
                    tmp = w
                    w = w[1:]
                    while(w):
                        if(w[0] not in num):
                            break
                        tmp = w
                        w = w[1:]
                    if(not w):
                        res += 'n'
                        break
                    if(w[0]=='.'):
                        tmp = w
                        w = w[1:]
                        while(w):
                            if(w[0] not in num):
                                break
                            tmp = w
                            w = w[1:]
                        if(not w):
                            res += 'n'
                            break
                        if(w[0] in (alp+Alp+'_')):
                            tmp = w
                            w = w[1:]
                            while(w):
                                if(w[0] not in (alp+Alp+'_'+num)):
                                    break
                                tmp = w
                                w = w[1:]
                            if(not w):
                                res += 'n.x'
                                break
                            w = tmp
                            res += 'n.x'
                        else:
                            res += 'n'
                            w = tmp
                        
                    elif(w[0] in (alp+Alp+'_')):
                        tmp = w
                        w = w[1:]
                        while(w):
                            if(w[0] not in (alp+Alp+'_'+num)):
                                break
                            tmp = w
                            w = w[1:]
                        if(not w):
                            res += 'x'
                            break
                        w = tmp
                        res += 'x'
                    else:
                        w = tmp
                        res += 'n'
                elif(w[0]=='.'):
                    tmp = w
                    w = w[1:]
                    while(w):
                        if(w[0] not in num):
                            break
                        tmp = w
                        w = w[1:]
                    if(not w):
                        res += 'n'
                        break
                    if(w[0] in (alp+Alp+'_')):
                        tmp = w
                        w = w[1:]
                        while(w):
                            if(w[0] not in (alp+Alp+'_'+num)):
                                break
                            tmp = w
                            w = w[1:]
                        if(not w):
                            res += 'x'
                            break
                        w = tmp
                        res += 'x'
                    else:
                        res += 'n'
            else:
                cur = w[0]
                tmp = w
                w = w[1:]
                while w:
                    if(w[0] not in (alp+Alp+num+'_')):
                        break
                    else:
                        cur += w[0]
                    tmp = w
                    w = w[1:]
                if(cur in atom):
                    if(w):
                        res += atom[cur]
                        w = tmp
                    else:
                        res += atom[cur]
                        w = tmp
                else:
                    if(w):
                        res += 'v'
                        w = tmp
                    else:
                        res+='v'
                        w = tmp
        tmp = w
        w = w[1:]
    return res.replace(" ", "")
