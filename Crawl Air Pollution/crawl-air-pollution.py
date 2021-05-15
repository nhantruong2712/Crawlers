from selenium import webdriver
from time import sleep
import pandas as pd
from datetimerange import DateTimeRange
import datetime

list = []


def dateRange(start, end, step):
	rangeList = []
	time_range = DateTimeRange(start, end)
	for value in time_range.range(datetime.timedelta(days=step)):
		rangeList.append(value.strftime('%d/%m/%Y'))
	return rangeList


for i in range(20, 13, -1):
	for j in range(12, 1, -1):
		if j == 1 or j == 3 or j == 5 or j == 7 or j == 8 or j == 10 or j == 12:
			end_of_month = 31
			start = "20{}-{}-01".format(i, j)
			end = "20{}-{}-{}".format(i, j, end_of_month)
			list.append(dateRange(start, end, 1))
		elif j == 2:
			if i == 20 or i == 16:
				end_of_month = 29
				start = "20{}-{}-01".format(i, j)
				end = "20{}-{}-{}".format(i, j, end_of_month)
				list.append(dateRange(start, end, 1))
			else:
				end_of_month = 28
				start = "20{}-{}-01".format(i, j)
				end = "20{}-{}-{}".format(i, j, end_of_month)
				list.append(dateRange(start, end, 1))
		else:
			end_of_month = 30
			start = "20{}-{}-01".format(i, j)
			end = "20{}-{}-{}".format(i, j, end_of_month)
			list.append(dateRange(start, end, 1))

date_list = [item for sublist in list for item in sublist]


def selenium():
	pm25 = []
	pm10 = []
	o3 = []
	no2 = []
	so2 = []
	co = []

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
	action = webdriver.ActionChains(browser)
	browser.get("https://aqicn.org/data-platform/register/")
	sleep(2)
	inut_city = browser.find_element_by_class_name("prompt")
	inut_city.send_keys("Hanoi, Vietnam")
	sleep(2)
	click_city = browser.find_element_by_css_selector(".results a:nth-child(1)")
	click_city.click()
	sleep(2)
	for i in range(15, 105):
		try:
			infos_pm25 = browser.find_elements_by_css_selector("tbody tr:nth-child({}) td.squares svg text".format(i))
			info_pm25 = [el.text for el in infos_pm25]
			for string in info_pm25:
				if string == "-" or len(string) == 0:
					pm25.append("")
				# print("pm10: ",pm10)
				else:
					pm25.append(string)
		except:
			pass
		# print("pm25: ",pm25)
	pm10_click = browser.find_element_by_xpath("/html/body/div[7]/center[3]/div/div[2]/div[3]/div[2]/center/ul/li[2]")
	sleep(1)
	action.move_to_element(pm10_click)
	action.perform()
	sleep(1)
	for i in range(15, 105):
		try:
			infos_pm10 = browser.find_elements_by_css_selector("tbody tr:nth-child({}) td.squares svg text".format(i))
			info_pm10 = [el.text for el in infos_pm10]
			for string in info_pm10:
				if string == "-" or len(string) == 0:
					pm10.append("")
				# print("pm10: ",pm10)
				else:
					pm10.append(string)
		except:
			pass

	o3_click = browser.find_element_by_xpath("/html/body/div[7]/center[3]/div/div[2]/div[3]/div[2]/center/ul/li[3]")
	sleep(1)
	action.move_to_element(o3_click)
	action.perform()
	sleep(1)
	for i in range(15, 105):
		try:
			infos_o3 = browser.find_elements_by_css_selector("tbody tr:nth-child({}) td.squares svg text".format(i))
			info_o3 = [el.text for el in infos_o3]
			for string in info_o3:
				if string == "-" or len(string) == 0:
					o3.append("")
				# print("pm10: ",pm10)
				else:
					o3.append(string)
			# print("o3: ", o3)
		except:
			pass

	no2_click = browser.find_element_by_xpath("/html/body/div[7]/center[3]/div/div[2]/div[3]/div[2]/center/ul/li[4]")
	sleep(1)
	action.move_to_element(no2_click)
	action.perform()
	sleep(1)
	for i in range(15, 105):
		try:
			infos_no2 = browser.find_elements_by_css_selector("tbody tr:nth-child({}) td.squares svg text".format(i))
			info_no2 = [el.text for el in infos_no2]
			# print("monthly: ",monthly)
			for string in info_no2:
				if string == "-" or len(string) == 0:
					no2.append("")
				# print("pm10: ",pm10)
				else:
					no2.append(string)
			# print("no2: ", no2)
		except:
			pass

	so2_click = browser.find_element_by_xpath("/html/body/div[7]/center[3]/div/div[2]/div[3]/div[2]/center/ul/li[5]")
	sleep(1)
	action.move_to_element(so2_click)
	action.perform()
	sleep(1)
	for i in range(15, 105):
		try:
			infos_so2 = browser.find_elements_by_css_selector("tbody tr:nth-child({}) td.squares svg text".format(i))
			info_so2 = [el.text for el in infos_so2]
			# print("monthly: ",monthly)
			for string in info_so2:
				if string == "-" or len(string) == 0:
					so2.append("")
				# print("pm10: ",pm10)
				else:
					so2.append(string)
			# print("so2: ", so2)
		except:
			pass

	co_click = browser.find_element_by_xpath("/html/body/div[7]/center[3]/div/div[2]/div[3]/div[2]/center/ul/li[6]")
	sleep(1)
	action.move_to_element(co_click)
	action.perform()
	sleep(1)
	for i in range(15, 105):
		try:
			infos_co = browser.find_elements_by_css_selector("tbody tr:nth-child({}) td.squares svg text".format(i))
			info_co = [el.text for el in infos_co]
			# print("monthly: ",monthly)
			for string in info_co:
				if string == "-" or len(string) == 0:
					co.append("")
				# print("pm10: ",pm10)
				else:
					co.append(string)
			# print("co: ", co)
		except:
			pass

	a = {'date': date_list, 'PM25': pm25, 'PM10': pm10, 'O3': o3, 'NO2': no2, 'SO2': so2, 'CO': co}
	df = pd.DataFrame.from_dict(a, orient='index')
	df = df.transpose()
	dataset = pd.DataFrame(data=df)
	dataset.to_csv('hanoi-air-quality.csv')
	browser.close()


if __name__ == '__main__':
	selenium()
