import os
import sys
import convert_to_json
import teadownloader


def download_state_data(file_level, file_set, file_type):
	teadownloader.get_multiple_years(file_level, file_set, file_type)

def convert_data(state, file_name):
	file_name = ''

if __name__ == '__main__':
	# convert_to_json.csv_to_json('district.dat', 'y')
	file_level = sys.argv[1]
	file_set = sys.argv[2]
	file_type = sys.argv[3]

	download_state_data(file_level, file_set, file_type)