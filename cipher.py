import random
import textwrap

from MainWindow import Ui_MainWindow

size = random.randint(3,5)
n = random.randint(50,53)
m = random.randint(300,400)
some_str = 'hello'

def generateSuperIncreasingKnapsack(size):
	first = random.randint(2, 2+size)
	knapsack = [first]
	sum = first
	for i in range(size-1):
		element = sum + random.randint(1, size)
		knapsack.append(element)
		sum += element
	return knapsack

def public_key(private_key, n, m):
    suma = sum(private_key)
    if suma >= m:
        raise AttributeError('m value should be greater then sum of private key')
    return [(k*n)%m for k in private_key]

def plain_text_to_binary(plain_text):
	binary_str = ''.join(format(ord(x), 'b') for x in plain_text)
	binary_str = textwrap.wrap(binary_str,size)
	return binary_str

def checking_for_last_element(binary_str):
	last_element = list(binary_str.pop())
	while len(last_element) < size:
		last_element.insert(0, '0')
	new_string = ''.join(last_element)
	binary_str.append(new_string)
	return binary_str

def encryption(public_key, number_list):
	result = []
	for i in range(len(number_list)):
		result.append(0)

	for i in range(len(number_list)):
		for j in range(len(public_key)):
			result[i] += public_key[j] * number_list[i][j]
	return result



private_key = generateSuperIncreasingKnapsack(size)
public_key = public_key(private_key, n, m)
print(private_key)
print("n is {}".format(n))
print("m is {}".format(m))
print(public_key)
binary_str = plain_text_to_binary(some_str)
print('Это бинарный текст', binary_str)
binary_str = checking_for_last_element(binary_str)
print('Это бинарный текст с проверенным последним элементом', binary_str)


binary_list = [list(d) for d in binary_str]
number_list = [[int(y) for y in x] for x in binary_list]
print(number_list)
# new_list = [list(x) for x in binary_str]s
# print(new_list)

encrypted_text = encryption(public_key, number_list)
print("Зашифрованное сообщение", encrypted_text)

# last_element = binary_str.pop()
# print(last_element)
# last_element = list(last_element)
# while len(last_element) < size:
# 	last_element.insert(0,'0')
# new_string = ''.join(last_element)
# print('Преобразованный элемент', new_string)
# binary_str.append(new_string)
# print("Окончательный список", binary_str)
	