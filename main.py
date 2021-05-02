import numpy as np
import pandas as pd
from datetime import *
import xlrd
import openpyxl
import csv as csv

#zad.1
# imiona=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(imiona,header=0)
# print(df)

#zad.2
# print(df[df['Liczba']>1000])
# print(df[df['Imie']=='OSKAR'])
# print(df.agg({'Liczba':['sum']}))
#print(df[((df.Rok>=2000) & (df.Rok<=2005))].agg({'Liczba':['sum']}))
# print('chlopcy :' ,df[df.Plec=='M'].agg({'Liczba':['sum']}))
# print('dziewczynki :' ,df[df.Plec=='K'].agg({'Liczba':['sum']}))
# print(df.loc[df[df.Plec=='M'].groupby("Rok")["Liczba"].idxmax()])
# print(df.loc[df[df.Plec=='K'].groupby("Rok")["Liczba"].idxmax()])
# print(df.loc[df[df.Plec=='M']['Liczba'].idxmax()])
# print(df.loc[df[df.Plec=='K']['Liczba'].idxmax()])

#zad.3
# df=pd.read_csv('zamowienia.csv',skipinitialspace=True, sep=";")
# print(df.drop_duplicates(subset=['Sprzedawca']))
# print(df.sort_values(by=['Utarg']).head(5))
# print(df.value_counts(subset='Sprzedawca'))
# print(df.value_counts(subset='Kraj'))
#print(df[((df.Kraj=="Polska") & (df['Data zamowienia']>=datetime.strptime('01.01.2005','%d.%m.%Y')))].value_counts(subset='Kraj')) nie mogę wpaść na pomysł jak operować na datach w pythonie