import wikipedia as wiki
from bs4 import BeautifulSoup
import requests
import pickle
import csv
import sys


#storing all the person data

# with open('file.pkl', 'rb') as handle:
#     connected = pickle.load(handle)

# keys = list(connected.keys())
# print(connected[keys[0]])
# print(keys[0])

# allpeople_dict = {}
# allpeople = []
# with open("all_people_new.csv") as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
# 	count = 0
# 	for row in spamreader:
# 		if count < 3:
# 			count = count + 1
# 			continue
# 		elif count > 174995:
# 			break
# 		row_split = str(row).split('"')
# 		# allpeople.append(row_split[0][3:])
# 		uuid = int(row_split[0][3:])
# 		allpeople_dict[uuid] = row_split[1]
# 		allpeople.append(row_split[1])
# 		count = count + 1
# # id = int(keys[0])
# # print(allpeople[id])

# f = open("person_dict.pkl","wb")
# pickle.dump(allpeople_dict,f)
# f.close()

# checking with the newly created pkl file
# import pickle

# with open('person_dict.pkl', 'rb') as handle:
#     connected = pickle.load(handle)

# person_list = list(connected.keys())
# person = person_list[0]
# print(person)
# print(connected[person_list[0]])

with open('person_dict.pkl', 'rb') as handle:
    person = pickle.load(handle)

with open('file.pkl', 'rb') as handle:
    connected = pickle.load(handle)

with open('extract_wiki.tsv', 'a') as fin:
    fin.write('uuid' + '\t' + 'person_name' + '\t' + 'wikipedia_name' + '\t' + 'max_entity_match' + '\t' + 'total _entity' + '\n')

count = 0

keys = list(connected.keys())
with open('extract_wiki.tsv', 'a') as fin:
	for i in range(len(keys)):
		temp_key = int(keys[i])
		person_name = person[temp_key]
		# print(person_name)
		# print(connected[keys[i]])
		# print(connected[keys[i]][0])

		search = wiki.search(person_name)
		if(len(search) != 0):
			count += 1
			max_match = 0 
			max_index = 0
			# flag = False
			for j in range(len(search)):
				# flag = False
				try:	
					summary = wiki.page(search[j]).content
					temp_match = 0
					for k in range(len(connected[keys[i]])):
						if connected[keys[i]][k].lower() in summary.lower():
							temp_match += 1
					if(max_match < temp_match):
						max_match = temp_match
						max_index = j
				except:
					print("")
			temp_row = str(temp_key) + '\t' + person_name + "\t" + search[max_index] + "\t" + str(max_match) + "\t" + str(len(connected[keys[i]])) + "\n"
			print(temp_row)
			
			fin.write(temp_row)
				# page = wiki.page(search[j])
				# url = page.url
				# url_name = url[::-1].split('/')[0]
				# url_name = url_name[::-1]
		
		# print(count)
		# break

with open('extract_wiki.tsv', 'a') as fin:
	fin.write('\n\n\n' + str(count) )
