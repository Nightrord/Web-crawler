import requests
import bs4

response = requests.get('http://brickset.com/sets/year-2016/page')
soup = bs4.BeautifulSoup(response.text, "html.parser")
# for item in soup.find_all("div", class_="meta"):
# 	print (item.h1.a.get_text().split(' ', 1)[1].replace(" ", ""))

for item in soup.find_all("article"):
	# print (item.div.h1.a.get_text())
	meta = item.find("div", class_="meta")
	# print (name.h1.a.get_text())
	print ("Name:", meta.h1.a.get_text().split(' ', 1)[1].replace(" ", ""))
	col = meta.find("div", class_="col")
	dts = col.find_all("dt")
	for dt in dts:
		if dt.get_text() == "Pieces":
			print ("Pieces", dt.next_sibling.a.get_text())
		if dt.get_text() == "Minifigs":
			print("Minifigs", dt.next_sibling.a.get_text())
	print ("-----------------")
