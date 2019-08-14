from bs4 import BeautifulSoup
import requests
for i in range(1,6):
	a="https://www.rithmschool.com/blog?page="+str(i)
	print(a)
	s=requests.get(a)
	soup=BeautifulSoup(s.text,"html.parser")
	for j in range(1,3):
		print(j,soup.find_all("article")[j].h4.get_text())
		l=soup.find_all(class_="card")[j].p.get_text()
		a=l.split()
		c=0
		print('Body: ',end='')
		for k in a:
			if (c<=30):
				print(k,end=' ')
				c+=1
		print(end='\n\n')
		print('Date: ',soup.find_all(class_="service-heading")[j].small.get_text(),end="\n\n")