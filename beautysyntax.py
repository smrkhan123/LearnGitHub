from bs4 import BeautifulSoup
import requests
s=requests.get("https://www.rithmschool.com/blog")
soup=BeautifulSoup(s.text,"html.parser")
#print(soup.find(class_="super"))
#print(soup.find(id="super"))
#print(soup.body.div.p)
#print(soup.find_all(attrs{"data-example":"yes"}))
#print(soup.select(".super"))
#print(soup.select("#special"))
