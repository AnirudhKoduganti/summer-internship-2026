import requests 

url = "https://www.sec.gov/files/company_tickers.json"

headers = {
    "User-Agent": "Anirudh Koduganti anirudhkoduganti09@gmail.com"
}

response = requests.get(url, headers=headers)

data = response.json()

ticker = input("Enter a ticker: ").upper()

found = False 
for company in data.values():
    if company["ticker"] == ticker:
        found = True
        print("Company: ", company["title"])
        cik = str(company["cik_str"]).zfill(10)
        print("CIK Number: ", cik)
        break 
    
if not found:
    print("Invalid ticker.")
    quit()

url = f"https://data.sec.gov/submissions/CIK{cik}.json"

response = requests.get(url, headers=headers)

data = response.json() 


forms = data["filings"]["recent"]["form"]
dates = data["filings"]["recent"]["filingDate"]

index = forms.index("10-K")
print("Most recent date of 10-K filing: ", dates[index])
