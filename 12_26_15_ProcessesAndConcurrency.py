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

# import multiprocessing
# import os
#
# def whoami(what):
#     print("Process %s says: %s" % ( os.getpid(), what))
#
# if __name__ == "__main__":
#     whoami("I'm the main Program")
#     for n in range(4):
#         p = multiprocessing.Process(target=whoami,
#                                     args=("I'm function %s" % n, ))
#         p.start()

# mp.py 파일을 생성해 Terminal 에서 'python mp.py'로 실행한다.

""" Multiprocessing 내의 Process() function은 새로운 process를 생성하고
내부의 do_this() 을 실행시킨다. 앞서 이 코드에서는 4번 반복했기 때문에
4번 생성하고 4번 실행하게 되는것이다. 

 또한 multiprocessing 내에는 작업에 걸리는 시간을 줄이기 위해 많은 bell과 whistle
이 있으며, process 간의 상호소통등을 가능케 하는 다양한 기능등도 포함하고 있다.
또한 concurrency에 대한 내용도 있지만 추후에 주로 다루게 될 것이다."""

"""
Kill a Process with terminate()
 process 를 종료하고싶다면 terminate() 함수를 이용하면 된다
아래의 코드를 별도의 파일에 저장후 python 해당 파일이름 으로 실행 하면 된다.
"""

# import multiprocessing
# import time
# import os
#
# def whoami(name):
#     print("I'm %s, in process %s" % (name, os.getpid()))
#
# def loopy(name):
#     whoami(name)
#     start = 1
#     stop = 1000000
#     for num in range(start, stop):
#         print("\tNumber %s of %s. Honk!" % (num, stop))
#         time.sleep(0.5)
#
# if __name__ == '__main__':
#     whoami("main")
#     p = multiprocessing.Process(target=loopy, args=('loppy',))
#     p.start()
#     time.sleep(10)
#     p.terminate()


"""
Get System Info with os
 os module 내에는 다양한 기능이 있으며, 특히나
information function도 존재하며 사용예시를 한번 살펴보자.
"""

import os
# os.uname()  # 해당 기능은 Unix에서만 실행되며 windows 에서는 사용하지 못한다!
# print(os.getloadavg())  # 이것도 마찬가지로 안됨.
# print(os.cpu_count())  # 와 이건 된다.

import os
# print(os.system('dir\w'))  # 다 깨져서 나온다. 뭐가 문젤가?

"""
Get Process Info with psutil
 써드 파티 package인 'psutil' 또한 system, process 에 관한 정보를 제공한다.
특히 이전의 것들과 다르게 여러가지 운영체제에 지원한다.
"""

import psutil
print(psutil.cpu_times(True))  # 정상출력됨.
print(psutil.cpu_percent(True))  # 얼마나 cpu 쓰고있는지.
print(psutil.cpu_percent(percpu=True))


"""
Command Automation
 종종 수동으로 여러가지 일을 처리하곤 하는데, python 에는 훌륭한 써드 파티 관리 도구가 있다.
관련된 topic, 'task queues'이다. 추후에 얘기하게 될 것이다.
"""

"""
Invoke
 'fabric' tool의 version1 은 사용자로 하여금 파이썬 코드로된 local, remote task를
작성하는것을 가능케 해준다. 그리고 개발자들은 이것을 두개로 분할했다.

- fabric2 (remote)
- invoke (local)

 invoke의 주 사용처중 하나는 함수를 command-line arguments로 만들어주는 것이다.
한번 tasks.py 파일을 만들어서 한번 살펴보자.
"""

"""
Other Command Helpers
 invoke와 유사하지만, 어떻게 쓰느냐에 따라 더 나을수도 있는 것들이다
 
- click : https://click.palletsprojects.com/
- doit : http://pydoit.org/
- sh : http://amoffat.github.io/sh
- delegator : https://github.com/kennethreitz/delegator.py
- pypeln : https://cgarciae.github.io/pypeln
"""

"""
Concurrency
 http://bit.ly/concur-lib 해당 링크에서 concurrency 에 대한 많은 package 와
technique 에 대해 공부할 수 있지만, 여기서는 대표적인 것 하나만 다뤄볼 것이다.

 만약 컴퓨터를 쓸때, 당신이 기다리고 있다면 대개 다음의 이유들 때문이다.
- I/O bound : 이게 대부분의 경우이다.
- CPU bound : 과학적, 그래픽 계산 떄문에 발생한다.

 다음의 두 단어들도 concurrency도 연관되있다.
- Synchronous : 한개가 다른 것에 따르는 형태이다. 부모를 줄지어 따르는 새끼오리들처럼.
- Asynchronous : 각각의 task가 독립적이다. 호수 이리저리에 흩어져있는 거위떼들 처럼.

 concurrency는 실제생활 문제를 수행하려고 할때, 어느시점에서 반드시 마주치게 될 문제들이며
따라서 매우 중요하다. 느린 작업 하나 때문에 다른 작업들이 모두 정체된다고 생각해보면,
매우 큰 문제임을 알 수 있을 것이다.
 single machine 에서 가능한 여러개의 task를 수행하고자 할때는, 각각의 업무들이
독립적으로 실행되게 해야한다.
 하지만 그럼에도 불구하고, concurrent computing은 regular computing보다 매우 복잡하며
무사히 마무리되기 어려운 방식이기도 하다.

 이처럼 여러 문제를 다룰 수 있는 방법은 바로 'queue'이다.
"""

# take away : 떠나가다

"""
Queues
 queue는 list와 유사하다. 한 지점에서 들어오고 다른 지점에서 나간다. 
흔히 말하는 FIFO(First in First out)와 같다.
 접시 닦는것으로 비유했을때, 하나를 닦고, 말린후, 놓는것과 여러개를 동시에
닦고, 말리고, 놓는것등이 해당할 것이다. 이 모두 synchronous appraoch 이며
한명의 worker가 한번에 한개씩 해내는 것이다.

 이 방법 말고는, helper나 여러사람이 하는 것이다. task를 나눠서할 수 있다면
효율이 매우 빨라질 것이다.
 근데 이때 작업자들간의 속도가 다를때 문제가 발생한다. 모두 수행되어야하는 필수적인
업무이기 때문에, 결국 가장 느린 작업자의 속도대로 task가 진행될 것이다.

 일반적으로 queue는 정보를 가지고 있는 message 를 운송한다.
일례로 work queue, job queue, task queue 등이 해당되며
washer, dryer, putawayer 에게 업무를 분담하는것도 해당하겠다.
그리고 이러한 작업들도 worker를 늘리면 업무도 빠르게 끝나게 될 것이다.
"""

"""
Processes
 queue를 구현하는데는 다양한 방법이 있지만, 앞서 사용했던
multiprocessing module 내에 queue function이 포함돼있다.
일단 1명의 washer와 여러명의 dryer process, 그리고
intermediate dish_queue가 있다 가정하고, dishes.py 내에 작성해보자.
"""
















