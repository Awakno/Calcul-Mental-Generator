from random import *
import string

print("Générating...")

while True:
	while True:
		n1 = "".join(choice(string.digits)for x in range(randint(1,3)))
		n2 = "".join(choice(string.digits)for x in range(randint(1,3)))
		if n1.startswith("0"):
			break
		if n2.startswith("0"):
			break
		s = ["+","-","*"]
		cal = f"{n1}{choice(s)}{n2}"
		r=eval(cal)
		
		if len(str(r)) >= 3:
			break
		
		f=open("cal.txt","a+")
		#read = open("cal.txt","r").read().splitlines()
		f.write(f"{cal}\n")
		#print(f"{cal} = {str(r)}")