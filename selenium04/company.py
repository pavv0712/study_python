import csv
from model_company import Company
 
def loadcompany():
    
    companies = list() 

    with open('c:/python/finance/companylist.csv', newline = '') as csvfile:
        
        reader = csv.DictReader(csvfile)
        
        for row in reader:
           
            symbol = row["Symbol"]
            name = row["Name"]
            lastsale = row["LastSale"]
            marketcap = row["MarketCap"]
            ipoyear = row["IPOyear"]
            sector = row["Sector"]
            industry = row["industry"]
            summary_quote = row["Summary Quote"]

            com = Company(symbol, name, lastsale, marketcap, ipoyear, sector, industry , summary_quote)
        
            companies.append(com)
    
    
    return companies
