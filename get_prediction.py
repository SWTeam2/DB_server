import requests
import json

# get data from infer server
# REST API 경로에 접속하여 응답(Response) 데이터 받아오기
url = ''
response = requests.get(url=url, params={'table':'Learning_table_bearing_ex', 'load_cnt':1})
data = response.json()
python_list = json.loads(data)

