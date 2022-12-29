import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print(f"Washing {dish} dish")
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print(f"Drying {dish} dish")
        input.task_done()

""" 메인 함수를 선언해야 오류가 안생기는듯 하다. 왜일까? 
-> 메인 함수 선언시 논리적 구조가 개선되고 독립된 실행 프로그램으로써 다루어진다고 한다.
아직 잘 모르겠으니, 더 공부해보자."""

if __name__ == '__main__':
    dish_queue = mp.JoinableQueue()
    dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    washer(dishes, dish_queue)
    dish_queue.join()


""" JoinableQueue와 join method를 통해 washer가 모든 dish가 말려졌음을 알기위해 사용됨. 
이 위의 queue 는 python iterator 처럼 보이지만, 사실 washer와 dryer 사이의 communication에
따라서 process가 시작된다.
 또한 이외에도 다양한 queue type이 multiprocessing module 내에 존재하며
다음의 링크를 통해 확인해 볼 수 있다. """

# http://bit.ly/multi-docs


