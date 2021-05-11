import threading

import keyboard as keyboard
import msvcrt
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl


name_stores = []
types = []
quality_points = []
price_points = []
service_points = []
placement_points = []
space_points = []
addresses = []
average_points = []
average_prices = []

def save():
	a = {'Stores': name_stores, 'Addresses': addresses, 'Types': types, 'Quality Points': quality_points,
		 'Price Points': price_points,
		 'Space Points': space_points, 'Service Points': service_points, 'Placement Points': placement_points,
		 'Average Points': average_points, 'Average Price': average_prices}

	df = pd.DataFrame.from_dict(a, orient='index')
	df = df.transpose()
	dataset = pd.DataFrame(data=df)
	dataset.to_excel('foody-stores.xlsx')

def find():
	name_store = browser.find_element_by_css_selector(".main-info-title h1")
	name_stores.append(name_store.text)
	print("name_stores: ", name_stores)

	try:
		kind_of_store_1 = browser.find_element_by_class_name("category-items")
		try:
			kind_of_store_2 = browser.find_element_by_class_name("cuisines-list")
		except:
			kind_of_store_2 = ""
		types.append(kind_of_store_1.text + " " + kind_of_store_2.text)
		print("Types: ", types)
	except:
		kind_of_store_1 = browser.find_element_by_class_name("category-items")
		try:
			kind_of_store_2 = browser.find_element_by_class_name("category-cuisines")
		except:
			kind_of_store_2 = ""
		types.append(kind_of_store_1.text + " " + kind_of_store_2.text)
		print("Types: ", types)

	placement_point = browser.find_element_by_css_selector(".micro-home-static tr:nth-child(2) td:nth-child(3) b")
	placement_points.append(placement_point.text)
	print("placement_points: ", placement_points)

	price_point = browser.find_element_by_css_selector(".micro-home-static tr:nth-child(3) td:nth-child(3) b")
	price_points.append(price_point.text)
	print("price_points: ", price_points)

	quality_point = browser.find_element_by_css_selector(".micro-home-static tr:nth-child(4) td:nth-child(3) b")
	quality_points.append(quality_point.text)
	print("quality_points: ", quality_points)

	service_point = browser.find_element_by_css_selector(".micro-home-static tr:nth-child(5) td:nth-child(3) b")
	service_points.append(service_point.text)
	print("service_points: ", service_points)

	space_point = browser.find_element_by_css_selector(".micro-home-static tr:nth-child(6) td:nth-child(3) b")
	space_points.append(space_point.text)
	print("space_points: ", space_points)

	address = browser.find_element_by_css_selector(".res-common-add span:nth-child(2)")
	addresses.append(address.text)
	print("addresses: ", addresses)

	average_point = browser.find_element_by_css_selector(".ratings-boxes-points b")
	average_points.append(average_point.text)
	print("average_points: ", average_points)

	average_price = browser.find_element_by_css_selector(".res-common-minmaxprice span:nth-child(2)")
	average_prices.append(average_price.text)
	print("average_prices: ", average_prices)

# def selenium(fromm, to, num_csv, name_thread):
def selenium():
	try:
		# print(name_thread)
		options = webdriver.ChromeOptions()
		options.add_argument("--start-maximized")
		options.add_argument("--disable-notifications")
		global browser
		browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
		#for i in range(1, 12):
		browser.get("https://www.foody.vn/da-nang/food/cafe?q=")
		sleep(1)

		login = browser.find_element_by_xpath("/html/body/div[2]/header/div[2]/div/div[6]/div[1]/a/span")
		login.click()
		sleep(1)

		txtUsername = browser.find_element_by_id("Email")
		txtUsername.send_keys("xxx")
		txtPassword = browser.find_element_by_id("Password")
		txtPassword.send_keys("xxx")
		txtPassword.send_keys(Keys.ENTER)
		sleep(1)

		for _ in range(3):
			scroll = browser.find_element_by_tag_name('html')
			scroll.send_keys(Keys.END)
			sleep(1)

		for _ in range(2):
			scroll = browser.find_element_by_tag_name('html')
			scroll.send_keys(Keys.PAGE_UP)
		#
		try:
			for _ in range(32):
				element = WebDriverWait(browser, 10).until(
				EC.element_to_be_clickable((By.ID, "scrollLoadingPage"))
				)
				element.click()
				sleep(2)
		except:
			pass
		click_img = browser.find_elements_by_css_selector('.ri-avatar a img')
		print(len(click_img))
		for x in range(0, len(click_img)):
			main_window = browser.current_window_handle
			click_img = browser.find_elements_by_css_selector('.ri-avatar a img')[x]
			click_img.click()
			browser.switch_to_window(browser.window_handles[1])
			sleep(1)
			try:
				click_brand = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/div/div[1]/ul/li[1]/div[1]/a")
				if click_brand.is_displayed():
					click_brand.click()
				browser.switch_to_window(browser.window_handles[2])
				find()
				browser.close()
				browser.switch_to_window(browser.window_handles[1])
				browser.close()
				browser.switch_to_window(main_window)
				sleep(1)
			except:
				find()
				browser.close()
				browser.switch_to_window(main_window)

		save()
		browser.close()
	except:
		save()

if __name__ == '__main__':
	selenium()