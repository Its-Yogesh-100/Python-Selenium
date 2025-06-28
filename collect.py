from bs4 import BeautifulSoup
import os
import pandas

d={'title':[],'price':[],'link':[]}

for file in os.listdir('data'):
    try:
        with open(f'data/{file}') as f:
            html_doc=f.read()
        soup=BeautifulSoup(html_doc,'html.parser')

        ti=soup.find('h2')
        title=ti.text
    

        #to scrap the link
        l=soup.find('a')
        link="https://amazon.in/"+l['href']
    


        # to scrap the price
        pi=soup.find('span',attrs={'class':'a-price-whole'})
        price=pi.get_text()
        

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

        print(d)
        
        
    except Exception as e:
        print(e)

df=p