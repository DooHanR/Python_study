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
저자도 이 방식을 즐겨 사용하며 권장되는 방식인듯 하다.
그리고 이후에 나오는 strptime(), strftime() 라는
dates를 parsing, formatting 하는 method에 대해 알아볼 것이다. """

# today() method를 이용 오늘의 날짜 만들어내기.
from datetime import date
now = date.today()  # 계속해서 오늘의 날짜가 나올 것이다.
# print(now)
# print(now.isoformat())

# timedelta object를 이용해 data에 time interval을 추가해보기.
from datetime import timedelta
one_day = timedelta(days = 1)
tomorrow = now + one_day

# print(tomorrow)
# print(now + one_day*8)
# print(now - one_day)

# date의 범위. 따라서 역사적인, 혹은 천문학적인 계산은 불가능하다.
# print(date.min)
# print(date.max)

# datetime의 time object는 하루의 시간을 나타내는데 사용된다. (시간, 분, 초)
from datetime import time
noon = time(12, 0, 0)
# print(noon)
# print(noon.hour)
# print(noon.minute)
# print(noon.second)
# print(noon.microsecond)
# print(time(14))  # 명시하지않으면 00분으로 간주한다.

# datetime object는 date, time 모두 포함한다. 다음의 예시를 한번 보자.
from datetime import datetime
some_day = datetime(2022, 1, 4, 5, 4, 5, 4)
# some_day = datetime.now()
# print(some_day)
# print(some_day.isoformat())  # 'T'는 date와 time을 구별해주는 역할을 한다.

# 또한 datetime 에도 now method가 있다!
now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)

# datetime 속으로 time과 date object 들을 combine 해보기.
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
# print(noon_today)

# datetime 에서 date, time을 뽑아낼 수도 있다. date(), time() method를 써보자.
# print(noon_today)
# print(noon_today.date())
# print(noon_today.time())

"""
Using the time Module
 datetime 모듈내에 time object이 있음에도 불구, 별개의 time module이 존재하며
time module 내에 또 time() 이 존재한다. (???)
 절대 시간을 나타내는 방법중 하나는, 바로 시작점에서부터의 초를 세는것이다.
Unix time은 1970년 7월 1일부터 시작한 초의 모임을 사용한다.
이러한 것을 epoch 라고도 부르는가 본데, system 내에서 dates,times를 교환하는
가장 간단한 방법이라고 한다? 한번 예시를 통해 알아보자.
"""

import time
now = time.time()
# print(now)  # 뉴욕의 1970년때부터 지금까지의 초.

# epoch value를 string 으로 바꿀수도 있다.
# print(time.ctime(now))

""" Epoch value는 서로 다른 시스템에서 date, time을 교환하기위한 최소공분모로 사용될 수 있다.
예를 들어 javascript의 경우, 그리고 가끔 구체적인 날짜, 시간을 알고싶을때
time 에서는 struct_time object를 제공한다.
- localtime() : system의 time zone내에서의 시간을 제공.
- gmtime() : UTC 기준에서 시간을 제공. """

# print(time.localtime(now))
# print(time.gmtime(now))
# print(time.localtime())  # 생략하면 현재시간을 나타내준다.
# print(time.gmtime())

""" 위의 함수를 통해 출력되는, struct_time values
- tm_wday : Day of week : 0(Monday)~6(Sunday)
- tm_yday : Day of year : 1~366 
- tm_isdt : Daylight savings? : 0 = no, 1 = yes, -1 = unknown. """

""" 이때 struct_time 내부의 tm_... 등을 type 하고싶진 않을 것이다.
struct_time 은 named_tuple 처럼 행동하기 때문에 index들을 사용할 수 있다."""

import time
now = time.localtime()
# print(now)
# print(now[0])
# print(list(now[x] for x in range(9)))

# 반면에 mktime() method는 struct_time object를 epoch second로 바꾼다.
tm = time.localtime()
# print(time.mktime(tm))

""" 교재에서 주는 시간과 관련해 몇가지 팁이 있다.
 첫째로, 가능한한 UTC를 사용하라는 것이다.
UTC 는 absolute time 이기때문에 만약 서버의 시간을 설정해야한다면
절대로 local time 을 사용하지 말고 UTC를 사용하도록 해라.

 둘째는, 가능한한 daylight savings time의 사용을 피하라는 것이다.
daylight savings time은 하절기에 1시간 댕기는 것을 의미하는데, 
이와 같은 기능은 봄에 한시간 당겨지고, 가을쯤에 한시간 미뤄져서 혼란을
야기하기가 쉬우므로 사용을 피하도록 해라. """


"""
Read and Write Dates and Times
 앞서 얘기햇듰이, dates 와 times를 쓰는 방식에는 여러가지가 있다.
isoformat() 처럼 표준적인 방식 외에도, ctime() function 과 같이 epoch를
string 으로 바꿀 수도 있다.

 또한 strftime() method를 이용. dates,times 를 string으로 바꿀수 있다.
이 함수는 datetime, date, time, time module 내부에 모두 있으며
output을 구체화 하기위해 format string을 사용한다.

 그리고 strptime() method를 이용. string의 형태를 입력받아 dates, times 로
전환또한 가능하다.

포맷스트링은 다양한 종류가 있으며 알고싶다면 pg 284의 Table 13-2를 참고해라.
"""

import time
fmt = "It's %A, %B %d, %Y, local time: %I:%M:%S%p"
t = time.localtime()
# print(t)
# print(time.strftime(fmt, t))

from datetime import date
some_day = date(2022, 12, 15)
fmt = "It's %A, %B %d, %Y, local time: %I:%M:%S%p"
# print(some_day.strftime(fmt))  # 입력되지 않은 사항은 default인 midnight 처리한다.

from datetime import time
some_time = time(9, 23)
# print(some_time.strftime(fmt))  # 마찬가지로 default로 date가 설정되고 시간만 설정된다.

""" string->date,time 하고 싶다면 strptime() 함수와 함께 format string을 사용해라.
한번 year-month-day로 나타내보자. 이때 '-'(dash)를 사용해야 함에 주의해라. """

import time
fmt = "%Y-%m-%d"  # 연 월 일
# time.strptime("2019 01 29", fmt)  # string을 date로. 이떄 형식이 맞지않음.
# print(time.strptime("2022-12-15", fmt))  # 형식에 맞춰야 정상출력.

# 이번에는 space로 출력하고 싶을때
fmt = "%Y %m %d"
# print(time.strptime("2022 12 15", fmt))


""" 두번째로 할 것은 string을 여러 국가에 맞춰 여러 종류의 언어로 나타내 봅시다."""

import locale
from datetime import date
halloween = date(2022, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', ]:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B %d')

import locale
names = locale.locale_alias.keys()

good_names = [name for name in names if len(name) == 5 and name[2] == '_']
# print(good_names[:5])

# 독일 language locales를 원한다면 다음과 같이 하라
de = [name for name in good_names if name.startswith('de')]
print(de)

""" pg 287 에도 python time inter-conversion의 요약이 그림으로
잘되어있으니 추후에 꼭 확인해보도록 하라. """


""" 
Alternative Modules
이 외에도 여러개 있으며 참고 하길 바란다. pg 288.
"""
























































































