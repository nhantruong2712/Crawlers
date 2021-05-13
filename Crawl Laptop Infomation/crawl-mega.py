from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import openpyxl

processors = []
ram = []
card = []
storage = []
inches = []
warranty = []
descriptions = []
prices = []
hdd_and_ram = []

def crawl():
	for i in range(15, 25):
		req = requests.get("https://mega.com.vn/may-tinh-xach-tay.html?page={}".format(i))  # URL of the website which you want to scrape
		content = req.content  # Get the content
		soup = BeautifulSoup(content, 'html.parser')

		div = soup.find_all('div', {'class': 'p-summary'})
		# print(len(div))
		for i in div:
			try:
				detail = i.find_all("li")
				for j in range(0, len(detail)):
					p = detail[j].text  # Extracting the text from the tags
					if ("CPU" in p):
						processors.append(p.replace("- CPU: ", ""))
						# print("processors: ", processors)
					elif ("RAM" in p):
						hdd_and_ram.append(p)
						for k in hdd_and_ram:
							z = k.replace("- RAM/SSD: ", "").replace("- RAM/ SSD: ", "").replace("- RAM/ HDD: ", "").replace(
								"- RAM/ Ổ CỨNG: ", "").replace("- RAM/SSD+HDD: ", "")
							y = z.replace("- RAM/SSD:", "").replace("- RAM/ SSD:", "").replace("- RAM/ HDD:", "").replace(
								"- RAM/ Ổ CỨNG:", "").replace("- RAM/SSD+HDD:", "")
							t = y.split("/")
							t.append(t)
							ram.append(t[0])
							storage.append(t[1])
							# print("ram: ", ram)
					# If RAM is present in the text then append it to the ram list. Similarly do this for the other features as well
					# elif ("HDD" in p or "SSD" in p or "Ổ cứng" in p):
					# 	storage.append(p.replace("Ổ cứng: ", ""))
					# 	# print("storage: ", storage)
					elif ("VGA" in p):
						card.append(p.replace("- VGA: ", ""))
						# print("card: ", card)
			except:
				ram.append("--")
				storage.append("--")
				processors.append("--")
				card.append("--")
				inches.append("--")


		price = soup.find_all('span', class_='p-price')
		# Extracting price of each laptop from the website
		for i in range(len(price)):
			prices.append(price[i].text)
		# print("prices:", prices)

		desc = soup.find_all('a', class_='p-name')

		for i in desc:
			if ('15.6 inch' in i.text or ',15.6 inch' in i.text):
				inches.append('15.6')
			elif ('14.0 inch' in i.text or ',14 inch' in i.text or '14 inch' in i.text):
				inches.append('14')
			elif ('12.5 inch' in i.text or ',12.5 inch' in i.text):
				inches.append('12.5')
			elif ('18.4 inch' in i.text):
				inches.append('18.4')
			elif ('13.3 inch' in i.text or ',13.3 inch' in i.text):
				inches.append('13.3')
			elif ('13 inch' in i.text or ',13 inch' in i.text):
				inches.append('13')
			elif ('13.5 inch' in i.text):
				inches.append('13.5')
			elif ('17.3 inch' in i.text):
				inches.append('17.3')
			elif ('16.0 inch' in i.text):
				inches.append('16')
			elif ('10 inch' in i.text):  
				inches.append('10')
			elif ('14.5 inch' in i.text):  
				inches.append('14.5')
			elif ('11.6 inch' in i.text):
				inches.append('11.6')
			elif ('17 inch' in i.text):
				inches.append('17')
			else:
				inches.append("No")

		for i in range(len(desc)):
			descriptions.append(desc[i].text)
	save()

def save():
	a = {'Description':descriptions,'Processor':processors,'RAM':ram,'Card':card,'Storage':storage,'Display':inches,'Price':prices}
	df = pd.DataFrame.from_dict(a, orient='index')
	df = df.transpose()
	dataset = pd.DataFrame(data=df)
	dataset.to_excel('laptops-mega-1.xlsx')

if __name__ == '__main__':
	crawl()