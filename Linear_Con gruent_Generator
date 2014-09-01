# New trial for Random Number Generator 1
# Written by: Stephen Szalajko
# Date: 8/17/2014

# first, randomize numbers from zero to (n-1) + n. Then, subtract by n. 

# First trial in creating a random 
# number generator for myself. So
# far, not a good random number 
# generator. There is a sort of a 
# pattern, if you can tell. It 
# repeats by whatever b is. Not too 
# good. Maybe, randomize b. Might work.
# Also, The random numbers here can 
# repeat, so it's not good for Monte
# Carlo analysis.

# import useful files
from random import randint, choice
from prime import prime
import random

# Warning for the user
print """
	Before we do anything, note that 
	you will have to give an initial 
	value before executing. 
	Make sure it is large. Otherwise,
	it will not be as consecutively 
	random.
	"""

# User input information
print "." * 100
print "How many random numbers do you want?"
n = int(raw_input('> '))
print "." * 100
print "Do you want the random numbers fixed in the range of the amount of random numbers that you wanted? (y/n)"
random_number_ranged = raw_input('> ')
print "." * 100

# Instance of prime object
thatnumber = prime()

# Initialization of variables and constants
a = randint(0, n ** 2)
b = randint(0, n ** 2)
initial1 = randint(0, n)
SEED = randint(0, 1000)
random.seed(SEED) 
N = n
i = 0
x = []
y = []

# Assign important functions nessisary for the operation. 
def sign_convention():
    return choice([True, False])
	
def shuffle_n_value(n):
	if(n < 4):
		return randint(4, 100)
	else:
		return randint(4, 2 * n)

def increment_B_function(b, n):
	relative_prime_flag = True
	while relative_prime_flag:
		if(thatnumber.relative_prime(n, b)):
			relative_prime_flag = False
			return b
		else:
			prime_number_array = thatnumber.sieve_of_eratosthenes(n)
			indexofprimearray = randint(0, len(prime_number_array) - 1)
			b = int(prime_number_array[indexofprimearray])
			
def multiplier_A_function(a, n):
	A = a - 1
	N = n
	multiplier_function_flag = True
	if(thatnumber.multiple_of_four(n)):
		multiple_list_of_four = range(4, 4 * n, 4)
		index = randint(0, len(multiple_list_of_four) - 1)
		A = int(multiple_list_of_four[index])
		a = A + 1
		return a
	else:
		prime_factor_flag = True
		prime_factor_of_N = list(set(thatnumber.prime_factor(n)))
		prime_factor_of_A = list(set(thatnumber.prime_factor(A)))
		length_of_N = len(prime_factor_of_N)
		while prime_factor_flag:
			if(len(prime_factor_of_N) == len(prime_factor_of_A)):
				for i in range(len(prime_factor_of_N)):
					if(prime_factor_of_N[i] == prime_factor_of_A[i]):
						if(i == length_of_N):
							prime_factor_flag = False
						continue
					else:
						length_of_prime_numbers_for_A = randint(len(prime_factor_of_N), N)
						for j in range(length_of_prime_numbers_for_A):
							index_for_N = randint(0, len(prime_factor_of_N) - 1)
							A *= prime_factor_of_N[index_for_N]
						prime_factor_flag = False
			else:
				length_of_prime_numbers_for_A = randint(len(prime_factor_of_N), N)
				for k in range(length_of_prime_numbers_for_A):
					index_for_N = randint(0, len(prime_factor_of_N) - 1)
					A *= prime_factor_of_N[index_for_N]
				prime_factor_flag = False
		a = A + 1
		return a

print (" ")

# Code to work on linear congruent generator
while i < n:

# initial value
	if (i == 0):
		x.append(i)
		y.append(i)
		x[0] = initial1
		y[0] = initial1
		print x[0]
	elif (i > 0):
		x.append(i)
		y.append(i)
# Selection if the range is not within the bounds.
		if(random_number_ranged == 'y'):
			N = shuffle_n_value(N)
		x[i] = ((multiplier_A_function(a, N) * x[i - 1]) + increment_B_function(b, N)) % (N)
		y[i] = x[i]
# Sign for 2's compliment.
		if (sign_convention()):
			y[i] = -1 * x[i]
			print y[i]
		else:
			print y[i]
	i += 1
