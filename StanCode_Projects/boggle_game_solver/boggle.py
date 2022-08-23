"""
File: boggle.py
Name: Louis
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	while True:
		first_row = input('1 row of letters: ').lower()
		if not input_check(first_row):
			print('Illegal input')
			break
		second_row = input('2 row of letters: ').lower()
		if not input_check(second_row):
			print('Illegal input')
			break
		third_row = input('3 row of letters: ').lower()
		if not input_check(third_row):
			print('Illegal input')
			break
		forth_row = input('4 row of letters: ').lower()
		if not input_check(forth_row):
			print('Illegal input')
			break

		first_row = first_row[0]+first_row[2]+first_row[4]+first_row[6]
		second_row = second_row[0]+second_row[2]+second_row[4]+second_row[6]
		third_row = third_row[0]+third_row[2]+third_row[4]+third_row[6]
		forth_row = forth_row[0]+forth_row[2]+forth_row[4]+forth_row[6]

		letter_list = [first_row]+[second_row]+[third_row]+[forth_row]
		print(letter_list)

		start = time.time()
		find_words(letter_list)

		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')
		break

def find_words(letter_list):
	dictionary_list = read_dictionary()
	ans_list = []
	count = [0]
	for y in range(4):
		for x in range(4):

			find_words_helper(letter_list, letter_list[y][x], [[x, y]], ans_list, dictionary_list, x, y, count)
	print(f'There are {len(ans_list)} words in total.')

def find_words_helper(letter_list, current_string, used_pos_list, ans_list, dictionary_list, x, y, count):
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			x_pos = x + i
			y_pos = y + j
			if 0 <= x_pos < 4:
				if 0 <= y_pos < 4:
					# choose

					used_pos = [x_pos, y_pos]
					if used_pos in used_pos_list:
						pass  # continue
					else:
						used_pos_list.append(used_pos)
						current_string += letter_list[y_pos][x_pos]
						if current_string in dictionary_list:
							if current_string not in ans_list:
								ans_list.append(current_string)
								print(f'Found \"{current_string}\"')
						# explore
						if has_prefix(current_string, dictionary_list):
							find_words_helper(letter_list, current_string, used_pos_list, ans_list, dictionary_list, x_pos, y_pos, count)
						# un-choose

						current_string = current_string[:-1]
						used_pos_list.pop()


def input_check(row):
	if len(row) != 7:
		return False
	else:
		for i in range(len(row)):
			if i % 2 != 0:  # i is even
				if row[i] != ' ':
					return False
			else:
				if not row[i].isalpha():
					return False
		return True

def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary_list = []
	with open(FILE, 'r') as f:
		for word in f:
			word = word.strip()
			if len(word) >= 4:
				dictionary_list.append(word)
	return dictionary_list


def has_prefix(sub_s, dictionary_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
