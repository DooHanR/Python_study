import multiprocessing
import os

def whoami(what):
    print("Process %s says: %s" % ( os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main Program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami,
                                    args=("I'm function %s" % n, ))
        p.start()


""" Multiprocessing 내의 Process() function은 새로운 process를 생성하고
내부의 do_this() 을 실행시킨다. 앞서 이 코드에서는 4번 반복했기 때문에
4번 생성하고 4번 실행하게 되는것이다. 

 또한 multiprocessing 내에는 작업에 걸리는 시간을 줄이기 위해 많은 bell과 whistle
이 있으며, process 간의 상호소통등을 가능케 하는 다양한 기능등도 포함하고 있다."""