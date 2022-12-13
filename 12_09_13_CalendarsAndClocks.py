"""
Calenders and Clocks
 지금까지 프로그래머들은 date, time을 표현하기 위해서 많은 노력을 했다.
그리고 여기서는 그들이 마주한 문제점과, 해결책, 몇가지 편법에 대해 이야기 해볼 것이다.

 날짜는 여러가지 형태로 표현될 수 있다. 하지만 이렇게 다양한 형태의 날짜 표현은
헷갈릴 수 있다. 예를 들어 1/6/2012 가 2012년 6월 1일인지, 1월 6일인지 어찌알 수 있을까?

 아무튼 python 의 standard library 에는 많은 date, time module이 존재한다.
몇몇개는 겹치기도 하고, 혼동되기도 할 것이다. 하여튼 공부해보자.
"""

"""
Leap year(윤년)
 알다시피 4년마다 2월달이 29일이 되는게 바로 윤년이다.
근데 100년 마다는 또 윤년이 아니며, 400년마다는?
python 에서는 함수를 이용해 해당 여부를 확인할 수 있다.
"""

import calendar
# print("1900:", calendar.isleap(1900))
# print("1996:", calendar.isleap(1996))
# print("2096:", calendar.isleap(2096))
# print("2396:", calendar.isleap(2396))


"""
The datetime Module
 datetime module은 이름에서 알다시피 date와 time에 관한것을 다룬다.
특히 네개의 object class가 정의되어있는데 다음과 같다.

- date : years, months, days 에 관한것
- time : hours, minutes, seconds, fractions 에 관한것.
- datetime : dates and times를 함께.
- timedelta : date and/or time intervals.
"""

from datetime import date
today = date(2022, 12, 13)
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.isoformat())

""" iso 는 ISO 8601로 국제 표준 date/time 표현방식이다. 
저자도 이 방식을 즐겨 사용하며 권장되는 방식인듯 하다. """

# today() method를 이용 오늘의 날짜 만들어내기.
from datetime import date
now = date.today()
print(now)
print(now.isoformat())




