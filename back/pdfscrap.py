import os
import sys
import re
import csv

path=sys.argv[1]




#with open(path,'r') as f, open(path2,'w') as f2:
with open(path, 'r') as f, open("dati.csv", 'w') as f2:
    header = ['name', 'price']

    writer=csv.DictWriter(f2, header)
    writer.writeheader()


    for line in f:
        #print(line)
        content = f.readline()
        #print(content)
        #content = [x.strip(';') for x in content]
        content = re.sub('\n', '', content)

        splitted=content.split(";")
        try:
            dict={'name':splitted[0], 'price':splitted[1]}
        #print(content)
            print(dict)
            writer.writerow(dict)
        except:
            pass

        #myline=line.strip()
        #print(content)
        #print("\n \n")
        # #if myline.startswith("Time"):
        #     #print(myline)
        #     myline2=myline.partition("= ")
        #     myline3=myline2[2].partition(" s;")
        #     #print(myline3)
        #     #f2.write(myline3[0] +"\n")


