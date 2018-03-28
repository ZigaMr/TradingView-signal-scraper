from selenium import webdriver
import selenium
import time
from bs4 import BeautifulSoup
from Mapping_poimenovanja import poimenovanja


def Browse_Signals():
    browser = webdriver.Firefox()
    #browser = webdriver.PhantomJS(r'C:\Users\Ziga\Desktop\MACHINE LEARNING\Crypto\CryptoSignals\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    #browser.set_window_position(-10000,0)
    url = "https://www.tradingview.com/cryptocurrency-signals/"
    browser.get(url)
    time.sleep(3)
    button = browser.find_element_by_xpath("/html/body/div[7]/div/div[3]/table/thead/tr/th[8]/div/div")
    button.click()
    time.sleep(2)
    button = browser.find_element_by_xpath("//div[contains(@class, 'tv-dropdown tv-dropdown-behavior')]")
    button.click()
    time.sleep(4)
    button = browser.find_element_by_xpath("//div[contains(@data-interval, '1h')]")
    button.click()
    button = browser.find_element_by_xpath("/html/body/div[7]/div/div[3]/table/thead/tr/th[9]/div/i")
    button.click()
    button = browser.find_element_by_xpath("/html/body/div[7]/div/div[6]/div/div[2]/div/span/span/span")
    button.click()
    time.sleep(3)
    #button = browser.find_element_by_xpath("/html/body/div[7]/div/div[7]/div[3]/div[1]/div[6]")
    #button.click()
    time.sleep(2)
    button = browser.find_element_by_xpath("//input[contains(@name, 'BITSTAMP')]")
    button.click()
    time.sleep(2)
    innerHTML = str(browser.execute_script("return document.body.innerHTML")) #returns the inner HTML as
    #time.sleep(10)
    browser.quit()
    
    soup = BeautifulSoup(innerHTML,"html.parser")
    spans = soup.find_all('tr', {'class' : 'tv-data-table__row tv-data-table__stroke tv-screener-table__result-row'})
    sez = []
    for i in spans:
        sez.append(i.get_text().strip().split(" / "))
    #print(sez)
    #print(sez)
    sez2 = []
    for i in sez:
        pair = i[0].split("\n")[0]
        if "Buy" in i[1]:
            sez2.append([pair,"Buy"])
        elif "Sell" in i[1]:
            sez2.append([pair,"Sell"])
        
    print(sez2)
    return sez2

    
#with open("dat.txt","w",encoding="utf8") as f:
#    f.write(innerHTML)
