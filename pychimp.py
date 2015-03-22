""" 

Python wrapper for MailChimp API v2.0

https://apidocs.mailchimp.com/api/2.0/

"""

import requests


class MailChimp(object):
	
	def __init__(self, api_key = '', extra_params = {}):
		
		self.api_key = api_key
		
		self.params = {'apikey':api_key}
		
		self.params.update(extra_params)
		
		# Extract the datacenter prefix from the api key
		dc = self.api_key.split('-')[1]
		
		self.base_url = 'https://%s.api.mailchimp.com/2.0' % dc
	
	""" 
	@method - API Method /lists/list or /lists/list.json
	@params - Data that we need to provide 
		{
			'apikey': example_api_key,
			'id': example_list_id,
			'email':
				{
					'email':'john@example.com'
				},
			'double_optin':False
		}
	"""
	def api_call(self, method, post_data = {}):
		
		#Construct the URL
		url = self.base_url + method
	
		post_data = self.params.copy()
		
		post_data.update(params)
	
		resp = requests.post(base_api_url,json=post_data)
		
		return resp.json()
