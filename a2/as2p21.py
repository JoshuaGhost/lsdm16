f = open("input.txt", "r+")

collection = ['']
for line in f.readlines():
	for word in line.split(" "):
		if len(word)>3:
			collection[-1] += word+" "
		elif collection[-1] == '':
			pass
		else:
			collection += ['']

for (index, phase) in enumerate(collection):
	if index != len(collection)-1:
		collection[index] += collection[index+1]
print collection