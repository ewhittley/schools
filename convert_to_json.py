import os
import csv
import json


def csv_to_json(csv_file, headers='y'):
	json_file = os.path.splitext(csv_file)[0] + '.json'

	with open(csv_file) as open_csv_file:
		reader = csv.DictReader(open_csv_file)
		rows = list(reader)

	with open(json_file, 'w') as open_json_file:
		json.dump(rows, open_json_file)

	open_csv_file.close()
	open_json_file.close()


if __name__ == '__main__':
	csv_to_json('district.dat', 'y')