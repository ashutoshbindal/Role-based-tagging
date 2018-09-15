import os
import csv
import re

F = open("query.cyp","w")
with open("allpeople.csv","rb") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	count = 0
	for row in spamreader:
		if count < 3:
			count = count + 1
			continue
		elif count > 174995:
			# print row
			break
		row_split = str(row).split('"')
		# print row_split[1]
		F.write("Match (:person {name:")
		F.write('"')
		F.write(row_split[1])
		F.write('"')
		F.write("})-->(connected) return connected.name;")
		F.write("\n")
		count = count + 1
		# call = "python connected.py "
		# call = call + '"' + row_split[1] + '"' 
		# os.system(call)
		# new_row = re.findall(r'"(.*?)"', str(row))
		# print(re.findall(r'"(.*?)"', str(new_row)))
F.close()


# F.write("Match (:person {name:")
# F.write('"')
# F.write(name)
# F.write('"')
# F.write("})-->(connected) return connected.name;")
# # call = "./neo4j-shell -file query.cyp > temp.csv"
# call = "./neo4j-shell -file query.cyp > "
# call = call + "files/" + name + ".csv"

# os.system(call)