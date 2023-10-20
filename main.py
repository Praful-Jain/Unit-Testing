import csv

csv_file1 = r'mock_matches.csv'
csv_file2 = r'mock_deliveries.csv'

def reader_function(csv_file):
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
        return data

matches_reader = reader_function(csv_file1)
deliveries_reader = reader_function(csv_file2)