mapa = [ 
		[" ","D"," "," "],
		[" "," "," "," "],
		[" "," "," "," "],
		[" "," "," "," "],
		["S"," "," "," "]
		]
pathing = [(4,0)]
steps = []
count = 0
type_check = type(())

def look_next(positions):
		every_possible = []
		for i in positions:
			UP = (i[0] + 1,i[1])
			DOWN = (i[0] - 1,i[1] )
			LEFT = (i[0], i[1] - 1 )
			RIGHT = (i[0],i[1] + 1)
			l = [UP,DOWN,LEFT,RIGHT]
			removal = []
			for j in l: 
				if j[1] < 0 or j[0] >= len(mapa) or j[1] >= len(mapa[j[0]])  or j[0] < 0 or type(mapa[j[0]][j[1]]) == type_check or mapa[j[0]][j[1]] =="S" or mapa[j[0]][j[1]] == "*" : 
					removal.append(j)
			l = list(set(l)-set(removal))
			every_possible.append(l)
		return every_possible
		
def get_path(start):
	global steps
	parent = mapa[start[0]][start[1]]
	if parent == "S":
		return "Done"
	steps.insert(0,parent)
	get_path(parent)


def main():
	global pathing
	global count 
	possible = look_next(set(pathing))
	count += 1
	parents = list(set(pathing))
	pathing= []
	finished = False 
	for i in possible:
		
		for j in i:
			if mapa[j[0]][j[1]] == "D":
				finished = True
				endcords = j
			mapa[j[0]][j[1]] = parents[possible.index(i)]
			#mapa[j[0]][j[1]] = "S"
			
			pathing.append(j)
		if finished == True:
			return endcords
	
while True:
	finished = main()
	print(finished)
	for i in mapa:
		print(i)

	if finished != None:
		print(count)
		get_path(finished)
		steps.append(finished)
		[print(f"{i[0]} {i[1]}") for i in steps]
		break
	print("-----------------------------------")
	


#for i in mapa:
	#print(i)
#print(look_next((3,0)))