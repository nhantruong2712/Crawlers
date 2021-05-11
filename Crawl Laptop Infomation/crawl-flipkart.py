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
chip_brand = []
chip_brands = []
chip_speed = []
chip_speeds = []
chip_type = []
chip_types = []
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

def save(num_cv):
    a = {'Description': descs, 'Chip Brands': chip_brands, 'Chip Speeds': chip_speeds, 'Chip Type': chip_types,
         'Ram': rams, 'Ram Type': ram_types, 'Ram Speed': ram_speeds,'SSD': ssds, 'HDD': hdds, 'Card Brands': card_brands,
         'Card Models': card_models, 'Prices (Rupee)': pricee, 'Prices (VND)': prices}
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    dataset = pd.DataFrame(data=df)
    dataset.to_csv('laptops-flipkart-{}.csv'.format(num_cv))

def clear_info():
    for string in generals:
        remove_n = string.replace("\n", ": ")
        if "Processor Brand:" in remove_n:
            chip_brand.append(remove_n)

        if "Clock Speed:" in remove_n:
            chip_speed.append(remove_n)

        if "Processor Name:" in remove_n:
            chip_type.append(remove_n)

        if "RAM:" in remove_n:
            ram.append(remove_n)

        if "RAM Type:" in remove_n:
            ram_type.append(remove_n)

        if "SSD:" in remove_n:
            ssd.append(remove_n)

        if "HDD Capacity:" in remove_n:
            hdd.append(remove_n)

        if "Graphic Processor:" in remove_n:
            card_model.append(remove_n)

        if "Screen Size:" in remove_n:
            inch.append(remove_n)

        if "RAM Frequency:" in remove_n:
            ram_speed.append(remove_n)

    for z in chip_brand:
        new_string_chip_brand = z.replace("Processor Brand: ", "")
        chip_brands.append(new_string_chip_brand)
        print("chip_brands: ", chip_brands)

    for z in chip_speed:
        new_string_chip_speed = z.replace("Clock Speed: ", "")
        chip_speeds.append(new_string_chip_speed)
        print("chip_speeds: ", chip_speeds)

    for z in chip_type:
        new_string_chip_type = z.replace("Processor Name: ", "")
        chip_types.append(new_string_chip_type)
        print("chip_types: ", chip_types)

    for z in ram:
        new_string_rams = z.replace("RAM: ", "")
        rams.append(new_string_rams)
        print("rams: ", rams)

    for z in ram_type:
        new_string_rams_type = z.replace("RAM Type: ", "")
        ram_types.append(new_string_rams_type)
        print("ram_types: ", ram_types)

    for z in ram_speed:
        new_string_rams_speed = z.replace("RAM Frequency: ", "")
        ram_speeds.append(new_string_rams_speed)
        print("ram_speeds: ", ram_speeds)

    for z in ssd:
        new_string_ssd = z.replace("SSD: ", "")
        ssds.append(new_string_ssd)
        print("ssds: ", ssds)

    for z in hdd:
        new_string_hdd = z.replace("HDD Capacity: ", "")
        hdds.append(new_string_hdd)
        print("hdds: ", hdds)

    for z in card_model:
        new_string_card_model = z.replace("Graphic Processor: ", "")
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
        card_models.append(new_string_card_model)
        print("card_models: ", card_models)
        print("card_brands: ", card_brands)

    for z in inch:
        new_string_inch = z.replace("Screen Size: ", "")
        inches.append(new_string_inch)
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

def selenium(fromm, to, num_csv, name_thread):
# def selenium():
    try:
        # print(name_thread)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        browser = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
        for i in range(fromm, to):
        # for i in range(1, 2):
            browser.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}".format(i))
            sleep(1)
            click_img = browser.find_elements_by_class_name("_4rR01T")
            # print(len(click_img))
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

                    general = browser.find_elements_by_css_selector("._14cfVK tr")
                    global generals
                    generals = [el.text for el in general]
                    # print("generals: ", generals)

                    change_money()
                    clear_info()
                    sleep(1)
                    browser.close()
                    browser.switch_to_window(main_window)
                    sleep(1)
                    # browser.back()
                except:
                    browser.back()

        save()
        # browser.close()
    except:
        save()



if __name__ == '__main__':
    # selenium()
    threads = []
    name_thread_1 = "thread 1"
    name_thread_2 = "thread 2"
    name_thread_3 = "thread 3"
    name_thread_4 = "thread 4"
    t1 = threading.Thread(target=selenium, args=(1, 9, 1, name_thread_1))
    t1.start()
    t2 = threading.Thread(target=selenium, args=(9, 16, 2, name_thread_2))
    t2.start()
    t3 = threading.Thread(target=selenium, args=(16, 23, 3, name_thread_3))
    t3.start()
    t4 = threading.Thread(target=selenium, args=(23, 30, 4, name_thread_4))
    t4.start()
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)
    for th in threads:
        th.join()
