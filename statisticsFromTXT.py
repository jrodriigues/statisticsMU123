from matplotlib.pyplot import close
from statisticsMU123 import Dataset

possible_filename = "possible.txt"
probable_filename = "probable.txt"
possible_data = []
probable_data = []

with open(possible_filename) as f:
    
    for line in f:
        possible_data.append(int(line.strip()))
    close

with open(probable_filename) as f:

    for line in f:
        probable_data.append(int(line.strip()))
    close

possible = Dataset(possible_data)
probable = Dataset(probable_data)
print(f"Possible dataset:\n{possible}")
print(f"\nProbable dataset:\n{probable}")

