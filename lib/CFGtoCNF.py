from copy import deepcopy
import string
import codecs

def readCFGFile(filepath):
	cfg = {} 
	f = open(filepath, 'r')
	lines = [line.split('->') for line in f.readlines()]
	for line in lines:
		if line[0] not in "\n" and line[0][0] not in "#":
			var = line[0].replace(" ","")
			production = [raw.split() for raw in line[1].split('|')]
			key = list(cfg.keys())
			if var in key:
				productions = cfg[var]
				productions.extend(production)
			else:
				cfg.update({var : production})
	f.close()
	return cfg

def isVar(x):
	for char in x:
		if char not in (string.ascii_uppercase + '_' + string.digits):
			return False
	return True

def removeUnitProduction(cfg):
	keyVar = list(cfg.keys())
	for var in cfg:
		productions = cfg[var]
		flag = True
		while flag:
			flag = False
			for production in productions:
				if len(production) == 1 and isVar(production[0]):
					productions.remove(production)
					if production[0] in keyVar:
						newProduction = deepcopy([production for production in cfg[production[0]] if production not in productions])
						productions.extend(newProduction)
					flag = True
	return(cfg)

def get_key(val,cfg):
    for key, value in cfg.items():
         if val == value:
             return key

def CFGtoCNF(cfg):
	temp = {}
	terminal = []
	for var in cfg:
		productions = cfg[var]
		for production in productions:
			if len(production) == 1 and not(isVar(production[0])):
				terminal.append(production[0])
	t = 1
	for var in cfg:
		productions = cfg[var]
		for production in productions:
			for symbol in production:
				if not(isVar(symbol)):
					if symbol not in terminal:
						terminal.append(symbol)
						temp.update({f'T{t}' : [[symbol]]})
						t += 1
	cfg.update(temp)
	temp.clear()

	for var in cfg:
		productions = cfg[var]
		for i, production in enumerate(productions):
			for j, symbol in enumerate(production):
				if not (isVar(symbol)) and len(production) > 1:
					v = get_key([[symbol]],cfg)
					if not(v):
						v =  get_key([[symbol]],temp)
						if not(v):
							temp.update({f'T{t}' : [[symbol]]})
							t += 1
						productions[i][j] = get_key([[symbol]],temp)
					else:
						productions[i][j] = v 
					cfg.update({var : productions})
	cfg.update(temp)
	temp.clear()	

	for var in cfg:
		productions = cfg[var]
		idx = 1
		for i, production in enumerate(productions):
			while len(production) > 2:
				temp.update({f"{var}{idx}": [[production[0], production[1]]]})
				production = production[1:]
				production[0] = f"{var}{idx}"
				idx += 1
			productions[i] = production
			cfg.update({var : productions})
	cfg.update(temp)
	return cfg

# cfg = readCFGFile(r'data\cfg.txt')
# cnf = CFGtoCNF((removeUnitProduction(cfg)))

# with codecs.open(r'cnf.txt', mode="w", encoding="utf-8") as f:
#     for key in cnf:
#         for rules in cnf[key]:
#             prods_str = map(lambda p: "".join(p), rules)
#             line = f"{key} -> {' | '.join(prods_str)}\n"
#             line = line.replace("'", "")
#             f.write(line)