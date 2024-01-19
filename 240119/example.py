# 서버로부터 데이터를 가져와보세용
# https://fakestoreapi.com/carts

# 남들이 만들어놓은 코드를 가져다가 쓰자 ~!
# -> 라이브러리
# 데이터를 가져오는 python 라이브러리(패키지) : requests
# 파이썬 패키지 관리 : pip
    # 설치 : pip install <패키지이름>
    # 목록 확인 : pip list

# 내 코드에 다른 패키지를 추가
import requests
import pprint

api_key = '85caa089b6fafbbc204aadce2fbff4f3'
lat = 37.56 #서울의 위도
lon = 126.97 #서울의 경도

url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
data = requests.get(url).json()
pprint.pprint(data)
# = pprint.pprint(data['weather'])

