import requests

print("\nPara ver la base de datos de datos del sarampion en Panama a la fecha presione 1:")
seleccion = int(input())
if seleccion == 1:
    api_url = "http://localhost:5000/"
    response = requests.get(api_url)
    for i in response:
        print (i)
