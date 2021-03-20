import random

def random_password(count):
	simbols = []

	for i in range(33, 127):
	    simbols.append(chr(i))

	result = ''

	for i in range(count):
		result += random.choice(simbols)

	return result

def string_procent_difference(str1, str2):
	str3 = ''
	str4 = ''

	for i in range(len(str2)):
		new = str3 + str2[i]
		if new in str1:
			str3 += str2[i]
		else:
			str4 += str2[i]

	result = (len(str3) * 100 / len(str1)) - (len(str4) * 100 / len(str1))

	return result

def search_tag(text, services_keys, all_service, END):
	text = text.replace('#', '')
	
	top_value = 0
	top = []

	for s in services_keys:
		condidate = string_procent_difference(s, text)
		if condidate > top_value:
			top_value = condidate
			s = s.replace(text, text.upper())
			top.insert(0, "> " + s)
		else:
			top.append(s)

	if top:
		all_service.delete(1.0, END)
		all_service.config(fg='#00FFFF')
		all_service.insert(1.0, '\n'.join(top))	