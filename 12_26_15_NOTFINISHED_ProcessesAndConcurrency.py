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

# dishes.py 의 파일내용.

# import multiprocessing as mp
#
# def washer(dishes, output):
#     for dish in dishes:
#         print(f"Washing {dish} dish")
#         output.put(dish)
#
# def dryer(input):
#     while True:
#         dish = input.get()
#         print(f"Drying {dish} dish")
#         input.task_done()

""" 메인 함수를 선언해야 오류가 안생기는듯 하다. 왜일까? 
-> 메인 함수 선언시 논리적 구조가 개선되고 독립된 실행 프로그램으로써 다루어진다고 한다.
아직 잘 모르겠으니, 더 공부해보자."""

# if __name__ == '__main__':
#     dish_queue = mp.JoinableQueue()
#     dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
#     dryer_proc.daemon = True
#     dryer_proc.start()
#
#     dishes = ['salad', 'bread', 'entree', 'dessert']
#     washer(dishes, dish_queue)
#     dish_queue.join(


""" JoinableQueue와 join method를 통해 washer가 모든 dish가 말려졌음을 알기위해 사용됨. 
이 위의 queue 는 python iterator 처럼 보이지만, 사실 washer와 dryer 사이의 communication에
따라서 process가 시작된다.
 또한 이외에도 다양한 queue type이 multiprocessing module 내에 존재하며
다음의 링크를 통해 확인해 볼 수 있다. : http://bit.ly/multi-docs """


"""
Threads
 thread는 process의 모든것에 접근가능하면서, process 와 함께 실행된다.
multiprocessing module에는 threading 이라는게 있는데, process 대신에
thread를 사용하는 것이다. 한번 thread로 process example을 테스트 해보자.
"""

# thread1. py의 내용.

# import threading
#
# def do_this(what):
#     whoami(what)
#
# def whoami(what):
#     print("Thread %s says: %s" % (threading.current_thread(), what))
#
# if __name__ == '__main__':
#     whoami("I'm the main program")
#     for n in range(4):
#         p = threading.Thread(target=do_this,
#                              args=("I'm function %s" % n,))
#         p.start()

""" process-based dish example 을 thread 를 이용해서 reproduce 해볼 것이다.
다음의 thread_dishes.py 에서 나타날 것이다. """

# thread_dishes.py 의 내용.

# import threading, queue
# import time
#
# def washer(dishes, dish_queue):
#     for dish in dishes:
#         print ("Washing", dish)
#         time.sleep(5)
#         dish_queue.put(dish)
#
# def dryer(dish_queue):
#     while True:
#         dish = dish_queue.get()
#         print ("Drying", dish)
#         time.sleep(10)
#         dish_queue.task_done()
#
# dish_queue = queue.Queue()
# for n in range(2):
#     dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
#     dryer_thread.start()
#
# dishes = ['salad', 'bread', 'entree', 'dessert']
# washer(dishes, dish_queue)
# dish_queue.join()



""" 
 Thread와 multiprocessing 의 차이점은, 바로 Thread 에는 terminate() function이 없다는
것이다. thread를 마구잡이로 제거하면 심각한 버그가 생길 수 있기 때문에, terminate가 없는것이다.

 또한 Thread는, 특히나 C나 C++처럼 memory 를 다루는 곳에서 위험하다. thread 에 의해 생기는
버그는 찾기도 힘들며, 고치기도 힘들다. 그래서 thread를 사용하기 위해서는, 반드시 program 내의
code들이 thread safe 이여야 한다. 예를 들어 앞선 thread의 사용처럼 전역 변수를 사용하지 않아
여타 코드에 영향이 안가게 해야 한다.

 process를 여러개 사용하는것은, 여러개의 집마다 각각 한명의 사람이 들어가 있는거와 같다.
거기에 무슨 물체를 두어도 그대로 있게 될 것이다. 반면에 thread를 사용하는것은 마치 유령이
있는것과도 같아서, 유령이 무슨 물체(변수)를 건들여도 파악하기 힘든것과 마찬가지이다.
 
 하지만 thread에 단점만 있는것도 아니다, 만약 thread에 전역 변수가 involved 되있지 않다면
thread 는 유용하고 안전한 방식이 된다. 예를 들어 I/O operation 에서 thread는 각각의
variable 들이 있기 때문에, data를 가지고 다투지 않아서 속도 향상을 기대할 수 있다.

 그리고 또 thread는 때때로 전역 변수를 바꾸는데 좋은 방식이기도 하다.
사실 다중 thread를 사용하는 주요 이유중 하나가 바로, data를 나누고자 할때이다.

 thread를 이용해 변수를 수정할때, data를 안전하게 공유하는 안전한 방법은 바로
'software lock'이다. 변경이 일어나고 있을때, 다른 thread로 하여금 접근을 막는 방식이다.

 아무튼 python 에서는 다음과 같이 권장한다.
- Thread의 경우 : I/O-bound problems.
- Processes, networking, event의 경우 : CPU-bound problem 의 경우. 
 """

"""
concurrent.futures
 concurrent.futures 는 thread 나 multiple process 를 사용할떄 수반하는 수많은 세부사항들을
간단하게 하기 위해 python 3.2에 추가됐다. concurrent.futures 는 asynchronous 한 worker들을 
thread(I/O bound), process(CPU bound)를 이용해 schedule 할 수 있게 해준다.
그들의 상태를 추적하고 결과를 모으기 위해 미래로 돌아갈 것이다. (이게무슨소리지?)
 아래의 예시에서 cf.py를 작성해볼 것이다. 여기서 test function 인 calc() 가 하는 기능은 다음과 같다.

- 1초 동안 sleep.
- argument의 square root를 계산후 return.

이 프로그램에서는 기본값이 3인, 사용할 작업자의 수를 argument로 받아서
thread pool 과 process pool 에서 일하게 하고, 경과시간을 출력한다.
values list 는 다섯 개의 숫자(calc 함수에 한번에 보내질)를 포함한다.
"""

""" 정수를 입력받아 해당 정수만큼의 worker가 프로그램 내에
정해져있는 작업의 양을 처리하는데 얼마나 걸리는지 출력하는 프로그램. """

# cf.py

# from concurrent import futures
# import math
# import time
# import sys
#
# def calc(val):
#     time.sleep(1)
#     result = math.sqrt(float(val))
#     return result
#
# def use_threads(num, values):
#     t1 = time.time()
#     with futures.ThreadPoolExecutor(num) as tex:
#         results = tex.map(calc, values)
#     t2 = time.time()
#     return t2 - t1
#
# def use_processes(num, values):
#     t1 = time.time()
#     with futures.ProcessPoolExecutor(num) as pex:
#         results = pex.map(calc, values)
#     t2 = time.time()
#     return t2 - t1
#
# def main(workers, values):
#     print(f"Using {workers} workers for {len(values)} values")
#     t_sec = use_threads(workers, values)
#     print(f"Threads took {t_sec:.4f} seconds")
#     p_sec = use_processes(workers, values)
#     print(f"Processes took {p_sec:.4f} seconds")
#
# if __name__ == '__main__':
#     workers = int(sys.argv[1])
#     values = list(range(1, 6))  # 1 ~ 5
#     main(workers, values)

"""
 one-second sleep() 은 각 계산에 최소한 1초를 걸리게 하기위함이다. 
그래서 다음과 같이 진행되게 된다.
- worker 가 한명일 경우 : 혼자서 5작업 진행. 그래서 최소 5초 이상이 걸리게 된다.
- worker 가 다섯명일 경우 : 5명이서 5작업. 따라서 각각 하나씩 맡아서 1초 이상이다.
- worker 가 세명일 경우 : 3명이서 5작업. 따라서 2번으로 나눠 진행되므로 최소 2초이다.

 여기서 우리는 의도적으로 square root를 출력하지 않았는데, elapsed time을 강조하기 위해서다.
아무튼 간에 square root를 출력하고 싶다면 아래의 예제를 보라.
"""

# cf2.py 의 코드내용.

# from concurrent import futures
# import math
# import sys
#
# def calc(val):
#     result = math.sqrt(float(val))
#     return val, result
#
# def use_threads(num, values):
#     with futures.ThreadPoolExecutor(num) as tex:
#         tasks = [tex.submit(calc, value) for value in values]
#         for f in futures.as_completed(tasks):
#             yield f.result()
#
# def use_processes(num, values):
#     with futures.ProcessPoolExecutor(num) as pex:
#         tasks = [pex.submit(calc, value) for value in values]
#         for f in futures.as_completed(tasks):
#             yield f.result()
#
# def main(workers, values):
#     print(f"Using {workers} workers for {len(values)} values")
#     print("Using threads:")
#     for val, result in use_threads(workers, values):
#         print(f"{val} {result:.4f}")
#     print("Using processes:")
#     for val, result in use_processes(workers, values):
#         print(f'{val} {result:.4f}')
#
# if __name__ == '__main__':
#     workers = 3
#     if len(sys.argv) > 1:
#         workers = int(sys.argv[1])
#     values = list(range(1, 6))  # 1 ~ 5
#     main(workers, values)

""" 
 이처럼 concurrent.futures 는 다음 예제들처럼
여러개가 동시에 발생하는 task 를 처리하는데 적합하다.

- Crawling URLs on the web
- 파일 processing ex) 이미지 resizing
- Calling services APIs.

 여기 추가적인 내용이 있는 링크가 있지만, 훨씬 기술적이다.
https://docs.python.org/3/library/concurrent.futures.html
"""

"""
Green Threads and gevent
 앞서 봤듯이, 개발자들은 느린 구간을 별도의 thread나 process를 통해 처리한다.
이것의 대표적인 예시로 Apache web server가 해당된다.

 또다른 대안으로는, event-based programming이라는게 있다.
event-based program은 task를 나누어주면서, central event loop를 반복하면서 실행한다.
NGINX web server 가 이와 같이 동작하며, 보통 Apache 보다는 빠르다.

 gevent library 는 event-based 이며, 정돈된 trick을 달성해냈다. 
normal imperative code를 작성하면, coroutine 으로 바꾸어 준다.
어찌보면 generator 와 비슷한데, 다른 generator 와 소통할수 있고 어디에 있는지
계속 추적할 수 있는 generator 이다.
 
 gevent 는 많은 python의 standard object 의 mechanism을 사용하기 위해 변경시킨다.
하지만 몇몇 c로 쓰인 python 내의 code 에서는 적용되지 않기도 한다.

 socket module 내에 gethostbyname 이라는 함수가 있는데, 이게 작동하는 동안 다른것을
할 수 없기 떄문에 기다려야 한다. 반면에 gevent version 을 사용하면 여러개의 site를
독립적으로 검색할 수 있다. 한번 다음예제를 보자.
"""

# gevent_test.py 의 코드

# import gevent
# from gevent import socket
# hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
#          'www.antique-taxidermy.com']
# jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# gevent.joinall(jobs, timeout=5)
# for job in jobs:
#     print(job.value)

""" gevent.spawn() 함수는 greenlet(green thread, microthread) 를 생성하는데
이는 각각의 gevent.socket.gethostbyname(url)을 실행시키기 위함이다.
기존의 normal thread 와의 차이점은 block 시키지 않는다는 것이다."""



















