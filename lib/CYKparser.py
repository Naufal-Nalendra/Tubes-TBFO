import numpy as np

# Fungsi menunjukkan hasil parsing
def parseResult(boolMatrix,length):
  # hasil parsing ditentukan lewat array of booleans
  if boolMatrix[length][1][1] == True:
    print("Accepted. No errors detected.")
  else:
    print("Syntax Error")

# Fungsi menunjukkan letak parsing error paling awal
def findError():
  return

# Fungsi parsing grammar dengan algoritma CYK
def CYKParser(input, CNF):
  strLength = len(input)
  cnfLength = len(CNF)
  
  # P merupakan 3 dimensional array of booleans
  P = np.zeros((cnfLength+1, cnfLength+1, strLength+1))
  # R merupakan array untuk menampung grammar cnf
  R = [None for x in range(cnfLength + 1)] 
  map = {}

  # Memasukan index dan variable yang terdapat di CNF ke map dan R
  range = enumerate(CNF)
  for i, var in range:
    map[var] = i + 1
    R[i + 1] = CNF[var]
  
  # CYK table-filling algorithm
  for i in range(1, strLength+1):
    for j in range(1, cnfLength+1):
      for cnf in R[j]:
        if cnf[0] == input[i-1]:
          P[1][i][j] = True
          break
  
  for l in range(2, strLength+1):
    for i in range(1, strLength-l+2):
      for j in range(1, l):
        for k in range(1, cnfLength + 1):
          for cnf in R[k]:
            if (len(cnf) != 1):
              cell1 = map[cnf[0]]
              cell2 = map[cnf[1]]
              if P[j][i][cell1] and P[l-j][i+j][cell2]:
                P[l][i][k] = True
  
  # Menunjukkan hasil parsing pada user
  parseResult(P,strLength)
  