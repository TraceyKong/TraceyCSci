Notes on loop 

~~~~while loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def string(s):
	l = len(s)
	return(l)

string('abcd') returns the length of the string +=



def string(s):
	l = len(s)
	i = 0
	while i<l:
		result += s[:i+1]
		i += 1
	return result

string('abc') returns 'aababc'


~~~~~for loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def string_for(s):
	l = len(s)
	result = ''
	for i in range(l):
		result += s[:i+1]
	return result

string_for('abc') returns 'aababc'


