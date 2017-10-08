#!/usr/bin/python3

import sys
import os
import shutil
import smtplib
import stat
import getpass
from email.mime.text import MIMEText

class submit:

	def instruct(self):

		self._target = input("Please enter the name of the file you want to submitted.\n")
		self._email = input("Please enter your email address for a receipt. \n")

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

		msg = MIMEText("You submiited file {} sussfully, please do not reply to this email!".format(self._target))

		# me == the sender's email address
		# you == the recipient's email address
		msg['Subject'] = 'DoNotReply Submission Successfully'
		msg['From'] = 'THISISFAKESENDER'
		msg['To'] = self._email

		# Send the message via our own SMTP server, but don't include the
		# envelope header.
		s = smtplib.SMTP('localhost')
		s.send_message(msg)
		s.quit()

			

def main():
	mysubmission = submit()
	mysubmission.instruct()
	mysubmission.submitWork()
	print("Bye-Bye\n") 


if __name__ == "__main__":main()



