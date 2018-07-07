#!/usr/bin/env python3
import re, sys

def isPhoneNumber(text):
	#we want to mathc pohen numbers but separate them from their 
	#regional codes (e.g., (+591))
	regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
	result = regex.findall(text)
	if result is not None:
		print(result)
		return True

if __name__ == '__main__':
	file_name = sys.argv[1]
	with open(file_name) as f:
		for line in f:
			print(isPhoneNumber(line))



