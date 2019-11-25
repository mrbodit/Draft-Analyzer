import csv
import pandas as pd
from config import DATA_FOLDER

data_file = 'D:\studia\Draft-Analyzer\data_gatherer\data\parsed_matches.csv'
# with open(data_file) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         print(row[7])
matches = pd.read_csv(data_file)
