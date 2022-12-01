"""
 지금부터 우리는 python의 완전한 program 을 작성할 것이다.
python의 standard library을 사용하고 직접 Module을 만들어 볼 것이다.
그렇게 해서 우리는 지금까지 처럼 단편적인 프로그램이 아니라
제대로된 프로그램을 만들 수 있으리라 기대된다.
"""

"""
Modules and the import Statement
 Module 은 file 안에 있는 python 코드를 의미하며, 특별한 지정같은게 필요없이
파일내의 Python code는 그자체로 다른 이들에게 import 되어 module로 사용될 수 있다.
또한 Module 을 참조할때는 'import' statement 를 사용해서 해당 모듈 내의
변수와 코드를 나의 프로그램에서 사용할 수 있게 해준다.
"""

"""
Import a Module
 import statement 를 사용하는 가장 간단한 방법은 import module이다.
여기서는 랜덤으로 음식을 고르는 function 을 가지고 있는 모듈을 작성하고
해당 모듈을 import 해보자.
"""

# import test

# place = test.pick()
# print(f"Let's go to {place})"  # 실행될때 마다 결과가 달라지는 걸 볼 수 있다.

"""
위의 함수에서 우리는 2번 import 했다.
1. 메인 프로그램인 이곳에서 test.py 를 import 했다.
2. test.py 에서 choice function을 사용하기위해 random module을 import 했다.
"""
      
"""
Import a Module with Another Name
 앞서 우리는 import test 를 호출했지만 다음과 같은 문제가 있다면?
- test 라는 이름의 module이 또 있으면?
- 더 기억하기 쉬운 이름을 사용하고 싶다면.
- typing을 최소화 하고 싶다면.
이와 같은 경우에는 'alias'를 import 하면 된다.
다음의 예시를 한번 봐보자.
"""

# import test as t  # test를 t라 칭하고 매우 간단하게 사용하는 모습!
# place = t.pick()
# print(f"Let's go to {place}")

"""
Import Only What You Want from a Module
 또한 module 의 import 범위를 조정하는 것도 가능하다.
이미 우리가 앞서 본것인데 바로 'from random import choice' 이다.
앞서 했던 것처럼 alias를 이용해 원하는 특정 기능만 사용 가능하다.
"""

from test import pick
place = pick()
# print(f"Let's go to {place}")

from test import pick as who_cares  # pick 을 who_cares 로 이름만 바꿔주기.
place = who_cares()
# print(f"Let's go to {place}")

"""
Packages
package 는 .py file들을 가지고 있는 subdirectory이다.
이를 한번 구현해보고자 한다. 일단 우리는 현재 디렉토리에
main program을 가지고 있으며, choices 라는 이름의 subdirectory 에
fast.py 와 advice.py 를 집어 넣을 것이다.
각각의 모듈은 string 을 리턴한다.
"""

# questions.py 메인 프로그램.
from choices import fast, advice
# choicies 디렉토리에서 fast, advice를 import 한다!

# 실행할 때 마다 결과물이 랜덤으로 출력된다.
# print(f"Let's go to {fast.pick()}")
# print(f"Should we  take out? {advice.give()}")


"""
The Module Search Path
import choices 호출시, 현재 디렉토리에서 해당 choice를 탐색한다는 것을
기억 할 것이다. 이때, 우리는 이러한 과정을 control 할 수 있다.

또한 random 에서 choice() 함수를 사용했던 것을 보면, 우리의 현재
디렉터리 에는 해당 random 모듈이 없으며, 외부에서 찾았음을 알 수 있다.

이렇게 python interperter가 작동하는 것을 확인해보고 싶다면
sys 모듈을 import 하고 path list를 사용해보면 된다.
이것은 python이 해당 모듈을 찾기까지의 경로의 list를 의미한다. 
"""

# import sys
# for place in sys.path:
#     print(place)

"""
이때 random 과 같이 standary library 에 있는것을 현재 디렉토리에
정의한다면 해당 기능을 사용 할 수 없음에 주의하라.
또한 코드를 통해 search path를 수정할 수도 있다.
"""

# import sys
# sys.path.insert(0, "/my/modules")
# 무서워서 실행 못시키겠다.

"""
Relative and Absolute Imports
지금까지 현재 디렉토리, 서브 디렉토리, 스탠다드 library 등에서 import 했다.
별 문제 없어보이지만, local module과 standard module의 이름이 겹치면
무엇을 import 해야 될지 혼동이 생기게 된다.

 그래서 python은 absolute 와 relative import를 지원한다.
지금까지의 import는 모두 absolute 였으며, relative의 사용법은 다음과 같다.

- relative import 사용법.
1. 같은 디렉토리에 있을 경우: from . import rougarou
2. 바로 상위 디렉토리에 있을 경우: from .. import rougarou
3. creatures 라는 형재 디렉토리에 있을 경우: from ..creatures import rougarou
"""

"""
Namespace Packages
package 를 directory를 따라서 namespace package 를 통해 나눌 수 있다.
이는 package 가 너무 비대해져, 나누고 싶지만 나누는 도중 해당
module 을 사용하고 있는 프로그램에 영향을 줄 수 있을때 유용하게 사용 될 수 있다.

대안은 다음과 같다.
1. critters(예시 package) 위에 새로운 location directories를 생성.
2. 생성된 new parents 디렉토리의 밑에 critters의 cousin 을 만들어준다.
3. 기존의 모듈들을 각각의 디렉토리로 이동시킨다.

- 기존의 것.
critters
 -> rougarou.py
 -> wendigo.py
사용: from critters import wendigo, rougarou

- parents directory 를 활용.
north
 ->critters
  ->wendigo.py

south
 ->critters
  ->rougarou.py
  
사용: from critters import wendigo, rougarou

만약에 north 와 south에 module search path에 있다면
single directory package 처럼 여전히 사용 할 수 있다.
"""

"""
Module Versus Objects
어쩔때 module 내에 code를 넣어야 하고, 언제 object 에 넣어야 할까?
그 둘은 여러 분야에서 매우 유사하게 사용 된다. thing.stuff 등과 같이 말이다.

또한 module 내부의 클래스, 펑션, 전역 변수들은 외부에서도 사용 가능하며
object는 property 와 (__)로 접근 권한등을 설정 할 수 있다.

그리고 import 를 통해 module 내의 무언가를 변경시켜도
그것은 복사된 것이 변경되는 것이기 때문에, 문제가 되진 않는다.
"""

"""
Goodies in the Python Standarad Library.
python 에는 정말 많은 standard library 가 있으며, 우리가 찾는
대부분의 것들이 있을정도이며, 교재에도 이러한 library 등이 있는
웹페이지나 교재들이 많이 소개 되어 있다.

이후로도 나오는 chapter 에서도 우리는 여러가지 standard module에 대해
공부하게 될 것이며, 일반적으로 사용되는 것들에 대해서도 많이 다뤄볼 것이다.
"""

"""
Handle Missing Keys with setdefault() and defaultdict()
dictionary에 존재하지 않는 key에 접근했을 때, exception 을 겪어봤을 것이다.
그래서 exception 을 피하기위해 dict의 get() 함수를 사용하곤 했다.

여기서 소개되는 setdefault() 함수는 get()과 유사하지만
만약 key가 missing 됐으면 item 을 할당하는 기능을 한다.
"""

periodic_table = {'Hydrogen': 1, 'Helium': 2,}
# print(periodic_table)

# 존재하지 않는 key 의 경우, 할당됨을 볼 수 있다.
carbon = periodic_table.setdefault('Carbon', 12)
# print(carbon)
# print(periodic_table)

# 기존의 key 를 변경시키고자 하는 경우, 변경 되지 않음.
helium = periodic_table.setdefault('Helium', 545)
# print(helium)
# print(periodic_table)

"""
defaultdict() 도 비슷하다. 다른점은 dictionary가 생성될때
default value를 구체화 하며, argument로 function을 받는다.
한번 예시를 통해 알아보자.
"""

from collections import defaultdict
periodic_table = defaultdict(int)
# 이제부터 missing value는 값이 0인 integer가 된다.

periodic_table['Hydrogen'] = 1
# print(periodic_table['Lead'])
# print(periodic_table)

""" 여기서 defaultdict() 의 argument로 들어간 function 은
missing key 에 배정될 value를 return 하는 것 들이다.
이후의 예제에서 no_idea 는 필요한 value를 return 하기 위함이다. """

from collections import defaultdict

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
# print(bestiary['A'])
# print(bestiary['B'])
# print(bestiary['C']) # 미 할당된 경우. Huh가 할당되어 출력되는 모습.
# print(bestiary)

""" 이외에도 int(), list(), dict() 과 같은 function을 사용 할 수 있다.
만약에 argument 를 생략하는 경우에는 새로운 key 의 default value는
None이 된다. 
 lambda를 쓰는 경우, 간단하게 만들 수도 있다."""

bestiary = defaultdict(lambda: 'Huh?')
# print(bestiary['E'])

# int()를 이용해 counter 만들어보기
from collections import defaultdict
food_counter = defaultdict(lambda: 0) # lambda 로도 작동이 된다.
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

# for food, count in food_counter.items():
#     print(food, count)

""" 만약 여기서 defaultdict 을 사용하지 않았더라면
food_counter의 값이 0으로 초기화 되지 않았기 때문에
exception이 발생해서 반복문에서 dict_counter[food] 를
0으로 설정해줘야 하는 수고로움이 일어나게 된다."""


"""
Count Items with Counter()
앞서한 dict 의 빈도수 세기 기능을 하는 standard library가 있다.
바로 counter() 이다.
"""

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
# print(breakfast_counter)  # 겁내 간단하다.

# most_common() : 내림차순으로 모든 element를 return.
# print(breakfast_counter.most_common())
# print(breakfast_counter.most_common(1))  # 숫자가 주어지면 해당 갯수만큼. 내림

# counter 를 combine 하는 것도 가능하다. 한번 보자

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)

# print("breakfast:", breakfast_counter)
# print("lunch", lunch_counter)
# print("breakfast + lunch:", breakfast_counter + lunch_counter)  # 합치기.
# print("breakfast - lunch:", breakfast_counter - lunch_counter)
# print("lunch - breakfast:", lunch_counter - breakfast_counter)
# print("lunch & breakfasat:", lunch_counter & breakfast_counter)
# print("breakfast | lunch:", lunch_counter | breakfast_counter)

"""
Order by Key with OrderedDict()
python 구 버전에서는 dictionary가 삽입된 순서대로 출력되지 않기때문에
OrderedDict()과 같은 함수가 필요했다. 지금은 아니다.
"""

quotes = {'Moe': 'A',
          'Larry': 'B',
          'Curly': 'C'}

# 최신버전이라 순서대로 출력, 테스트가 안됨.
# for stooge in quotes:
#     print(stooge)

"""
Stack + Queue == deque
deque는 double ended queue 를 의미한다. stack, queue 모두의 특징을
지니고 있으며 sequence의 양끝에서 더하거나, 삭제할 수 있다.
 
 이제 회문(거꾸로해도 같은것)인지 알기위해 우리는 단어의 양끝에서 중앙까지 확인할 것이다.
1. popleft(): deque의 최좌측 item을 제거하고 return.
2. pop(): 최우측 item 제거후 return.

 이것들을 통해 끝에서 부터 가운데까지 탐색해 나갈 것이다. 
"""

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

# print(palindrome('a'))
# print(palindrome('abc'))
# print(palindrome('aba'))

# 굳이 이런 방식말고 string을 revers 했을때 같은지 확인하면 됨.
def another_palindrome(word):
    return word == word[::-1]

# print(another_palindrome('a'))
# print(another_palindrome('ab'))

"""
Iterate over Code Structures with itertools
itertools 에는 특수한 목적의 iterator function을 포함하고 있다.
각각의 function 들은 for loop 가 시행될때 1개의 item을 리턴하며,
call 사이에서 그 상태들을 기억한다.
"""

# chain() 함수 사용하는 모습. 주어진 인자를 엮는다(chain)
import itertools
# for item in itertools.chain([1, 2], [3, 4], ['a', 'b']):
    # print(item)

# cycle() 함수 사용하는 모습. 무한하게 반복됨.
import itertools
# for item in itertools.cycle([1, 2]):
    # print(item)

# accumulte() 함수는 accumulated value 들을 계산한다. default로는 sum 을 계산해냄.
# import itertools
# for item in itertools.accumulate([1, 2, 3, 4]):
    # print(item)

# 두번째 매개변수로 function 을 부여하면 기존의 동작(더하기)를 대체 할 수 있다.
import itertools
def multiply(a, b):
    return a * b

# for item in itertools.accumulate([1, 2, 3, 4], multiply):
#     print(item)

""" itertools 에는 이외에도 다양한 function들을 가지고 있으며, 잘 응용한다면
시간을 아끼는데에 도움이 될 것이다. """

"""
Print Nicely with pprint()
지금까지 우리는 print()로 출력해왔는데, 때떄로 읽기 힘들때가 많았다.
그래서 좀 더 개선된 pprint()를 여기서 소개할 것이다.
"""

from pprint import pprint
quotes = dict([('Moe', 'A wise guy, huh?'),
               ('Larry', 'Ow!'),
               ('Curly', 'Nyuk nyuk!'),])


# print(quotes)  # 삽입순으로 그대로 출력.
# pprint(quotes)  # 좀더 읽기 쉽게 출력되는듯?

"""
Get Random
random 모듈내의 특정 function 등을 통해 sequence 에서
무작위로 value를 뽑아낼 수 있다.
"""

from random import choice
# pprint(choice(range(1001)))
# pprint(choice('alphabet'))
# pprint(choice(('a', 'one', 'and-a', 'two', 'three')))

# 한번에 여러개의 랜덤 value를 얻고싶다면 숫자와 함께 sample() 을 사용하면 된다.
from random import sample
# print(sample([23, 9, 45, 'bacon', 'a', 'b', range(50)], 3))

# 특정범위내의 무작위 수를 얻기위해서 randint(), randrange() 와 같은 함수도 있다.
from random import randrange
# print(randrange(34, 311))
# print(randrange(38, 74, 5))  # 범위 지정 + step지정(건너뛰기)

# random() 함수를 통해 0.0 과 1.0 사이의 진짜 random 한 숫자 얻기.
from random import random
# print(random())


""" Things to Do """
# 11.1
# import zoo
# zoo.hours()

# 11.2
import zoo as menagerie
# menagerie.hours()
# hours()  # 이렇게는 안되는듯 하다.

# 11.3
from zoo import hours
# hours()  # direct로 import 따라서 바로 사용이 가능하다.

# 11.4
from zoo import hours as info
# info()

# 11.5
plain = dict(a=1, b=2, c=3)
# pprint(plain)

# 11.6
""" OrderedDict 만들 수 없다. 여기서는 지원을 안해!"""

# 11.7
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a') # 이게 정답. append 라는게 따로있네?
# dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])







