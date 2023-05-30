import the_best_structure

p = the_best_structure.statistic_counter()
p.add('The is the link to the python package I am trying to compile and install I have tried what I can find online for hours but cannot get over the ImportError')
p.add('is the link to the python package I am trying to compile and install I have tried what I can find online for hours but cannot get over the ImportError''The is the link to the python package I am trying to compile and install I have tried what I can find online for hours but cannot get over the ImportError')
p.add('the link to the python package I am trying to compile and install I have tried what I can find online for hours but cannot get over the ImportError''The is the link to the python package I am trying to compile and install I have tried what I can find online for hours but cannot get over the ImportError')

s = p.get_next()
while(s != ''):
	print(s)
	s = p.get_next()
	
# print(p.get_by_number(10))

# print(p.get_by_pref('package'))