""" 이 챕터는 이전의 챕터와 다르게 다소 난이도가 있을 수 있다.
하지만 열심히 잘 따라오면 별 문제 없을것이다."""

"""
Programs and Processes
 프로그램이 실행될때, 운영체제는 process를 생성한다. process 는 시스템 리소스, 커널 내부의
data structures를 사용한다. 이때 각각의 프로세스는 독립적이기 때문에 서로 관여할 수 없다.

 이때 운영체제는, 각각의 실행되는 process를 추적하면서 그들이 일을 고르게 그리고 사용자로 하여금
제때 사용할 수 있도록 도와준다. 운영체제의 종류에따라 GUI로 표현되는 형태도 다양하다.

 또한 당신은 program을 이용해 process data에 접근할 수 있다. python 에서는 os module
을 이용해서 system information 에 접근할 수 있다.
 다음의 function은 process id와 python interpreter의 현재 작업 디렉토리를
얻어낸다. 한번 살펴보자.
"""

import os
# print("process id:", os.getpid())
# print("current working directory:", os.getcwd())

# 뭐지 왜 이 밑에것들 안되지?
# print("user id", os.getuid())
# print("group id", os.getgid())

"""
Create a Process with subprocess
 지금까지 본 대부분의 프로그램은 각각의 process 이다. 이때 우리는
python의 subprocess moudle을 통해 존재하는 프로그램을 시작하거나
혹은 중단시킬 수 있다.

- getoutput() : shell 내의 프로그램을 실행시키고 output을 grab 하고 싶을때.

다음의 예시를 한번 보자.
"""

# print("what the hell is goingon")
import subprocess
# ret = subprocess.getoutput('date')  # 실행이 아예안됨.
# print(ret)

# ret = subprocess.getoutput('date -u')
# print(ret)

""" subprocess 를 이용한 모든 process 생성은 실행이되지 않는다.
실행시간이 너무 오래걸리든, 뭘 하든간에 말이다. 따라서 대부분의 예제를
스킵하게 됐다. """


"""
Create a Process with multiprocessing
 'multiprocessing' module을 이용해서 python의 function을 분리된 process로 실행시키거나
심지어 여러개의 독립적인 process로 생성 가능하다. 한번 다음의 예시를 보자.
"""







