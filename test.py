""" test용 python 파일. """
# from random import choice

places = ["McDonalds", "KFC", "Burger King", "Taco Bell",
          "Wendys", "Arbys", "Pizza Hut"]

# def pick():  # 아래의 docstring에 주의. 함수에 대한 설명임!
#     """ Return random fast food pace"""
#     return choice(places)


def pick():
    """ 이게 더 안전하기는 하지만 더많은 typing 을 필요로 한다.
    자신이 사용하기에 편한대로 사용하도록 하라. 누구는 import 된 것을
    확실히 알기 위해 위에 몰아넣기도 한다. """
    import random
    return random.choice(places)

