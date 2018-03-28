from TradingView_Get_StrongBuy import Browse_Signals
import json,requests
import time


def dobi_ceno(par):
    url = "https://www.bitstamp.net/api/v2/ticker/"
    resp = requests.get(url=url+par)
    data = json.loads(resp.text)
    return data["last"]

def zazeni():
    #Naredimo slovar z kljucem par+Buy/Sell, pod vrednost damo: 1-zadnjo ceno.
    #Nato cez 15min za vsak element pogledamo ceno in izracunamo profit/izgubo
    #Zapremo pozicije in ponovimo vajo
    
    portfelj = 1000
    while True:
        slovar_parov = dict()
        n = 0
        while n==0:
            try:
                sez = Browse_Signals()
                n=1
                print(n)
            except:
                pass
        for i in sez:
            print(i)
            slovar_parov[i[0]] = [dobi_ceno(i[0].lower()),i[1]]
            time.sleep(1)
        time.sleep(900)
        for i in sez:
            print(i)
            cena = dobi_ceno(i[0].lower())
            if slovar_parov[i[0]][1] == "Buy":
                sprememba = float(cena)/float(slovar_parov[i[0]][0])
                print("Prej cena: " + str(slovar_parov[i[0]][0]))
                print("Potem cena: " + str(cena))
                print("Par : " + i[0] + " Buy")
                print("Sprememba: " + str(sprememba))
                if sprememba > 1:
                    print("Profit")
                else:
                    print("Izguba")
                portfelj*=sprememba
            elif slovar_parov[i[0]][1] == "Sell":
                sprememba = (float(slovar_parov[i[0]][0])-float(cena))/float(slovar_parov[i[0]][0])
                print("Prej cena: " + str(slovar_parov[i[0]][0]))
                print("Potem cena: " + str(cena))
                print("Par : " + i[0] + " Sell")
                print("Sprememba: " + str(sprememba))
                if sprememba >0:
                    print("Profit")
                    
                else:
                    print("Izguba")
                portfelj+=sprememba*portfelj
            print("\n\n")
            
            print(portfelj)
        #if time.time() > 1512919635.834428:
            #break
            
        
        
