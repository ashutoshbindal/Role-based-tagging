import re
import os
import csv
import pickle

# def Repeat(x): 
#     _size = len(x) 
#     repeated = [] 
#     for i in range(_size): 
#         k = i + 1
#         for j in range(k, _size): 
#             if x[i] == x[j] and x[i] not in repeated: 
#                 repeated.append(x[i])
#                 print x[i]
#     return repeated 

allpeople_connected = {}
allpeople = []
with open("all_people_new.csv","rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
	count = 0
	for row in spamreader:
		if count < 3:
			count = count + 1
			continue
		elif count > 174995:
			break
		row_split = str(row).split('"')
		allpeople.append(row_split[0][3:])
		count = count + 1
# print allpeople[0]

# allpeople_new = list(set(allpeople))
# print len(allpeople_new)
# print len(allpeople)

# print (Repeat(allpeople)) 

all_lines = []
with open("outfile_new_new.csv","rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		all_lines.append(row)

total = 0
count = 0
i = 0
while i < len(all_lines):
	if "connected.name" in all_lines[i][0]:
		ents = []
		i+=2
		name = "files/"
		name += allpeople[count].replace("/","_")
		name += ".csv"
		# name.replace("/","_")
		# file = open(name,'w')
		while all_lines[i][0][0] != "+":
			ent = str(all_lines[i][0]).split('"')
			ents.append(ent[1])
			# file.write(ent[1])
			# file.write("\n")
			i+=1
		allpeople_connected[allpeople[count]] = ents
		# file.close()
		total+=1
		count += 1
		i+=3
	else:
		i+=1
# print total

print len(allpeople_connected.keys())

f = open("file.pkl","wb")
pickle.dump(allpeople_connected,f)
f.close()

