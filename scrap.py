from bs4 import BeautifulSoup
import requests
s=requests.get("https://www.rithmschool.com/blog")
soup=BeautifulSoup(s.text,"html.parser")
#1.
print("1.",soup.find_all("article")[0].h4.get_text())
l=soup.find_all(class_="card")[0].p.get_text()
a=l.split()
c=0
print('Body: ',end='')
for i in a:
	if (c<=30):
		print(i,end=' ')
		c+=1
print(end='\n\n')
print('Date: ',soup.find_all(class_="service-heading")[0].small.get_text(),end="\n\n")


#2.
print('2. ',soup.find_all("article")[1].h4.get_text())
m=soup.find_all(class_="card")[1].p.get_text()
b=m.split()
c=0
print('Body: ',end='')
for i in b:
	if (c<=30):
		print(i,end=' ')
		c+=1
print(end='\n\n')
print(soup.find_all(class_="service-heading")[1].small.get_text(),end="\n\n")

#3
print('3. ',soup.find_all("article")[2].h4.get_text())
n=soup.find_all(class_="card")[2].p.get_text()
d=n.split()
c=0
print('Body: ',end='')
for i in d:
	if (c<=30):
		print(i,end=' ')
		c+=1
print(end='\n\n')
print(soup.find_all(class_="card")[2].small.get_text(),end="\n\n")

#4

print("4. ",soup.find_all('article')[3].h4.get_text())
p=soup.find_all(class_="card")[3].p.get_text()
e=p.split()
c=0
print('Body: ',end='')
for i in e:
	if (c<=30):
		print(i,end=' ')
		c+=1
print(end='\n\n')
print(soup.find_all(class_="card")[3].small.get_text(), end="\n\n")
#5
print('5 ',soup.find_all("article")[5].h4.get_text())
q=soup.find_all(class_="card")[5].get_text()
f=q.split()
c=0
print('Body: ',end='')
for i in f:
	if (c<=30):
		print(i,end=' ')
		c+=1
print(end='\n\n')
print(soup.find_all(class_="card")[5].small.get_text())


	
