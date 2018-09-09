import requests
from bs4 import BeautifulSoup


def get_table():
	url = "https://www.geeksforgeeks.org/gate-cs-notes-gq/"
	source = requests.get(url)
	soup = BeautifulSoup(source.text, features="html5lib")
	table = soup.findAll('table')[0]
	return table


def subjects_maker(tabu):
	tableMain = get_table()
	subjects = dict()
	for i in tableMain.findChildren('tr')[1:]:
		for j in i.findChildren('td')[0].text.strip().split('\n'):
			if j.startswith('Section '):
				subjects[j.split(": ")[1]] = 0
	for i in tableMain.findChildren('a'):
		if i.attrs['href'].find('geeksforgeeks.org') != -1:
			i.attrs['class'] = 'tarGet'
		else:
			par = i.findParent()
			par.clear()
	num = 0
	keys = list(subjects.keys())
	for i in tableMain.findChildren('tr')[1:]:
		subjects[keys[num]] = i.findChildren('td')[tabu+1].findChildren('ol')[0]
		# subjects[keys[num]] = str(subjects[keys[num]])
		num += 1
	return subjects


if __name__ == "__main__":
	print("Won't do it!!")
	# subjects = subjects_maker()
	# print(subjects)
