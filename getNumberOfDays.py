"""
Script Name: getNumberOfDays.py
Date: 09/03/2017

Description: This program Prompts for Input from user. Below are the input prompts -
-- Name of the User
-- DoB of the User in format (MM/DD/YYYY)

The program prints the age of the user in number of days.
"""
import datetime as dt
import time



def fetch_user_input ():
	"""
	This function will prompt the user for the below inputs:
	-- User name
	-- User Date of Birth
	The function will validate the inputs, and will return a tuple object with both the inputs.
	The function will return None, if the user chose to quit 
	"""
	#Prompt user for Name
	user_name = input("Please enter your name : ")
	#Prompt user for DoB
	user_dob = input("Please enter your Date of Birth in format - MM/DD/YYY  : ")
	#Initializing flags
	is_input_correct=False
	attempt_number=1
	user_quit = 0

	#Loop to capture correct inputs from user
	while not is_input_correct and user_quit!=1:
		#Validate the input arguments
		try:
			valid_date = time.strptime(user_dob, '%m/%d/%Y')
			is_input_correct=True
		except Exception as e:
			if attempt_number < 4:
				print('uh-oh! Looks like you entered a wrong date \n\n\t {} try entering your birthdate in the format - MM/DD/YYYY'.format(user_name+','))
				user_dob=input("Date of Birth : ")
				attempt_number+=1
				is_input_correct=False
				continue
			else:
				print ('Hmm... Looks like you things are just not going right.. Do you want to quit now and try again?')
				user_quit=int(input('Enter 1 for quit or any other number to continue : '))
				if user_quit != 1:
					user_dob = input("Please enter your Date of Birth in format - MM/DD/YYY  : ")
				attempt_number=1
	
	#Return the input arguments back
	if user_quit!=1:
		return [user_name,valid_date]
	else:
		return None



user_input=fetch_user_input()

#print(user_input)





