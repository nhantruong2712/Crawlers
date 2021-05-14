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

def crawl():
	for i in range(1, 19):
		req = requests.get("https://www.hanoicomputer.vn/laptop-may-tinh-xach-tay/{}/".format(i))  # URL of the website which you want to scrape
		content = req.content  # Get the content
		soup = BeautifulSoup(content, 'html.parser')

		div = soup.find_all('div', {'class': 'p-info'})
		# print(len(div))
		for i in div:
			# div2 = i.find('div', {'class': 'productSummary2021'})
			detail = i.find_all("li")
			if len(detail) > 3:
				# print(detail)
				for i in range(len(detail)):
					p = detail[i].text  # Extracting the text from the tags
					if len(p) > 0:
						if ("CPU" in p):
							processors.append(p.replace("CPU: ", ""))
						elif ("RAM" in p):
							ram.append(p.replace("RAM: ", ""))
							# print("ram: ", ram)
						# If RAM is present in the text then append it to the ram list. Similarly do this for the other features as well
						elif ("HDD" in p or "SSD" in p or "Ổ cứng" in p):
							storage.append(p.replace("Ổ cứng: ", ""))
							# print("storage: ", storage)
						elif ("VGA" in p):
							card.append(p.replace("VGA: ", ""))
							# print("card: ", card)
						elif ("Màn hình" in p):
							inches.append(p.replace("Màn hình: ", ""))
							# print("inches: ", inches)
			else:
				pass
		price = soup.find_all('span', class_='p-price js-get-minPrice')
		# Extracting price of each laptop from the website
		for i in range(len(price)):
			prices.append(price[i]['data-price'])
		# print("prices:", prices)

		desc = soup.find_all('h3', class_='p-name')

		for i in range(len(desc)):
			descriptions.append(desc[i].text)
		# print("descriptions: ", descriptions)
	save()

def save():
	a = {'Description':descriptions,'Processor':processors,'RAM':ram,'Card':card,'Storage':storage,'Display':inches,'Price':prices}
	df = pd.DataFrame.from_dict(a, orient='index')
	df = df.transpose()
	dataset = pd.DataFrame(data=df)
	dataset.to_excel('laptops-hanoicomputer1.xlsx')

if __name__ == '__main__':
	crawl()