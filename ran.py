import random 
  
# prints a random value from the list 
list1 = [1, 2, 3, 4, 5, 6]  
print(random.choice(list1)) 
  
# prints a random item from the string  
string = "striver" 
print(random.choice(string))  




ml=var.split()
mr=[]
for i in ml:
	mr.append(i[0:1:])
name=' '.join(mr)
mar=soup.find_all(class_="clearfix")[r].div.a.attrs['href']
aut=requests.get("https://www.brainyquote.com"+mar)
soup=BeautifulSoup(aut.text,"html.parser")
nat=soup.find_all(class_="subnav-below-p")[0].find_all("a")[0].get_text()
pro=soup.find_all(class_="subnav-below-p")[0].find_all("a")[1].get_text()
dob=soup.find_all(class_="subnav-below-p")[0].find_all("a")[2].get_text()

guess=input('Guess author name: ')
if(var==guess):
	print("Right answer")
else:
	print("Wrong answer, Hint:-Nationality ",nat)
	guess=input('Now guess once again: ')
	if(var==guess):
		print("Right answer")
	else:
		print("Wrong answer, Hint:-Profession: ",pro)
		guess=input('Now guess once again: ')
		if(var==guess):
			print("Right answer")
		else:
			print("Wrong answer, Hint:-DOB: ",dob)
			guess=input('Now guess once again : ')
			if(var==guess):
				print("Right answer")
			else:
				print("Wrong answer, Hint:-First & Last Letter: ",name)
				guess=input('Now guess once again : ')
				if(var==guess):
					print("Right answer")
				else:
					print('Wrong answer')
					print("Right answer is: ",var) 