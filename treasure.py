__author__ = 'akovinenko'

import os


#Simple function
def treasure_path(array, cur='11'):
	result = ''
	while True:
		if (int(cur[0]) > 5) or (int(cur[1]) > 5) or (int(cur[0]) < 1) or (int(cur[1]) < 1):
			return 'Error: out of range: ' + result + cur
		if cur == array[int(cur[0])-1][int(cur[1])-1]:
			return result + cur
		if cur not in result:
			result += cur + ' '
			cur = array[int(cur[0])-1][int(cur[1])-1]
		else:
			return 'Error: Endless path: ' + result + cur

#Closure
def closure_treasure_path(array, cur='11'):
	def treasure_path(cur='11'):
		result = ''
		cur = cur
		while True:
			if (int(cur[0]) > 5) or (int(cur[1]) > 5) or (int(cur[0]) < 1) or (int(cur[1]) < 1):
				return 'Error: out of range: ' + result + cur
			if cur == array[int(cur[0])-1][int(cur[1])-1]:
				return result + cur
			if cur not in result:
				result += cur + ' '
				cur = array[int(cur[0])-1][int(cur[1])-1]
			else:
				return 'Error: Endless path: ' + result + cur
	return treasure_path

#Recursion
def rec_treasure_path(array, cur = '11'):
	return cur if cur == array[int(cur[0])-1][int(cur[1])-1] else cur + ' ' + rec_treasure_path(array, array[int(cur[0])-1][int(cur[1])-1])

#Object-oriented way
class Treasure(object):
	def __init__(self, array):
		super(Treasure, self).__init__()
		self.array = array

	def rec_treasure_path(self, cur = '11'):
		return cur if cur == self.array[int(cur[0])-1][int(cur[1])-1] else cur + ' ' + rec_treasure_path(self.array, self.array[int(cur[0])-1][int(cur[1])-1])
		


if __name__ == '__main__':
	input_1 = '''55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15'''
	
	input_2 = '''34 21 32 41 25
14 42 43 14 31
54 45 52 42 23
33 15 51 31 35
21 52 33 13 23'''

	array_1 = [x.split(' ') for x in input_1.split('\n')]
	array_2 = [x.split(' ') for x in input_2.split('\n')]
	
	#Simple function
	print(treasure_path(array_1))

	#Closure
	func = closure_treasure_path(array_2)
	print(func())
	
	#Recursion
	print(rec_treasure_path(array_1))

	#Read from file (if file 'input.txt' exists)
	if os.path.exists('input.txt'):
		with open('input.txt', 'r') as file:
			array_3 = [x.split(' ') for x in file.read().splitlines()]
			print(rec_treasure_path(array_3))

	#Object-oriented way
	T = Treasure(array_3)
	print(T.rec_treasure_path())