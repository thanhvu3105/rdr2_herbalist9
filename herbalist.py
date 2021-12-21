##Keep track of herb that you haven't picked for HERBALIST 9 
##how to run 
# python3 herbalist.py [herb_name]

import sys
import json



def checkFinished(data):
    for herb in data:
        if data[herb] == 0:
            return False
    return True

def checkHerbLeft(data):
    herbsLefted = []
    print("Herbs left to pick: ")
    for herb in data:
        if data[herb] == 0:
            herbsLefted.append(herb)
    print(len(herbsLefted))
    for herb in herbsLefted:
        print(herb)

if(len(sys.argv) > 1):
    # input = sys.argv[1].replace('_',' ').title()
    input = str(sys.argv[1]).title()
    print(input)


with open('list.json','r') as f:
    data = json.load(f)

if input in data:
    print(" ------------ key exist -------------")
    if data[input] == 0:
        print(" ---------------- update -----------------")
        data[str(input)] = 1
    else:
        print(" ---------------- herb is already picked --------------- ")
else:
    print("Invalid herb")

with open('list.json','w') as f:
    json.dump(data, f)



if(checkFinished(data) == False):
    print(" -------------- CHALLENGE NOT DONE -------------")
    checkHerbLeft(data)
else:
    print(" -------------- FINISH CHALLENGE ---------------- ")


f.close()