# 필터를 템플릿에서 사용하려면 pybo/__init__.py 파일의 create_app 함수를 다음처럼 수정해야 한다.
def datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)


# filter.py에 필터 등록 -> __init__에 필터의 변수명, 필터에서 사용할 filter.py의 함수를 import 
# -> Template에서 해당 필터를 {{ 변수명 | 필터명}} 으로 사용 
# question_detail.html 에서 사용할 시간 필터를 만들어서 직접 화면에 출력해주세요. 
# date_time2 필터명을 작성해서 등록합니다. 


def datetime2(value):
    return value.year, value.month, value.day


# https://docs.python.org/ko/3/library/datetime.html