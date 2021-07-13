from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


PATH ="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

url='https://servicio.indecopi.gob.pe/gaceta/'

driver.get(url)

getArea=driver.find_element_by_id('FormListado:cboAreGacetacomboboxValue')
getArea.clear()
#getArea.send_keys("SIGNOS DISTINTIVOS")
#getArea.send_keys(Keys.RETURN)
#getAreax=driver.find_element_by_id("FormListado:cboAreGaceta")
#select =Select(driver.find_element_by_id("FormListado:cboAreGaceta"))
#continue_link = driver.find_element_by_link_text('SIGNOS DISTINTIVOS')
#continue_link.click()
time.sleep(5)
driver.quit()

headers={
    
    
    'Accept-Language':'es-ES,es;q=0.9'
    ,'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    ,'Cookie':'cookiesession1=678ADA84TUVWXYZABCDEFGHIJKLMB3C3; _ga=GA1.3.699267409.1626093199; _gid=GA1.3.1924001759.1626093199; JSESSIONID=7hugJDfdBzNAs80542pAtCJei7FT8_Hb83uApeq4IM2TJyY-ZFo-!174632755!2060465349'
    ,'Host':'servicio.indecopi.gob.pe'
    ,'Origin':'https://servicio.indecopi.gob.pe'
    ,'Referer':'https://servicio.indecopi.gob.pe/gaceta/'
    ,'sec-ch-ua-mobile':'?0'
    ,'Sec-Fetch-Dest':'empty'
    ,'Sec-Fetch-Mode':'cors'
    ,'Sec-Fetch-Site':'same-origin'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

#r=requests.get(url,headers=headers)
#print(r.text)
#tohtml.wrapStringInHTML("test",url,r.text)