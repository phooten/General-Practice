# problem 1
# start date: [ december 30 2019 ] 
# source:
#		https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/min-max-8/

# Status: INCOMPLETE - [2/23/2020]

# Log:
#-------------------------------------------------------------------
# [1/30/2019]
#	- 
#-------------------------------------------------------------------

# PROJECT NAME
# PROJECT DESCRIPTION
# BUNCH O'FILES

#	PASTE PROBLEM STATEMENT LATER

# HELPFUL NOTES:
# - "b = 12L" - add an "L" or "l" after the number to make variable as long integer

#GLOBAL VARIABLE
min = 0
max = 0

#FUNCTIONS:
def calc(Narray, N):
	# option 1:
	global min
	global max
	for i in range(0, N-1):
		min = min + Narray[i]
		#print(min, "\n")
	
	for i in range(1, N):
		max = max + Narray[i]
		#print(max, "\n")

# all print statements would normally be deleted
print("Input value of N: ")
N = int(input())

print("Input N list (seperate with spaces): ")
 
Narray = list(map(int, input().split()))

calc(Narray, N)
print(min, " ", max)

# print("N: ", N, " Narray: ", Narray)
# print(min, " ", max)


