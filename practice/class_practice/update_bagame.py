import sys
import time

def enemy():
	theday = input("which year:")
	myday = int(theday)
	if 2020 - myday >= 5:
		print("reconciliation?")
	else:
		print("oh! I have to escape!wait....")
		for i in range(2):
			print(".")
			time.sleep(0.5)
		time.sleep(1)
		sys.exit()

print("um~~Sun poke out again~~. Who want to visiting my farm?")

class VISITWHO():
	def __init__(self, name, gender, relation):
		self.name = name
		self.gender = gender
		self.relation = relation
	def farmer(self, income, pay):
		sdd1 = 100
		if not self.relation == "friend":
			if income < sdd1:
				print("keep going!")
			else:
				print("welcome!")
			if pay >= sdd1:	# 印出"--. --- --- -..   -... --- -.--"
				print("--. --- --- -..   -... --- -.--")
			else:
				print("get out!")
		if self.relation == "friend":
			print("my friend!come in!")
		if self.relation == "mistress":
			ask = input("Do you wnat to mess here? if no, give me a punch:")
			if not ask == "0":
				print("you")
				for i in range(1):
					time.sleep(1)
					print(".")
				time.sleep(1)
				sys.exit()
			else:
				print("fine.come in, my customer.")
		if self.relation == "enemy":
			enemy()
		if self.relation == "no":
			print("who are you?")
			name = input("your name?:")
			gender = input("your gender?:")
			relation = input("what is our relation?:")
			if not type(name) == "<class 'str'>":
				new = VISITWHO(name,gender,relation)
				print("I got the new member.")
			else:
				print("Don't mess around!")


# 規則
# 性別可以填: male female
# 關係可以填: friend mistress enemy no

#I = VISITWHO("請輸入名字","請輸入性別","請輸入跟農場主人的關係")
#I.farmer(請輸入你的收入,請輸入你想付給農場主人多少錢)