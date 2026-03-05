# api 사용
import requests
import csv
from datetime import datetime
import os

MY_API = os.getenv("WEATHER_API_KEY")
city_name ="Seoul"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_API}"
url += "&units=metric"
# get 방식 요청 --> request 라이브러리 사용
response = requests.get(url)
result = response.json()

main = result["weather"][0]["main"]
temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
current_time = datetime.now().strftime("%Y-%m-%d- %H:%M:%S")

# weather.csv 를 만들자
# 최초 생성 시  -> 헤더 추가
# 파일 존재하면 덮어쓰기
csv_exist = os.path.exists("weather.csv")
header = ["current_time", "temp", "humidity", "main"]
with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not csv_exist:
        writer.writerow([])
    
    writer.writerow([current_time, temp, humidity, main])
print("날씨 저장 완")
