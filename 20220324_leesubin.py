#1
letters = 'python'
print(letters[0])
print(letters[2])
#2
string = "PYTHON"
print(string[::-1])
#3
url = input("url을 입력하세요: ")
url_split = url.split('.')
print(url_split[-1])
#4
file_name = "보고서.xlsx"
file_name.endswith(("xlsx"))
#5
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
#6
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41<= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")
#7
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
#8
warn_investment_list = ["Microsoft", "Google", "Naver", "kakao", "SAMSUNG", "LG"]
종목 = input("종목명: ")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
#9
리스트 = [100, 200, 300]
for 변수 in 리스트:
    print(변수 + 10)
#10
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 종목명 in 리스트:
    길이 = len(종목명)
    print(길이)
