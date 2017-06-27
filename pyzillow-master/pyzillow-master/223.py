import csv
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
with open ('jihe.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    address_list=[]
    for row in readCSV:
        address=row[3]
        zipcode=row[7]
       
        if address!='':
            address_list.append([address,zipcode])
       
    print (address_list)
zillow_data = ZillowWrapper('X1-ZWz1958v54k6bv_5w3uy')
for address,zipcode in address_list:
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    result = GetDeepSearchResults(deep_search_response)

