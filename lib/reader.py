import string
def enumerateFunction():
    with open('./data/functions.txt', 'r') as f:
        lines = f.read()
    func = lines.split('\n')
    enum = dict(zip(func, [chr(ord('A')+i) for i in range(len(func))]))
    return enum



def read(filepath: str):
    f = open(filepath, 'r')
    w = f.read()
    lowCase = string.ascii_lowercase
    uppCase = string.ascii_uppercase
    dig = string.digits
    res = ""
    funct = enumerateFunction()

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
        elif(w[0] == '//'):
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
        elif(w[0] not in (lowCase+uppCase+dig+'_')):
            res += w[0]
        else:
            if(w[0] not in (lowCase+uppCase+'_')):
                # n is for integer and float
                # x is for invalid variable
                if(w[0] in dig):
                    tmp = w
                    w = w[1:]
                    while(w):
                        if(w[0] not in dig):
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
                            if(w[0] not in dig):
                                break
                            tmp = w
                            w = w[1:]
                        if(not w):
                            res += 'n'
                            break
                        if(w[0] in (lowCase+uppCase+'_')):
                            tmp = w
                            w = w[1:]
                            while(w):
                                if(w[0] not in (lowCase+uppCase+'_'+dig)):
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
                        
                    elif(w[0] in (lowCase+uppCase+'_')):
                        tmp = w
                        w = w[1:]
                        while(w):
                            if(w[0] not in (lowCase+uppCase+'_'+dig)):
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
                        if(w[0] not in dig):
                            break
                        tmp = w
                        w = w[1:]
                    if(not w):
                        res += 'n'
                        break
                    if(w[0] in (lowCase+uppCase+'_')):
                        tmp = w
                        w = w[1:]
                        while(w):
                            if(w[0] not in (lowCase+uppCase+'_'+dig)):
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
                    if(w[0] not in (lowCase+uppCase+dig+'_')):
                        break
                    else:
                        cur += w[0]
                    tmp = w
                    w = w[1:]
                if(cur in funct):
                    if(w):
                        res += funct[cur]
                        w = tmp
                    else:
                        res += funct[cur]
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
