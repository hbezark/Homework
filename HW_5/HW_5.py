import re

fhand = open('regex_sum_31515.txt')
empty_lst = []
for line in fhand:
	line = line.rstrip()
	words = re.findall('([0-9]+)', line)

	if len(words) > 0:
		value = sum(map(int, words))
		empty_lst.append(value)
count = 0
for number in empty_lst:
	count += number
print (count)