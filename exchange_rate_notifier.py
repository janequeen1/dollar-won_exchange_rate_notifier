import requests
from datetime import datetime

def get_exchange_rate():
	# exchangerate-api.com API 사용
	url = "https://api.exchangerate-api.com/v4/latest/USD"
	response = requests.get(url)

	if response.status_code == 200:
		data = response.json()
		return data['rates'].get('KRW', 'N/A') # 달러/원 환율 가져오기
	else:
		return "Error fetching rate"

def main():
	# 현재 날짜와 시간 가져오기
	now = datetime.now()
	date_str = now.strftime("%Y-%m-%d")
	day_of_week = now.strftime("%A") # 요일
	time_str = now.strftime("%H:%M:%S")

	# 환율 가져오기
	exchange_rate = get_exchange_rate()

	# 출력
	print(f"{date_str} {day_of_week} {time_str}의 환율은 {exchange_rate} 입니다.")

if __name__ == "__main__":
	main()