# A class file for prime 
# numbers in python

# Created By: Stephen Szalajko
# 8/17/2014

# Imported files needed for class
from fractions import gcd

# Class prime
class prime(object):

	# Function that determines if the number is prime or not
	def is_prime(self, n):
		for i in range(2,n):
			if(n % i == 0):
				return False
		return True
		
	# Algorithm that returns a list of prime numbers 
	def sieve_of_eratosthenes(self, limit):
		numbers = range(0, limit ** 2)
		for prime in numbers:
			if prime < 2:
				continue
			elif prime > limit ** 0.5:
				break
			for i in range(prime ** 2, limit, prime):
				numbers[i] = 0
		return [x for x in numbers if x > 1]
	
	# Function that determines if a number is a multiple of four or not
	def multiple_of_four(self, n):
		if(n % 4 == 0):
			return True
		return False
	
	# Function that finds the prime factors of a number greater than or equal to 2
	def prime_factor(self, n):
		i = 2
		index = 0
		N = n
		T = []
		while i**2 < N:
			while N % i == 0:
				N = N / i
				T.append(index)
				T[index] = i
				index += 1
			T.append(index)
			T[index] = N
			index += 1
			i += 1
		return [x for x in T]
	
	# Function that shows if the numbers are relatively prime to eachother
	def relative_prime(self, n, x):
		if(gcd(n,x) == 1):
			return True
		return False
		
