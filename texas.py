import os
import convert_to_json
import teadownloader


def download_state_data():
	teadownloader.get_multiple_years('district', '1999-2001', 'data')

def convert_data(state, file_name):
	file_name = ''

if __name__ == '__main__':
	# convert_to_json.csv_to_json('district.dat', 'y')
	download_state_data()