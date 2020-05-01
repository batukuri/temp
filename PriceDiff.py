import json 
import requests
from operator import itemgetter
import  datetime 
import csv

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

prevDataFile = "Data_"+str(yesterday)+".json"
currDataFile = "Data_"+str(today)+".json"
def GetSymbolList():
    baseUrl = 'https://financialmodelingprep.com/'
    queryUrl = baseUrl + 'api/v3/company/stock/list'
    return requests.get(queryUrl)

#with open("symbol_data.json", "r") as fr:
    data = json.load(fr)
    with open("symbol_data_prev.json", "w") as fw:
        json.dump(data, fw, indent=4);
# refactor this file to be usable by others 
# copy the old data to previous date file   
def SetupData():
    # get the latest data 
    result = GetSymbolList()
    if (result.status_code == 200):
        print("success")
        with open(currDataFile, "w") as f:
            json.dump(result.json(), f, indent=4);
    else:
        print ("failed") 

# compare the old and new file and dump the diff in sorted order 
SetupData()
prevFr = open(prevDataFile, "r")
currFr = open(currDataFile, "r")
prevData = json.load(prevFr)["symbolsList"]
currData = json.load(currFr)["symbolsList"]
diffPercent = []
for i, record in enumerate(prevData):
    #print (record["symbol"] + " " + str(record["price"]) + " : " + str(currData[i]["price"]))
    diff = (currData[i]["price"] - record["price"])
    if (record["price"] == 0):
        diffP = 0
    else:
        diffP =  diff / record["price"] * 100
    diffPercent.append({"diffP" : round(diffP, 2), "symbol" : record["symbol"], "prevprice" : record["price"], 
                        "currprice" : currData[i]["price"]})
    #print (record["symbol"] + " " + str(record["price"]) + " : " + str(currData[i]["price"]) + " -> " + str(diffPercent[i]))
    #print (diffPercent[i])

sortedDiffPercent = sorted(diffPercent, key=itemgetter('diffP'), reverse = True) 
with open("sortedSymbolData.json", "w") as f:
    json.dump(sortedDiffPercent, f, indent=4);
    
with open('symbolList.csv', 'w', newline='') as csvfile:
    fieldnames = ["symbol", "prevprice", "currprice", "diffP"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sortedDiffPercent)
