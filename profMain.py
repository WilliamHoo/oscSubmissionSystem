#!/usr/bin/python3

import sys
import os
import shutil
import fileinput 
import getpass
import stat
import pwd 

class workManager:

	def readComd(self):

		print("1. Create a new directory for assignment. \n2. Create submission command. \n3. Display all my files. \n4. Quit.")
		self._command  = input(">> ")

	def createDirec(self):
		while(1):
			path = input("Please enter the path for your directory. Press enter to create under current folder.\n")
			direcName = input("Please enter the name for your directory.\n")
			if (path!=""):
				os.chdir(path)	
			if not os.path.exists(direcName):
				os.makedirs(direcName)
				break
			else:
				print("The directory is already exist, please enter another one. ")

		currentPath = os.path.abspath(direcName)
		target = getpass.getuser()
		self.addGroupPermission(getpass.getuser(), currentPath)
		print("Successfully created your directory.\n")

	def createSubmitComd(self):

		print("Please enter the file name you wish to use.")
		self.displayFile()
		filename = input(">> ")
		email = input("Please enter your email for email servies.\n ")
		
		destination = os.getcwd() + "/{}".format(filename)
		shutil.copyfile("os.py","submit.py")
		currentPath = os.getcwd() + "/submit.py"

		
		os.chdir(destination)
		shutil.move(currentPath, destination)
		destination = destination + "/submit.py"

		fakePath = "THiSISFAKEPATH"
		fakeSender = "THISISFAKESENDER"

		with fileinput.FileInput("submit.py", inplace=True) as file:
			for line in file:
				print(line.replace(fakePath,destination).replace(fakeSender,email), end='')

		currentPath = os.getcwd() + "/submit.py"

		os.chmod(currentPath,stat.S_IRWXU | stat.S_IXGRP | stat.S_IRGRP | stat.S_IXOTH)

		print("Below is the path to run your program.")
		print(currentPath)

	def displayFile(self):

		print("Here are all your files: \n")
		files = [f for f in os.listdir('.') if not os.path.isfile(f)]
		for f in files:
			print(f)

	def addGroupPermission(self,target,currentPath):
		tail = os.path.basename(currentPath)
		head = os.path.dirname(currentPath)
		os.chmod(tail,stat.S_IRWXU | stat.S_IWGRP | stat.S_IXGRP | stat.S_IXOTH)
		while (tail != target):
			st = os.stat(head)
			os.chmod(head, st.st_mode | stat.S_IXGRP)
			tail = os.path.basename(head)
			head = os.path.dirname(head)

def main():

	username = getpass.getuser()
	print("Welcome, {}!\n".format(username))
	myWork = workManager()
	myWork.readComd()

	while (1):
		if (myWork._command == "1"):
			myWork.createDirec()
		elif (myWork._command == "2"):
			myWork.createSubmitComd()
		elif (myWork._command == "3"):
			myWork.displayFile()
		elif (myWork._command == "4"):
			break
		else:
			print("Error message!")
		
		print()
		myWork.readComd()

	print("Bye-Bye\n") 


if __name__ == "__main__":main()



