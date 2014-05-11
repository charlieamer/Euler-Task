from pictureShower import pictureShower
import mechanize
import re
from bs4 import BeautifulSoup as bs
from random import random
import traceback, os

class EulerTask:

	"""
    * Importing the class:
    from EulerTask import EulerTask
    
    * Submit solution:
    EulerTask('username', 'password').setProblem(ProblemNumber).solve(MySolution)
    
    * Print problem statement:
    EulerTask('username', 'password').setProblem(ProblemNumber).printProblemStatement()
    
    * Print problem statement and submit solution:
    EulerTask('username', 'password').setProblem(ProblemNumber).printProblemStatement().solve(MySolution)
    """


	def __init__(self, username, password, threadText = "Default", forceSubmit = False):
		self.agent = mechanize.Browser()
		self.username = username
		self.password = password
		self.threadText = threadText
		self.forceSubmit = forceSubmit
		print('Going to the project euler login page ...')
		self.agent.open('http://projecteuler.net/login')
		print('Logging in ...')
		self.agent.select_form('login_form')
		self.agent.form.find_control('username').value = self.username
		self.agent.form.find_control('password').value = self.password
		self.response = self.agent.submit().read()
		if 'If you have not already created an account then please' in self.response:
			raise Exception('Invalid username / password')

	def setProblem(self, problem):
		self.problem = str(problem)
		print('Getting task number '+self.problem+' ...')
		self.response = self.agent.open('http://projecteuler.net/problem='+self.problem).read()
		return self

	def printProblemStatement(self):
		resp = bs(self.response).find(class_ = "problem_content").get_text()
		print ("#######################################")
		print ("Text:")
		print (resp)
		print ("#######################################")
		return self

	def solve(self, solution):
		solution = str(solution)
		try:
			self.unique = str(random())
			self.captcha =  'http://www.projecteuler.net/' + self.response.split()[self.response.split().index('document.captcha.src')+2][1:-1] + self.unique
			self.captcha = self.captcha.split('&')[0]
			self.agent.select_form(nr=0)
			self.agent.form.find_control('guess_'+self.problem).value = solution
			pictureShower(self.captcha, self.agent._ua_handlers['_cookies'].cookiejar)
			#numbers = ""
			try:
				numbers = raw_input("Enter numbers from above: ")
			except NameError:
				numbers = input("Enter numbers from above: ")
			self.agent.form.find_control('confirm').value = numbers
			self.response = self.agent.submit().read()
			if 'Confirmation Code:' in self.response: raise Exception('Invalid captcha code')
			print ("#######################################")
			if 'incorrect' in self.response:
				print ("The answer '"+solution+"' was INCORRECT")
			else:
				print ("The answer '"+solution+"' was CORRECT")
				if self.threadText is not None: self.solutionToThread()
			print ("#######################################")
		except ValueError:
			print ("ERROR: You already solved this problem")
			if self.threadText is not None and self.forceSubmit: self.solutionToThread()
		return self

	def solutionToThread(self):
		print("Fetching thread ... (Don't want this ? Visit https://github.com/charlieamer/Euler-Task/blob/master/Automatic%20solution%20submission%20FAQ.md)")
		mpath = os.path.realpath(__file__).replace('.pyc','.py')
		for stack in traceback.extract_stack()[::-1]:
			if not mpath == os.path.realpath(stack[0]):
				try:
					self.agent.open('http://projecteuler.net/new_post='+self.problem)
					self.agent.select_form(nr = 0)
					txt = open(os.path.realpath(stack[0]),'r').read()
					txt = txt.replace(self.username,'YOUR USERNAME HERE').replace(self.password,'YOUR PASSWORD HERE')
					if self.threadText == "Default":
						self.threadText = ("My solution in python:\n"
						"Solution was submitted with the project Euler-Task: [url]https://github.com/charlieamer/Euler-Task[/url]\n"
						"[code=python]%s[/code]")
					self.agent.form.find_control('message').value = self.threadText%txt
					print('Submitting your solution to thread ...')
					self.agent.submit()
				except IOError:
					print("Error opening file :(")
				except mechanize._mechanize.FormNotFoundError:
					print("ERROR: You already wrote in this thread")
				finally:
					break
		return self


		
if __name__=="__main__":
        print(help(EulerTask))