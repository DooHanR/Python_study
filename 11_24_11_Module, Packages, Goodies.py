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

import sys
for place in sys.path:
    print(place)

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
