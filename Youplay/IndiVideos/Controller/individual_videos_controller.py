import requests
import webbrowser
from selenium import webdriver
import dateutil.parser
import json
import re
import time
import pandas as pd


class CreateAndPlayController():

	def create_video_list(self,input_file_path):
		df = pd.read_excel(input_file_path)
		return list(df['VideoID'])

	def playlist(self,video_list,key):
		headers = {'Content-Type': 'application/json'}
		for id in video_list:
			url = 'https://www.googleapis.com/youtube/v3/videos/?part=contentDetails&id=' + id + '&key=' + key
			resp = requests.get(url,headers)
			response_data = json.loads(resp.text)#['items']#[0]['contentDetails']['duration']
			videoduration = response_data['items'][0]['contentDetails']['duration']
			#time_in_minutes = dateutil.parser.parse(videoduration)
			print(videoduration)
			video_duration_in_seconds = int(re.findall(r'\d+',videoduration)[0]) * 60 + int(re.findall(r'\d+',videoduration)[1])
			base_video_url = 'https://www.youtube.com/watch?v=' + id

			chrome_open = webdriver.Chrome('G:/PortableTools/chromedriver_win32/chromedriver.exe')
			chrome_open.get(base_video_url)
			#webbrowser.open(base_video_url,new=0,autoraise=True)
			time.sleep(video_duration_in_seconds + 10)
			chrome_open.close()
		