import itertools as its
from collections import Counter

# Function to determine whether or not a pair is less than another one
def less(pair):
	a, b = pair
	if a[0] < b[0] and a[1] < b[1]:
		return True
	else:
		return False

# Function to calculate the Alexander grading s
def A(state):
	s = 0

	# Given the state, look up the winding number in grid and add to s
	for i in range(5):
		idx = state[1][i]
		s += grid[i][idx]
	
	# Calculate the final grade and return it
	grade = -1 * s - 5
	return grade

# Function to calculate the Maslov grading d
def M(state):
	J_xx, I_Ox, I_xO = 0, 0, 0
	Os = [(i + .5, 4.5 - i) for i in range(0, 5)]
	coords = list([(state[0][i], state[1][i]) for i in range(5)])
	
	# Comparisons between ordered pairs of coordinates
	comps = its.permutations(coords, 2)
	for pair in comps:
		if less(pair):
			J_xx += 1

	# Comparisons between the coordinates and Os
	comps2 = its.product(Os, coords)
	for pair in comps2:
		if less(pair):
			I_Ox += 1

	# Comparisons between the Os and coordinates.
	comps3 = its.product(coords, Os)
	for pair in comps3:
		if less(pair):
			I_xO += 1

	# Do some final calculation, and then return the grade
	J_xO = (I_xO + I_Ox) / 2
	grade = J_xx - 2 * J_xO + 1
	return int(grade)

# These are the winding numbers of the T_{2,3} grid; grid[x][y] <-> (x,y)
grid = [[0, 0, 0, 0, 0, 0], [0, 0, -1, -1, -1, 0], [0, -1, -2, -2, -1, 0], [0, -1, -2, -1, 0, 0], [0, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

# Generate the possible permutations
base = (0, 1, 2, 3, 4)
perms = list(its.permutations(base))

# Create all the states
states = []
for i in perms:
	states.append([base, i])

# Calculate the Alexander and Maslov gradings for each state, and append them to each state
for i in range(len(states)):
	a = A(states[i])
	m = M(states[i])
	states[i] = [states[i], a, m]

# For a given Alexander grading s, create an array with the possible Maslov gradings
s = 1
maslovs = []
for i in states:
	if i[1] == s:
		maslovs.append(i[2])
print(Counter(maslovs))
