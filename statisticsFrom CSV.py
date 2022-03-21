import csv
from statisticsMU123 import Dataset

filename = "data.csv"


with open(filename) as f:

    file_reader = csv.reader(f)
    data_str = next(file_reader)   
    f.close()

data_int = []

for item in data_str:
    data_int.append(float(item))

dataset = Dataset(data_int)
print(f"Dataset details: {dataset}")

