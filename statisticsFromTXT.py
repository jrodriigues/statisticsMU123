from statisticsMU123 import Dataset

# Filenames
possible_filename = "possible.txt"
probable_filename = "probable.txt"
practiceQuiz_filename = "dataPracticeQuiz.txt"

# Data storages
possible_data = []
probable_data = []
practiceQuiz_data = []

with open(possible_filename) as f:
    
    for line in f:
        possible_data.append(int(line.strip()))
    f.close()

with open(probable_filename) as f:

    for line in f:
        probable_data.append(int(line.strip()))
    f.close()


with open(practiceQuiz_filename) as f:
    
    for line in f:
        practiceQuiz_data.append(int(line.strip()))
    f.close()

"""
possible = Dataset(possible_data)
probable = Dataset(probable_data)
practiceQuiz = Dataset(practiceQuiz_data)
print(f"Possible dataset:\n{possible}")
print(f"\nProbable dataset:\n{probable}")
print(f"\nPractice quiz dataset:\n{practiceQuiz}")
"""

