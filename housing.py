import urllib2, time
from bs4 import BeautifulSoup

def call():
	url = "https://housing6.res.jhu.edu/General/Count2.html"
	soup = BeautifulSoup(urllib2.urlopen(url).read(),"html.parser")
	table = soup.find('tbody')
	rows = table.findAll('tr')
	priorities = ["14","00","15","05","13","10","11","21","24","12","18","26","27"]
	print "Priority Low to High"
	priorities.reverse()
	timenow = time.strftime("%H_%M_%S")
	for num in priorities:
		search(rows, num, timenow)
		
	print "Current time is: " + time.strftime("%H:%M:%S")

	with open(timenow+".txt", 'a') as f:
		f.write("Current time is: " + time.strftime("%H:%M:%S"))

	

def search(rows, num, timenow):
	with open(timenow+".txt", 'a') as f:
		for tr in rows:
			cols = tr.findAll('td')
			if "11 month" not in cols[4].text:
				for td in cols:
					if "Commons" in td.text and len(td.text)<25 and num in td.text and td.text[len(td.text)-1]=="A":
						print td.text[18:-1]
						f.write(td.text[18:-1]+"\n")

while (True):
	call()
	time.sleep(10)
