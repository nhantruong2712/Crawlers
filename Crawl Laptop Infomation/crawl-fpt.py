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

chip_brands = []
chip_speeds = []
chip_types = []
hdds = []
ssds = []
card_brands = []
card_models = []
card_onboards = []
card_onboard_models = []
prices = []
rams = []
ram_types = []
ram_speeds = []
inches = []
descs = []


# def selenium(fromm, to, num_csv, name_thread):
def selenium():
    try:
        # print(name_thread)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
        #for i in range(1, 12):
        browser.get("https://mega.com.vn/tim?scat_id=&q=laptop&page=1")
        sleep(1)
        click_img = browser.find_elements_by_css_selector(".cdt-product__img")
        print(len(click_img))
        # for x in range(from, to):
        for x in range(0, len(click_img)):
            click_img = browser.find_elements_by_css_selector(".cdt-product__img")[x]
            click_img.click()
            sleep(1)

            try:
                more_detail_btn = browser.find_element_by_xpath("/html/body/div[3]/div[4]/div[5]/div/div[2]/a")
                more_detail_btn.click()
                sleep(1)

                chip_brand_name = browser.find_element_by_css_selector("#full-spec > table > tbody > tr:nth-child(1)")
                if "Sản phẩm" in chip_brand_name:
                    chip_brand_name = browser.find_element_by_css_selector("#full-spec > table > tbody > tr:nth-child(2)")
                chip_brands.append(chip_brand_name.text)
                # sleep(1)
                print("chip_brands: ", chip_brands)

                # chip_speed = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/table[1]/tbody/tr[6]/td[2]")
                # chip_speeds.append(chip_speed.text)
                # # sleep(1)
                # # print("chip_speeds: ", chip_speeds)
                #
                # chip_type_1 = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/table[1]/tbody/tr[2]/td[2]")
                # chip_type_2 = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/table[1]/tbody/tr[3]/td[2]")
                # chip_types.append(chip_type_1.text + " " + chip_type_2.text)
                # # sleep(1)
                # # print("chip_types: ", chip_types)
                #
                # ram = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/table[1]/tbody/tr[1]/td[2]")
                # rams.append(ram.text)
                # # sleep(1)
                # # print("rams: ", rams)
                #
                # ram_type = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/table[1]/tbody/tr[2]/td[2]")
                # ram_types.append(ram_type.text)
                # # sleep(1)
                # # print("ram_types: ", ram_types)
                #
                # ram_speed = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/table[1]/tbody/tr[3]/td[2]")
                # ram_speeds.append(ram_speed.text)
                # # sleep(1)
                # # print("ram_speeds: ", ram_speeds)
                #
                # try:
                #     ssd = browser.find_element_by_xpath(
                #         "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[5]/div[2]/div[1]/table/tbody/tr[2]/td[2]")
                #     if ssd.is_displayed():
                #         ssds.append(ssd.text)
                #         # sleep(1)
                #         # print("ssds: ", ssds)
                # except:
                #     ssds.append("--")
                #     # sleep(1)
                #     # print("ssds: ", ssds)
                # try:
                #     hdd = browser.find_element_by_xpath(
                #         "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[5]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
                #     if hdd.is_displayed():
                #         hdds.append(hdd.text)
                #         # sleep(1)
                #         # print("hdds: ", hdds)
                # except:
                #     hdds.append("--")
                #     # sleep(1)
                #     # print("hdds: ", hdds)
                #
                # try:
                #     card_brand_name = browser.find_element_by_xpath(
                #         "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]")
                #     if card_brand_name.is_displayed():
                #         card_brands.append(card_brand_name.text)
                #         # sleep(1)
                #         # print("card_brands: ", card_brands)
                # except:
                #     card_brands.append("--")
                #     # sleep(1)
                #     # print("card_brands: ", card_brands)
                # try:
                #     card_onboard_name = browser.find_element_by_xpath(
                #         "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div[2]/table/tbody/tr[1]/td[2]")
                #     if card_onboard_name.is_displayed():
                #         card_onboards.append(card_onboard_name.text)
                #         # sleep(1)
                #         # print("card_onboards: ", card_onboards)
                # except:
                #     card_onboards.append("--")
                #     # sleep(1)
                #     # print("card_onboards: ", card_onboards)
                #
                # try:
                #     card_brand_model = browser.find_element_by_xpath(
                #         "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div[1]/table/tbody/tr[2]/td[2]")
                #     if card_brand_model.is_displayed():
                #         card_models.append(card_brand_model.text)
                #         # sleep(1)
                #         # print("card_models: ", card_models)
                # except:
                #     card_models.append("--")
                #     # sleep(1)
                #     # print("card_brands: ", card_brands)
                # try:
                #     card_onboard_model = browser.find_element_by_xpath(
                #         "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
                #     if card_onboard_model.is_displayed():
                #         card_onboard_models.append(card_onboard_model.text)
                #         # sleep(1)
                #         # print("card_onboard_models: ", card_onboard_models)
                # except:
                #     card_onboard_models.append("--")
                #     # sleep(1)
                #     # print("card_onboard_models: ", card_onboard_models)
                #
                # inch = browser.find_element_by_xpath(
                #     "/html/body/div[2]/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[3]/table[1]/tbody/tr[1]/td[2]")
                # inches.append(inch.text)
                # # print("inches: ", inches)
                #
                # # details = browser.find_elements_by_css_selector(".product-summary li")
                # # detail = [el.text for el in details]
                # # # print("detail: ", detail)
                # # prices = browser.find_elements_by_css_selector("#product-info-price p:nth-child(2) b")
                # # if len(prices) > 0:
                # #     price = [el.text for el in prices]
                # # else:
                # #     prices = browser.find_elements_by_css_selector("#product-info-price b")
                # #     price = [el.text for el in prices]
                # # # price = [el.text for el in prices]
                # # # print("price: ", price)
                # # for i in range(0, len(detail)):
                # #     if ("CPU" in detail[i]):
                # #         processors.append(detail[i])
                # #         for string in processors:
                # #             new_string_pro = string.replace("- CPU: ", "")
                # #             processor.append(new_string_pro)
            except:
                browser.back()

        browser.close()
        # browser.back()

        sleep(1)
        a = {'Brands': descs, 'Chip Brands': chip_brands, 'Chip Speeds': chip_speeds, 'Chip Type': chip_types,
             'Ram': rams, 'Ram Type': ram_types, 'SSD': ssds, 'HDD': hdds, 'Card Brands': card_brands,
             'Card Models': card_models, 'Card Onboards': card_onboards, 'Card Onboard Models': card_onboard_models,
             'Prices': prices}
        df = pd.DataFrame.from_dict(a, orient='index')
        df = df.transpose()
        dataset = pd.DataFrame(data=df)
        dataset.to_csv('laptops-fpt.csv')
        browser.close()
    except:
        # a = {'Brands': descs, 'Chip Brands': chip_brands, 'Chip Speeds': chip_speeds, 'Chip Type': chip_types,
        #      'Ram': rams, 'Ram Type': ram_types, 'SSD': ssds, 'HDD': hdds, 'Card Brands': card_brands,
        #      'Card Models': card_models, 'Card Onboards': card_onboards, 'Card Onboard Models': card_onboard_models,
        #      'Prices': prices}
        #
        # df = pd.DataFrame.from_dict(a, orient='index')
        # df = df.transpose()
        # dataset = pd.DataFrame(data=df)
        # dataset.to_csv('laptops-fpt.csv')
        pass


if __name__ == '__main__':
    selenium()
    # threads = []
    # name_thread_1 = "thread 1"
    # name_thread_2 = "thread 2"
    # name_thread_3 = "thread 3"
    # name_thread_4 = "thread 4"
    # name_thread_5 = "thread 5"
    # name_thread_6 = "thread 6"
    # name_thread_7 = "thread 7"
    # t1 = threading.Thread(target=selenium, args=(0, 153, 1, name_thread_1))
    # t1.start()
    # t2 = threading.Thread(target=selenium, args=(153, 306, 2, name_thread_2))
    # t2.start()
    # t3 = threading.Thread(target=selenium, args=(396, 459, 3, name_thread_3))
    # t3.start()
    # t4 = threading.Thread(target=selenium, args=(459, 612, 4, name_thread_4))
    # t4.start()
    # t5 = threading.Thread(target=selenium, args=(612, 765, 5, name_thread_5))
    # t5.start()
    # t6 = threading.Thread(target=selenium, args=(765, 918, 6, name_thread_6))
    # t6.start()
    # t7 = threading.Thread(target=selenium, args=(918, 1071, 7, name_thread_7))
    # t7.start()
    # threads.append(t1)
    # threads.append(t2)
    # threads.append(t3)
    # threads.append(t4)
    # threads.append(t5)
    # threads.append(t6)
    # threads.append(t7)
    # for th in threads:
    #     th.join()
