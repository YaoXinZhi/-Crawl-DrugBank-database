# /usr/bin/python
# -*- coding : utf-8 -*-

#python 3.5
import requests
from bs4 import BeautifulSoup
import pandas
import os 

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
    
def parserPage(infolist,url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    for i in soup.find('tbody').children:
        a = {}
        a['DrugName'] = i.find(attrs={'class':'name-value text-sm-center drug-name'}).a.string
        if i.find(attrs = {'class':'categories-value'}).a == None:
            a['DrugCategories'] = ''
        else:
            a['DrugCategories'] = i.find(attrs={'class':'categories-value'}).a.string
        a['ID'] = i.find(attrs = {'class':'name-value text-sm-center drug-name'}).a.attrs['href'].split('/')[2]
        a['Weight'] = i.find(attrs = {'class':'weight-value'}).contents[0]
        a['Indication'] = i.find(attrs = {'class':'indication-value'}).string
        infolist.append(a)
  
                    
def replace(original,new,pos):
    return original[:pos]+new
        
def main():
    infolist = []
    #depth = 364
    depth = 23
    count = 0        
    for i in range(1,depth):
        #url = 'https://www.drugbank.ca/drugs?utf8=%E2%9C%93&type=small_molecule&filter=false'
        url = 'https://www.drugbank.ca/drugs?utf8=%E2%9C%93&type=biotech&filter=false'
        if i != 1:
            #page = 'c=name&d=up&filter=false&page='+str(i)+'&type=small_molecule'
            page = 'c=name&d=up&filter=false&page='+str(i)+'&type=biotech'
            url = replace(url,page,30)
        parserPage(infolist,url)
        count = count + 1
        print ("\r当前进度: {:.2f}%".format(count*100/depth),end="")
        
    Oput_file = pandas.DataFrame(infolist)
    Oput_file.head(50)
    if not os.path.exists('DrugBank-BiotechDrug.xlsx'):
        os.mknod('DrugBank-BiotechDrug.xlsx')
    if not os.path.exists('DrugBank-SmallMoleculeDrug.xlsx'):
        os.mknod('DrugBank-SmallMoleculeDrug.xlsx')
    #Oput_file.to_excel('DrugBank-SmallMoleculeDrug.xlsx')
    Oput_file.to_excel('DrugBank-BiotechDrug.xlsx')
    print ()
    print ('win')
    
main()
            
        
