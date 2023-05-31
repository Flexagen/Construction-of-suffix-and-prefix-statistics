import statistics

p = statistics.statistic_counter()
p.add('The is the link to the python package')
p.add('is the link to the python package I ')
p.add('the link to the python package I am')

s = p.get_next()
while(s != ''):
	print(s)
	s = p.get_next()
	
print(p.get_by_number(10))

print(p.get_by_pref('package'))