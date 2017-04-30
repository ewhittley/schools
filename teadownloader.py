import os
import requests
from lxml import html

def get_tea_snapshot_data(file_level, file_set, file_type):
	session_requests = requests.session()

	# Actual form page to view download options located at
	# 'https://rptsvr1.tea.texas.gov/perfreport/snapshot/download.html'
	snapshot_url = 'https://rptsvr1.tea.texas.gov/perfreport/snapshot/push.cgi' 

	if file_type == 'data':
		file_extension = '.dat'
	elif file_type == 'descriptions':
		file_extension = '.lyt'
	else:
		print "not a valid file_type"

	form_data = {'level': file_level, 'set': file_set, 'suf': file_extension}
	result = session_requests.post(snapshot_url, data=form_data)

	download_file_name = file_level + '_' + file_set + file_extension

	current_directory = os.path.abspath(os.path.dirname( __file__ ))
	output_data_directory = os.path.join(current_directory, 'output')
	output_data_file = os.path.join(output_data_directory, download_file_name)

	with open(output_data_file, 'wb') as download_file:
		download_file.write(result.content)

def get_multiple_years(file_level, year_range, file_type):
	if "-" not in year_range:
		print "year_range not provided in propert format. Please submit as YYYY-YYYY."
	else:
		data_years = [ int(year) for year in year_range.split("-") ]
		
		start_year = data_years[0]
		end_year = data_years[-1]

	for year in range(start_year, end_year + 1):
		get_tea_snapshot_data(file_level, str(year)[-2:], file_type)

		# print "start year: " + start_year + " end year: " + end_year

if __name__ == '__main__':
	get_multiple_years('district', '1999-2005', 'data')
	# get_tea_snapshot_data('district', '13', 'data')