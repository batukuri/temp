import requests
import json 

class Stock:
    baseUrl = "https://finnhub.io/api/v1/stock/"
    key = "bq4ih7frh5rbnj6k5l1g"
    
    edgarKey = '9f4d11d4c5101b97f88db2d4a2bdd7c8'
    edgarBaseUrl = 'https://datafied.api.edgar-online.com/v2' 
    
    def __init__(self, ticker):
        self.ticker = ticker
    
    def GetInsiderFiling(self):
        # from edgar 
        queryUrl = self.edgarBaseUrl + '/insiders/filers?'
        params = {'issuetickers' : self.ticker, 'appkey' : self.edgarKey}
        r = requests.get(queryUrl, params)
        print(r.url)
        return r
    
    def GetCurrentIssueHolders(self):
        # from edgar 
        queryUrl = self.edgarBaseUrl + '/ownerships/currentissueholders?'
        params = {'limit' : 9999, 'tickers' : self.ticker, 'appkey' : self.edgarKey}
        r = requests.get(queryUrl, params)
        print(r.url)
        return r
    
    def GetCurrentIssueHoldersSince(self):
        # from edgar - NOT WORKING 
        queryUrl = 'https://datafied.api.edgar-online.com/v2/ownerships/currentissueholders?modifiedsince eq "12/30/2019"&appkey={9f4d11d4c5101b97f88db2d4a2bdd7c8}'
        r = requests.get(queryUrl)
        print(r.url)
        return r
    
    def GetCurrentIssueHolders2(self):
        # from edgar - NOT WORKING 
        # https://datafied.api.edgar-online.com/v2/ownerships/currentownerholdings?filter=ticker eq "BAC"&appkey={APPKEY}
        #queryUrl = self.edgarBaseUrl + 'ownerships/currentownerholdings?'
        #filter = 'ticker eq ' + '"{}"'.format(self.ticker)
        #params = {'filter' : filter, 'appkey' : self.edgarKey}
        queryUrl = 'https://datafied.api.edgar-online.com/v2/ownerships/currentownerholdings?filter=ticker eq "BAC"&appkey={9f4d11d4c5101b97f88db2d4a2bdd7c8}'
        r = requests.get(queryUrl)
        print(r.url)
        return r
    
    def GetInvestorOwnership(self):
        #queryUrl = self.baseUrl + 'investor-ownership?symbol={}&token={}'.format(self.ticker, self.key)
        #return requests.get(queryUrl)
        queryUrl = self.baseUrl + 'investor-ownership?'
        params = {'symbol' : self.ticker, 'token' : self.key}
        r = requests.get(queryUrl, params)
        print(r.url)
        return r
    
    def GetInvestorOwnershipYahoo(self):
        #queryUrl = self.baseUrl + 'investor-ownership?symbol={}&token={}'.format(self.ticker, self.key)
        #return requests.get(queryUrl)
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders"
        querystring = {"symbol":self.ticker}
        headers = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': "e9b6a8fdf8msh9fbafd25ae17073p13647ejsnd27aee4ff878"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        return response
    
    def GetFundOwnership(self):
        queryUrl = self.baseUrl + 'fund-ownership?symbol={}&token={}'.format(self.ticker, self.key)
        return requests.get(queryUrl)
    def GetData(self):
        ''' this gets the entire data for a given ticket'''
        ''' Still need to validate the data '''
        ''' https://eodhistoricaldata.com/knowledgebase/stock-etfs-fundamental-data-feeds/'''
        queryUrl = "https://eodhistoricaldata.com/api/fundamentals/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX"
        return requests.get(queryUrl)
    def GetMostActive(self):
        queryUrl = "https://financialmodelingprep.com/api/v3/company/rating/ONTX"
        return requests.get(queryUrl)
    def GetRealTimePrice(self):
        queryUrl = 'https://financialmodelingprep.com/api/v3/real-time-price/AAPL'
        return requests.get(queryUrl)
    def GetSymbolList(self):
        baseUrl = 'https://financialmodelingprep.com/'
        queryUrl = baseUrl + 'api/v3/company/stock/list'
        return requests.get(queryUrl)
    def GetHistoricalData(self):
        baseUrl = 'https://financialmodelingprep.com/'
        queryUrl = baseUrl + 'api/v3/historical-price-full/AAPL?timeseries=244'
        return requests.get(queryUrl)
        
    
stock = Stock("MITT")
result = stock.GetHistoricalData()
if (result.status_code == 200):
    print("success")
    with open("data.json", "w") as f:
        json.dump(result.json(), f, indent=4);
else:
    print ("failed") 
#result2 = stock.GetCurrentIssueHolders2()
# result = stock.GetData()
#result = stock.GetMostActive()
#with open("data2.json", "w") as f:
    #json.dump(result2.json(), f, indent=4);
