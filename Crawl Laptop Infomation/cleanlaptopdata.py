# -*- coding: utf-8 -*-
"""cleanlaptopdata.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JmXqwRK3-qFnwXIfgYhcJP0wygqGlw3f

# UPLOAD FILE XLSX
"""

from google.colab import files
uploaded = files.upload()

"""# READ FILE"""

import pandas as pd
my_dic = pd.read_excel('laptops.xlsx', index_col=0).to_dict()

dataset = pd.DataFrame(data = my_dic)

dataset['ram'] = dataset['RAM'].copy() # Creating a copy of RAM
dataset['ram'].unique()

print(dataset['ram'])

"""# RAM"""

ram_in_gb = []
for i in dataset['ram']:
  if('8' in i): # 8GB RAM
    ram_in_gb.append(i[0])
  elif('4' in i): # 4GB RAM
    ram_in_gb.append(i[0])
  elif('16' in i): # 16GB RAM
    ram_in_gb.append('16')
  elif('32' in i): # 32GB RAM
    ram_in_gb.append('32')
dataset['ram_in_gb'] = ram_in_gb
print(len(ram_in_gb))
dataset['ram_in_gb']

"""# RAM TYPE

"""

ddr_version = []
for i in dataset['ram']:
    if('LPDDR4X' in i): 
      ddr_version.append("LPDDR4X")
    elif('DDR4' in i):  
      ddr_version.append("DDR4")
    else:  # If 32GB RAM then check the DDR version
      ddr_version.append("DDR3")
dataset['ddr_version'] = ddr_version
print(len(ddr_version))
dataset['ddr_version']

"""# PROCESSOR"""

dataset['processor'] = dataset['Processor'].copy() # Creating a copy of Processor
gen = dataset['processor'].apply(lambda x:x.replace("Intel Core", ""))
dataset['processor'].unique()

dataset['processor']

gen

"""# Processor Type

"""

processor_type = []
for i in (gen):
    processor_type.append(" ".join(i.split()))
processor_type

"""# Processor name"""

processor_name = []
for i in dataset['processor']:
  if('Intel' in i): 
    processor_name.append('Intel')
  elif('AMD' in i):
    processor_name.append('AMD')
  elif('Microsoft' in i):
    processor_name.append('Microsoft')
  elif('Apple' in i):
    processor_name.append('Microsoft')
  else:
    processor_name.append('Unknown')
dataset['processor_name'] = processor_name
print(len(processor_name))
dataset['processor_name']

"""# Storage"""

dataset['storage'] = dataset['Storage'].copy() # Creating a copy of Storage
dataset['storage'].unique()

dataset['storage']

disk_drive = []
for y in dataset['storage']:
    if('HDD' in y and 'SSD' not in y):   # If only HDD
      disk_drive.append('HDD')
    elif('SSD' in y and 'HDD' not in y): # If only SSD
      disk_drive.append('SSD')
    elif('+' in y):     # If both HDD and SSD
      disk_drive.append("Both")
    else:
      disk_drive.append("Unknown")
dataset['disk_drive'] = disk_drive
print(len(disk_drive))
dataset['disk_drive']

storage_in_gb = []
for i in dataset['storage']:
  if('512' in i and 'TB' not in i): # Only 512GB SSD or 512GB HDD
    storage_in_gb.append('512')
  elif('256' in i and 'TB' not in i): # Only 256GB SSD or 256GB HDD
    storage_in_gb.append('256')
  elif('128' in i and 'TB' not in i): # Only 128GB SSD or 128GB HDD
    storage_in_gb.append('128')
  elif('512' in i and 'TB' in i):     # If 1TB HDD + 512GB SSD
    storage_in_gb.append('1000+512')
  elif('256' in i and 'TB' in i):     # If 1TB HDD + 256GB SSD
    storage_in_gb.append('1000+256')
  elif('128' in i and 'TB' in i):     # If 1TB HDD + 128GB SSD
    storage_in_gb.append('1000+128')
  elif('1' in i and '256' not in i and '512' not in i): # Only 1TB HDD or 1TB SSD
    storage_in_gb.append('1000')
  elif('2' in i and '256' not in i and '512' not in i): # Only 2TB HDD or 2TB SSD
    storage_in_gb.append('2000')
  else:
    storage_in_gb.append('Unknown')
dataset['storage_in_gb'] = storage_in_gb
print(len(storage_in_gb))
dataset['storage_in_gb']

"""# Display"""

dataset['display'] = dataset['Display'].copy() # Creating a copy of Display
dataset['display'].unique()

dataset['display']

size_in_inches = []
for i in dataset['display']:
  if('15.6' in str(i)):   
    size_in_inches.append('15.6')
  elif('14' in str(i) or '14.0' in str(i)):  
    size_in_inches.append('14')
  elif('13.3' in str(i)):  
    size_in_inches.append('13.3')
  elif('13' in str(i) or '13.0' in str(i)):    
    size_in_inches.append('13')
  elif('13.4' in str(i)):    
    size_in_inches.append('13.4')
  elif('13.7' in str(i)):    
    size_in_inches.append('13.7')
  elif('13.5' in str(i)): 
    size_in_inches.append('13.5')
  elif('17.3' in str(i)): 
    size_in_inches.append('17.3')
  elif('17' in str(i) or '17.0' in str(i)): 
    size_in_inches.append('17')
  elif('16' in str(i) or '16.0' in str(i)):   
    size_in_inches.append('16')
  elif('11' in str(i) or '11.0' in str(i)):  
    size_in_inches.append('11.6')
  elif('12.3' in str(i)):   
    size_in_inches.append('12.3')
  elif('12.4' in str(i)):   
    size_in_inches.append('12.4')
  elif('12.5' in str(i)):   
    size_in_inches.append('12.5')
  elif('16' in str(i) or '16.0'):   
    size_in_inches.append('16')
  elif('10' in str(i) or '10.0' in str(i)):  
    size_in_inches.append('10.5')
  elif('15' in str(i) or '15.0' in str(i)):    
    size_in_inches.append('15')
dataset['size_in_inches'] = size_in_inches
print(len(size_in_inches))
dataset['size_in_inches']

"""# Decriptions"""

dataset['description'] = dataset['Description'].copy() # Creating a copy of Description
dataset['description'].unique # All the laptops are unique
# dataset['description']

company = []
for i in dataset['description']:
  if('Dell' in i):           
    company.append('Dell')
  elif('Asus' in i):         
    company.append('Asus')
  elif('Lenovo' in i):        
    company.append('Lenovo')
  elif('Acer' in i):         
    company.append('Acer')
  elif('HP' in i):           
    company.append('HP')
  elif('Apple' in i or 'Macbook'):        
    company.append('Apple')
  elif('MSI' in i):          
    company.append('MSI')
  elif('Avita' in i or 'AVITA' in i): 
    company.append('Avita')
  elif('LG' in i): 
    company.append('LG')
  elif('Microsoft' in i): 
    company.append('Microsoft')
dataset['company'] = company
print(len(company))
dataset['company']

"""# Graphic Cards"""

dataset['card'] = dataset['Card'].copy() # Creating a copy of Description
card = dataset['card'].apply(lambda x:x.replace("NVIDIA ", "").replace("AMD ", "").replace("Intel ", "").replace("Nvidia ", "").replace("Radeon ", "").replace("INvidia ", ""))
dataset['card'].unique # All the laptops are unique
# dataset['description']

card

graphic_card_company = []
for i in dataset['card']:
  if('Onboard' in i):
    graphic_card_company.append('Onboard')
  elif ('INVIDIA' in i or 'NVIDIA' in i):
    graphic_card_company.append("NVIDIA")
  elif ('AMD' in i):
    graphic_card_company.append("AMD")
  elif ('Intel' in i):
    graphic_card_company.append("Intel")
  elif ('Intel' in i):
    graphic_card_company.append("Intel")
  elif ('Radeon' in i):
    graphic_card_company.append("Radeon")
  elif ('Radeon' not in i and 'Intel' not in i and 'AMD' not in i and 'INVIDIA' not in i and 'NVIDIA' not in i and 'Onboard' not in i):
    graphic_card_company.append("Intel")
dataset['graphic_card_company'] = graphic_card_company
print(len(graphic_card_company))
dataset['graphic_card_company']

dataset

dataset.drop(['ram','storage','processor','card','display','description', 'Description', 'Processor', 'Card', 'RAM', 'Storage', 'Display'],axis=1,inplace=True)

dataset

dataset.to_excel('datalaptop-cleaned.xlsx')