import sys
import os

name = sys.argv[1]
call = "./neo4j-shell -file query.cyp > temp.csv"
os.system(call)