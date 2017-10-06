#!/usr/bin/python3

import sys
import os
import shutil
import smtplib
import stat
import getpass

class submit:

	def instruct(self):

		self._target = input("Please enter the name of the file you want to submitted.\n")
		self._email = input("Please enter your email address for a receipt. \n")
		self._emailps = getpass.getpass("Please enter the password of your email address. \n")

	def submitWork(self): 

		path = "THiSISFAKEPATH"
		submissionP = os.getcwd() + "/{}".format(self._target)
		os.chmod(submissionP,stat.S_IRWXU | stat.S_IRWXG)
		target = os.path.join(os.path.dirname(path),self._target)
		for root, dirs, files in os.walk(submissionP):
			for d in dirs:
				os.chmod(os.path.join(root, d), stat.S_IRWXU | stat.S_IRWXG)
			for f in files:
				os.chmod(os.path.join(root, f), stat.S_IRWXU | stat.S_IRWXG)		
		shutil.copytree(submissionP,target)
		os.chmod(submissionP,stat.S_IRWXU)
		for root, dirs, files in os.walk(submissionP):
			for d in dirs:
				os.chmod(os.path.join(root, d), stat.S_IRWXU)
			for f in files:
				os.chmod(os.path.join(root, f), stat.S_IRWXU)
		print("You've submitted your work successfully.\n")
		self.email()

	def email(self):

		message = """From: From Person <from@fromdomain.com>
		To: To Person <to@todomain.com>
		Subject: SMTP e-mail test

		This is a test e-mail message.
		"""

		try:
		   smtpObj = smtplib.SMTP("localhost")
		   smtpObj.login(self._email,self._emailps)
		   smtpObj.sendmail(self._email, self._email, message)         
		   print("Successfully sent email.")
		except smtplib.SMTPException:
		   print("Error: unable to send email.")
			

def main():
	mysubmission = submit()
	mysubmission.instruct()
	mysubmission.submitWork()
	print("Bye-Bye\n") 


if __name__ == "__main__":main()



