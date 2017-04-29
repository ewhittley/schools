import requests
from lxml import html

def get_tea_snapshot_data(file_level, file_set, file_type):
	session_requests = requests.session()

	# Actual form page to view download options located at
	# 'https://rptsvr1.tea.texas.gov/perfreport/snapshot/download.html'
	snapshot_url = 'https://rptsvr1.tea.texas.gov/perfreport/snapshot/push.cgi' 

	if file_type == 'data':
		form_data = {'level': file_level, 'set': file_set, 'suf': '.dat'}
	elif file_type == 'descriptions':
		form_data = {'level': file_level, 'set': file_set, 'suf': '.lyt'}
	else:
		print "not a valid file_type"

	result = session_requests.post(snapshot_url, data=form_data)

	download_file_name = file_level + '_' + file_set + '.dat'

	current_directory = os.path.abspath(os.path.dirname( __file__ ))
	output_data_directory = os.path.join(current_directory, 'output')
	output_data_file = os.path.join(output_data_directory, download_file_name)

	with open(output_data_file, 'wb') as download_file:
		download_file.write(result.content)

if __name__ == '__main__':
	get_tea_snapshot_data('district', '13', 'data')