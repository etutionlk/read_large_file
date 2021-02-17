#!/usr/bin/python3
import zipfile
import csv
import pandas as pd

zip_file = zipfile.ZipFile("500000-Sales-Records.zip")

df = pd.read_csv(zip_file.open("500000_Sales_Records.csv"))

for index, row in df.iterrows():
    print(row["Sales Channel"])
    exit(0)
