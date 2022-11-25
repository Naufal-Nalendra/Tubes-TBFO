import re
import finite_automata as fa

def splitOperator(filename):
    f = open(filename, "r")
    inputfile = f.read()
    f.close()

    output = []
    # split the target string on the occurance of one or more whitespace characters
    inputfile = inputfile.split(" ")
    for statement in inputfile:
        if statement != '':
            output.append(statement)

    operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'null', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'else if', 'else', 'while', 'function', 'break', 'continue', 'throw', 'return', '%', '\n']
    operator2 = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', '+', '*', '**', "'", '"', '(', ')', 'null', 'true', 'false', '{', '}', '[', ']', 'for', 'else if', 'else', 'while', 'break', 'continue', 'throw', 'function', 'return', '%', '\n']
    
    # split the target string with the following pattern
    for oper in operator:
        temp = []    
        for statement in output:
            elmt = re.split(r'[A..z]*(' + oper + r')[A..z]*', statement)
            
            for splitted in elmt:
                temp.append(splitted) 
        output = temp

    # checking list
    temp = []
    valid = True
    for statement in output:
        if statement in operator2:
            temp.append(statement)
        else:
            if statement == 'as' or statement == 'is' or statement == 'or' or statement == 'in' or statement == 'if' or statement == 'and':
                temp.append(statement)
            else:
                if(fa.isVariable(statement)):
                    temp.append('a')
                elif(fa.isNumber(statement)):
                    temp.append('1')
                elif statement == '':
                    continue
    for i in range(len(temp)):
        if temp[i] == '\n':
            temp[i] = 'newline'
    return temp,valid