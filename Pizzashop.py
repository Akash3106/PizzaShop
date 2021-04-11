#Alan Pizza
def Menu():	#menu Function - print the pizzas with their numbers
		Menu.path="items.txt"  # Please provide path of your directory example-   C:\Users\Public\Desktop\items.txt    
		login()
		
		print("Enter 1 to go to the Menu  \nEnter 2 to Update the Menu  ")
		while True:
			try:
				chs= int(input("Enter your Choise : "))
				if chs == 2 or chs == 1:
					if(chs == 1):
						print("-------------- 10 inch Pizzas -------------- \n[1]	Mighty Meaty = £6.95 \n\n[2]	Funghi with Onions = £4.90 \n\n[3]	Cheese Feast = £5.75 \n\n[4]	Chicken and Garlic = £3.50 \n\n[5]	Seafood Surprise = £5.30\n")
						additionals()
					elif(chs == 2):
						other()
					break	
				else:
					print("That entry is not acceptable. Please enter again")
			except:	
				continue				
	
def phone(): #if the user selects the option phone this function is called.
	print("---------------Enter the order--------------")
	list=[]
	amt=0 #this sets a variable for the amount
	total=0 #this sets a variable for the total
	more=('Y' or 'y') #this allows upper or lower caseY to be accepted
	while( more != 'N') and (more != 'n'): #This allows upper or lower case N to be accepted.
		while True:
			try: #this is for error handling
				i=5
				import os.path
				if os.path.isfile(Menu.path):
					f=open(Menu.path,'r')
					for line in f:
						i=i+1
					f.close()
				else:
					i=5
				option=int(input('Select the Pizza from Menu : '))	 #asks the user to select the type of pizza
				if option >=1 and option<=5: #the following code works out the cost of each number of pizza
					if(option==1): 
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*6.95
						list.append("Mighty Meaty")
					elif(option==2):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*4.90
						list.append("Funghi with Onions")
					elif(option==3):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*5.75
						list.append("Cheese Feast")
					elif(option==4):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*3.50
						list.append("Chicken and Garlic")
					elif(option==5):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*5.30
						list.append("Seafood Surprise")
					break
				if option >=6 and option<=i: #the following code works out the cost of each number of pizza
					f = open(Menu.path , 'r')
					cnt=0
					deli="= £"
					for line in f:
						cnt=cnt+1
						if cnt == option:
							price=float(line.partition(deli)[2])
					f.close()
					num =int(input('Enter the number of pizza : '))
					amt=amt+num*price
					break;
				else:
					print("That entry is not acceptable. Please enter again")

			except: #this is the end of the statement for error handling
				continue
		while True:
			try:
				more=input('ADD More PIZZA (Y/N):') #after the user has added a pizza and anumber they are asked if they want to add another
				if(more=='Y' or more=='y' or more=='N' or more=='n'): #I made sure that upper and lowe case Y can be accepted. Try-except handles other entries.
					break
				else:
					print("That entry is not acceptable. Please enter again")
			except:
				continue
	while True:
		try: #this is for error handling
			deliver=input("Does the customer want order to be delivered (Y/N) : ")#the following code handles the delivery option
			if (deliver=='Y' or deliver=='y'or deliver=='N' or deliver=='n'):
				if(deliver=='Y' or deliver=='y'):
					total=amt + 1.50	#this gives total amount including delivery charge
					print('Total Bill of Customer = £',round(total, 2))
				if(deliver=='N' or deliver=='n'):
					total=amt	#this gives total amount without delivery charge
					print('Total Bill of Customer = £',round(total, 2))
				break
			else:
				print("That entry is not acceptable. Please enter again")
		except: #this is for error handling
			continue
	while True:
		try: #this is for error handling
			exit=input('Would you like to exit ? (Y/N) : ') #creates a variable to store Y/N in
			if(exit=='Y' or exit=='y' or exit=='N' or exit=='n'):
				if(exit=='Y' or exit=='y'):  #if Yes the program will exit or else menu will displayed
					print("GOOD BYE") #If they select Y they get a good bye message
				elif (exit == 'N' or exit == 'n'):
					Menu()
				break
			else:
				print("That entry is not acceptable. Please enter again")
		except: #this is for error handling
			continue	
	
def onLine():  #if user selects online this function is called.
	print("---------------Enter the order--------------")
	list=[]
	amt=0
	total=0
	more=('Y' or 'y')
	while ( more != 'N') and (more != 'n'):
		while True:
			try: #this is for error handling
				i=5
				import os.path
				if os.path.isfile(Menu.path):
					f=open(Menu.path,'r')
					for line in f:
						i=i+1
					f.close()
				else:
					i=5
				option=int(input('Select the Pizza from Menu : '))	 #asks the user to select the type of pizza
				if option >=1 and option<=5: #the following code works out the cost of each number of pizza
					if(option==1): 
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*6.95
						list.append("Mighty Meaty")
					elif(option==2):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*4.90
						list.append("Funghi with Onions")
					elif(option==3):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*5.75
						list.append("Cheese Feast")
					elif(option==4):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*3.50
						list.append("Chicken and Garlic")
					elif(option==5):
						num =int(input('Enter the number of pizza : '))
						amt=amt+num*5.30
						list.append("Seafood Surprise")
					break
				if option >=6 and option<=i: #the following code works out the cost of each number of pizza
					f = open(Menu.path , 'r')
					cnt=0
					deli="= £"
					for line in f:
						cnt=cnt+1
						if cnt == option:
							price=float(line.partition(deli)[2])
					f.close()

					num =int(input('Enter the number of pizza : '))
					amt=amt+num*price
					break;
				else:
					print("That entry is not acceptable. Please enter again")

			except: #this is for error handling
				continue
		while True:
			try: #this is for error handling
				more = input('ADD More PIZZA (Y/N):') 
				if (more == 'Y' or more == 'y' or more == 'N' or more == 'n'):
					break
				else:
					print("That entry is not acceptable. Please enter again")
			except: #this is for error handling
				continue
	while True:
		try: #this is for error handling
			deliver=input("Is customer want order to be delivered (Y/N) : ")
			if (deliver=='Y' or deliver=='y'or deliver=='N' or deliver=='n'):
				if(deliver=='Y' or deliver=='y'):
					total=amt*0.80	 + 1.50	#this gives total discount amount including delivery charge
					print('Total Bill of Customer = £',round(total, 2))
					
				if(deliver=='N' or deliver=='n'):
					total=amt*0.80		#this gives total discount amount without delivery charge
					print('Total Bill of Customer = £',round(total, 2))
					
				break
			else:
				print("That entry is not acceptable. Please enter again")
		except: #this is for error handling
			continue
	while True:
		try: #this is for error handling
			exit=input('Would you like to exit ? (Y/N) : ')
			if(exit=='Y' or exit=='y' or exit=='N' or exit=='n'):
				if(exit=='Y' or exit=='y'): #if true the program exits or else menu will displayed
					print("GOOD BYE")
				elif (exit == 'N' or exit == 'n'):
					print("-----------------------------------------")
					Menu()
				break
			else:
				print("That entry is not acceptable. Please enter again")
		except: #this is for error handling
			continue
	

def customer_details(): # This function takes the details of customer from user
	
	while True:
		try: #the following code works out the cost of each number of pizza
			pmode=input("Is Customer Order through Phone (Y/N): ") #Ask for type(mode) of order 
			if pmode=='Y' or pmode=='y' or pmode=='N' or pmode=='n':
				if(pmode=='Y' or pmode=='y'): #check the mode if true call the function phone() else go to the elif condition.
					phone()
				elif(pmode=='N' or pmode=='n'):#if this condition is true
					while True:
						try:
							omode=input("Is Customer Order through onLine (Y/N):") # ask the user for online mode
							if omode=='Y' or omode=='y' or omode=='N' or omode=='n':
								if(omode=='Y' or omode=='y'): #check if true call the function onLine() or else ask for exit from user
									onLine()
								elif(omode=='N' or omode=='n'):
									while True:
										try:
											exit=input('Do you want to exit ? (Y/N) : ')#ask the user to exit or not.
											if (exit == 'Y' or exit == 'y' or exit=='N' or exit=='n'):
												if(exit=='Y' or exit=='y'): #if true the program will exit or else the menu will displayed
													print("GOOD BYE")
												elif(exit=='N' or exit=='n'):
													Menu()
												break
											else:
												print("That entry is not acceptable. Please enter again")
										except:
											continue
								break
							else:
								print("That entry is not acceptable. Please enter again")
						except:
							continue
				break
			else:
				print("That entry is not acceptable. Please enter again")
		except:
			continue

		
def login():
	print("LOGIN")
	login.login_name=input("Enter Name : ")
	if(len(login.login_name)>=3):
		if(login.login_name.isalpha() == True):
			print("Login Successfull")
			print("-------------------------------------------")

		else:
			print("Name should contain only characters")
			print("-------------------------------------------")

			Menu()
	else:
		print("Please add a Longer Name")
		print("-------------------------------------------")

		Menu()
		
		
		
def additionals():
	j=0
	import os.path
	if os.path.isfile(Menu.path):
		j=1		
	else:
		j=0		
	if j==1:
		f=open(Menu.path,'r')
		n=0
		for line in f:
			n=n+1
			if n>5:
				print("["+str(n)+"]	"+line)
		f.close()
		print("     Delivery charge = £1.50\n-------------------------------------------")
		customer_details()  #Here is the menu function where we call the customer detail function from later in the code

	elif j==0:
		print("     Delivery charge = £1.50\n-------------------------------------------")
		customer_details()  #Here is the menu function where we call the customer detail function from later in the code
		

		
def other():
	import os.path
	if os.path.isfile(Menu.path):
		i=1
	else:
		i=0
	f = open(Menu.path , 'a')
	print("-------------------------------------------")
	itemname=input("Enter the name of Pizza :")
	itemprice= input("Enter the price of Pizza: £")
	print("-------------------------------------------")
	if i==0:
		f.write("Mighty Meaty = £6.95\nFunghi with Onions = £4.90\nCheese Feast = £5.75\nChicken and Garlic = £3.50\nSeafood Surprise = £5.30\n")
		f.write(itemname + " = £" +itemprice)

	elif i==1:
		f.write("\n")
		f.write(itemname + " = £" +itemprice)
	
	f.close()
	print("-------------- 10 inch Pizzas -------------- \n[1]	Mighty Meaty = £6.95 \n\n[2]	Funghi with Onions = £4.90 \n\n[3]	Cheese Feast = £5.75 \n\n[4]	Chicken and Garlic = £3.50 \n\n[5]	Seafood Surprise = £5.30\n")
	additionals()
	
Menu()#the memory function displays the menu
