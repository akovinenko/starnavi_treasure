__author__ = 'akovinenko'

import treasure
from treasure import Treasure

test_input_1 = '''55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15'''

test_output_1 = '11 55 15 21 44 32 13 25 43'

def test_treasure_path():
	assert treasure.treasure_path([x.split(' ') for x in test_input_1.split('\n')]) == test_output_1

def test_rec_treasure_path():
	assert treasure.rec_treasure_path([x.split(' ') for x in test_input_1.split('\n')]) == test_output_1

def test_closure_treasure_path():
	assert treasure.closure_treasure_path([x.split(' ') for x in test_input_1.split('\n')])() == test_output_1

def test_class_treasure():
	T = Treasure([x.split(' ') for x in test_input_1.split('\n')])
	assert T.rec_treasure_path() == test_output_1