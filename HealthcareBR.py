import numpy as np
import pandas as pd
import os
DH_PATH = 'healthcare_dataset[1].csv'

df = pd.read_csv(DH_PATH)
#df.head()
df.tail()



#df.isnull().sum()   #Check if any col have empty cells


#Fixing capitalization and  strip whitespace
df['Name'] = df['Name'].str.strip().str.title()
df['Doctor'] = df['Doctor'].str.strip().str.title()
df['Hospital'] = df['Hospital'].str.strip().str.title()


#Checking age to ensure between 120 and 0
print(df['Age'].min() > 0 and df['Age'].max() < 120)

#Checking unique vals for errors/typos
df['Gender'].unique().tolist()
df['Insurance Provider'].unique().tolist()
df['Blood Type'].unique().tolist()
df['Admission Type'].unique().tolist()
df['Test Results'].unique().tolist()
df['Medication'].unique().tolist()

#rounding bill to nearest hundreths place
df['Billing Amount'] = df['Billing Amount'].round(2)

#Checking current info on dataframe
df['Date of Admission'].info()

#Seeting datetime type
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')
print(df[['Date of Admission', 'Discharge Date']].dtypes)


#df.tail()
