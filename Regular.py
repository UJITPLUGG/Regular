import re

string = "Завтрак будет в 16:00 Футбольный счет 24:30"

class main():
	def __init__(self,string):
		words = string.split(" ")

		for word in words:
			time = re.findall(r"[0-2][0-9]:[0-6][0-9]",word)
			if len(time) < 1:
				continue
			if int(time[0].replace(":","")) < 2400:
				print(time[0])

if __name__ == "__main__":
	main(string)
