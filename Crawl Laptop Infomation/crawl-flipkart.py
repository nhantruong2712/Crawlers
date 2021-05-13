import threading
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl

convert_generals = []
generals = []
chip_brand = []
chip_brands = []
chip_speed = []
chip_speeds = []
chip_type = []
chip_types = []
chips = []
hdd = []
hdds = []
ssd = []
ssds = []
card_brand = []
card_brands = []
card_model = []
card_models = []
pricee = []
prices = []
ram = []
rams = []
ram_type = []
ram_types = []
ram_speed = []
ram_speeds = []
inch = []
inches = []
descs = []
ssd_capacities = []

def save():
	a = {'Description': descs, 'Chip Brands': chip_brands, 'Chip Speeds': chip_speeds, 'Chip Type': chip_types,
		 'Ram': rams, 'Ram Type': ram_types,'SSD': ssds, 'HDD': hdds, 'Card Brands': card_brands,
		 'Card Models': card_models, 'Prices (Rupee)': pricee, 'Prices (VND)': prices, 'SSD Capacity': ssd_capacities}
	df = pd.DataFrame.from_dict(a, orient='index')
	df = df.transpose()
	dataset = pd.DataFrame(data=df)
	dataset.to_excel('laptops-flipkart.xlsx'.format())

def clear_info():
	for i in range(len(generals)):
		chip_name = ""
		chip_brand_name = ""
		chip_speed_name = ""
		chip_type_name = ""
		hdd_name = ""
		ssd_name = ""
		ssd_capacitie_name = ""
		card_model_name = ""
		ram_name = ""
		ram_type_name = ""
		inch_name = ""
		for string in generals[i]:
			remove_n = string.replace("\n", ": ")
			# print("Remove n: ", remove_n)
			if "Processor Brand:" in remove_n:
				chip_brand_name = (remove_n.replace("Processor Brand: ", ""))

			if "Clock Speed:" in remove_n:
				chip_speed_name = (remove_n.replace("Clock Speed: ", ""))

			if "Processor Variant:" in remove_n:
				chip_name = (remove_n.replace("Processor Variant: ", ""))

			if "Processor Name:" in remove_n:
				chip_type_name = (remove_n.replace("Processor Name: ", ""))

			if "RAM Type:" in remove_n:
				ram_type_name = (remove_n.replace("RAM Type: ", ""))

			if "RAM:" in remove_n:
				ram_name = (remove_n.replace("RAM: ", ""))

			if "SSD:" in remove_n:
				ssd_name = (remove_n.replace("SSD: ", ""))

			if "SSD Capacity:" in remove_n:
				ssd_capacitie_name = (remove_n.replace("SSD Capacity: ", ""))

			if "HDD Capacity:" in remove_n:
				hdd_name = (remove_n.replace("HDD Capacity: ", ""))

			if "Graphic Processor:" in remove_n:
				card_model_name = (remove_n.replace("Graphic Processor: ", ""))

			if "Screen Size:" in remove_n:
				inch_name = (remove_n.replace("Screen Size: ", ""))
		if len(chip_brand_name) == 0:
			chip_brands.append("No")
		else:
			chip_brands.append(chip_brand_name)
		if len(chip_speed_name) == 0:
			chip_speeds.append("No")
		else:
			chip_speeds.append(chip_speed_name)
		if len(chip_name) == 0:
			chips.append("No")
		else:
			chips.append(chip_name)
		if len(chip_type_name) == 0:
			chip_types.append("No")
		else:
			chip_types.append(chip_type_name)
		if len(ram_type_name) == 0:
			ram_types.append("No")
		else:
			ram_types.append(ram_type_name)
		if len(ram_name) == 0:
			rams.append("No")
		else:
			rams.append(ram_name)
		if len(ssd_name) == 0:
			ssds.append("No")
		else:
			ssds.append(ssd_name)
		if len(ssd_capacitie_name) == 0:
			ssd_capacities.append("No")
		else:
			ssd_capacities.append(ssd_capacitie_name)
		if len(hdd_name) == 0:
			hdds.append("No")
		else:
			hdds.append(hdd_name)
		if len(card_model_name) == 0:
			card_models.append("No")
		else:
			card_models.append(card_model_name)
		if len(inch_name) == 0:
			inches.append("No")
		else:
			inches.append(inch_name)
	for z in card_models:
		if "Intel" in z:
			card_brands.append("Intel")
		elif "AMD" in z:
			card_brands.append("AMD")
		elif "NVIDIA" in z:
			card_brands.append("NVIDIA")
		elif "Qualcomm" in z:
			card_brands.append("Qualcomm")
		elif "MediaTek" in z:
			card_brands.append("MediaTek")
		else:
			card_brands.append("NO")

	print("card_brands: ", card_brands)
	print("chip_brands: ", chip_brands)
	print("chip_speeds: ", chip_speeds)
	print("chips: ", chips)
	print("chip_types: ", chip_types)
	print("ram_types: ", ram_types)
	print("rams: ", rams)
	print("ssds: ", ssds)
	print("SSD Capacity: ", ssd_capacities)
	print("hdds: ", hdds)
	print("card_models: ", card_models)
	print("inches: ", inches)

def change_money():
	for string in pricee:
		new_string_price = string.replace("₹", "")
		new_string_price = new_string_price.replace(",", ".")
		new_string_price = float(new_string_price) * 313.73
		new_string_price = round(new_string_price, 3)
		new_string_price = "{:0,.3f}".format(new_string_price)
		new_string_price = new_string_price.replace(",", ".")
		prices.append(new_string_price)
		print("prices (vnd): ", prices)

# def selenium(fromm, to, num_csv, name_thread):
def selenium():
	try:
		# print(name_thread)
		options = webdriver.ChromeOptions()
		options.add_argument("--start-maximized")
		options.add_argument("--disable-notifications")
		options.add_argument("--disable-popup-blocking")
		browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
		try:
			# for i in range(fromm, to):
			for i in range(2, 10):
				browser.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}".format(i))
				sleep(1)
				click_img = browser.find_elements_by_class_name("_4rR01T")
				print(len(click_img))
				# for x in range(from, to):
				for x in range(0, len(click_img)):
					main_window = browser.current_window_handle
					click_img = browser.find_elements_by_class_name("_4rR01T")[x]
					click_img.click()
					browser.switch_to_window(browser.window_handles[1])
					sleep(1)

					try:
						description = browser.find_element_by_class_name("B_NuCI")
						# print("description: ", description.text)
						descs.append(description.text)

						try:
							price = browser.find_element_by_class_name("_17Rl6L")
							print("price: ", price.text)
							pricee.append(price.text)
						except:
							price = browser.find_element_by_class_name("_30jeq3")
							print("price: ", price.text)
							pricee.append(price.text)

						more_detail_btn = browser.find_element_by_class_name("_1FH0tX")
						more_detail_btn.click()

						general_info = browser.find_elements_by_css_selector("._14cfVK tr")
						global generals
						general = [el.text for el in general_info]
						generals.append(general)
						print("generals: ", generals)
						sleep(1)
						browser.close()
						browser.switch_to_window(main_window)
						sleep(1)
						# browser.back()
					except:
						browser.back()
			change_money()
			clear_info()
			save()
			# browser.close()
		except:
			save()
	except:
		save()



if __name__ == '__main__':
	selenium()
	# threads = []
	# name_thread_1 = "thread 1"
	# name_thread_2 = "thread 2"
	# name_thread_3 = "thread 3"
	# name_thread_4 = "thread 4"
	# t1 = threading.Thread(target=selenium, args=(2, 9, 1, name_thread_1))
	# t1.start()
	# t2 = threading.Thread(target=selenium, args=(9, 16, 2, name_thread_2))
	# t2.start()
	# t3 = threading.Thread(target=selenium, args=(16, 23, 3, name_thread_3))
	# t3.start()
	# t4 = threading.Thread(target=selenium, args=(23, 30, 4, name_thread_4))
	# t4.start()
	# threads.append(t1)
	# threads.append(t2)
	# threads.append(t3)
	# threads.append(t4)
	# for th in threads:
	# 	th.join()
