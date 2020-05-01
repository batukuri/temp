import json 
dates = []
values = []
sma = []
    
with open("data.json", "r") as f:
    data = json.load(f)
    smaRange = 7
    for i, record in enumerate(data["historical"]):
        print (str(i) + " " + record["date"] + " " + str(record["close"]))
        dates.append(record["date"])
        values.append(record["close"])
        if (i >= smaRange - 1):
            # find the sum of smaRange values 
            sum = 0
            for j in range(smaRange):
                sum += values [i - j]
            sma.append(round(sum / smaRange, 2))
        else:
            sma.append(0)
    for i in range(len(dates)):
        print (str(i) + " " + dates[i] + " " + str(values[i]) + " " + str(sma[i]))
