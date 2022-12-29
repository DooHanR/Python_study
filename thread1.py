""" process 대신에 thread를 실행해보기 위한 test 파일이다. """

import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,
                             args=("I'm function %s" % n,))
        p.start()

