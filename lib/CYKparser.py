import numpy as np

# Fungsi menunjukkan hasil parsing
def parseResult(boolMatrix,length):
  # hasil parsing ditentukan lewat array of booleans
  if boolMatrix[length][1][1] == True:
    print("Accepted. No errors detected.")
  else:
    print("Syntax Error")

# Fungsi parsing grammar dengan algoritma CYK
def CYKParser(input, CNF):
  strLength = len(input)
  cnfLength = len(CNF)
  
  # P merupakan 3 dimensional array of booleans
  bool = [[[0 for x in range(cnfLength + 1)] for x in range(strLength + 1)] for x in range(strLength + 1)]
  # R merupakan array untuk menampung grammar cnf
  list = [None]
  id = dict(zip(CNF, [i for i in range(1, cnfLength+1)]))
  map = {}

  # Memasukan index dan variable yang terdapat di CNF ke map dan R 
  for var in CNF:
    list.append(CNF[var])
  
  # CYK table-filling algorithm
  for i in range(1, strLength+1):
    for j in range(1, cnfLength+1):
      for cnf in list[j]:
        if cnf[0] == input[i-1]:
          bool[1][i][j] = True
          break
  
  for l in range(2, strLength+1):
    for i in range(1, strLength-l+2):
      for j in range(1, l):
        for k in range(1, cnfLength + 1):
          for cnf in list[k]:
            if (len(cnf) != 1):
              if bool[j][i][id[cnf[0]]] and bool[l-j][i+j][id[cnf[1]]]:
                bool[l][i][k] = True
  
  # Menunjukkan hasil parsing pada user
  parseResult(bool,strLength)
  