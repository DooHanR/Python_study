"""Dictionaries
dictionary는 list와 비슷하지만 여러모로 다른점이 많다.
1. item의 순서는 상관이 없다.
2. 각각의 value에 특정한 key를 associate 시키는 형식이다.
(이때 key들은 python의 immutable type들이다. string, boolean, tuple ..)
3. dictionary는 mutable이다. 따라서 수정이 가능하다."""


""" Create with {}
Dictionary는 다음과 같은 구성요소로 이루어진다.
1. curly brakcet '{}'
2. comma로 분리되있는 key : value pairs."""

# empty_dict = {}
# print(empty_dict)
#
# bierce = {
#     "day": "A period of twenty-four hours, mostly misspent",
#     "positive": "Mistaken at the top of one's voice",
#     "misfortune": "The kind of fortune that never misses",
#     }
#
# print(bierce)

# list 나 tuple, dictionary 에서 last item의 뒤에
# comma 를 붙이는게 흔한데, 가시성을 위한것으로 해두면 유익하다


""" Create with dict()
너무 많은 quote와 curly bracket은 입력하기만 번거로울 뿐이다.
따라서 이를 방지하기 위해 dict() function이 있다."""

# # traditional way
# acme_customer = {'first': 'Wile', 'middle': 'E', 'last':'Coyote'}
# print(acme_customer)
#
# # using dict
# acme_customer = dict(first="While", second="E", last="Coyote")
# print(acme_customer)
# # 이때 argument name은 반드시 legal variable names 이여야한다.
# # no space, no reserved words.


"""Convert with dict()
dict() function 을 이용해서 two-value sequences를
dictionary로 convert 할 수 있다. 예시와 함께 살펴보자."""

# lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# print(dict(lol))  # 길이가 오직 2이여야만 한다. 그렇지않으면 error 발생하는 모습.
# print(lol)  # 원본은 그대로인 모습.
#
# lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# print(dict(lot))
# print(lot)
#
# los = ['ab', 'cd', 'ef']
# print(dict(los))
# print(los)
#
# tos = ('ab', 'cd', 'ef')
# print(dict(tos))
# print(tos)
#
# # zip과 함께 dict를 사용하면 더 쉽게 사용할 수 있다.
# print(dict(zip(los, tos)))


"""Add or Change an item by [key]
dictionary에 item을 추가하는 것은 쉽다. 그저 item을 key와 value에
알맞게 할당해주면 된다. 이미 존재할 경우에는 대체되고, 그렇지 않으면
새롭게 하나 추가된다. 그리고 list와 다르게 범위 걱정할 필요도 없다.
한번 예시를 한번 해보자."""

# pythons = {
#     'Chapman': 'Graham',
#     'Cleese': 'John',
#     'Idle': 'Eric',
#     'Jones': 'Terry',
#     'Palin': 'Michael',
#     }
# print(pythons)
#
# # 이때 우리가 Terry Gilliam 을 빼먹었다고 가정, 넣으려고 해보자.
# pythons['Gilliam'] = 'Gerry'
# print(pythons)
# pythons['Gilliam'] = 'Terry' # 변경됨.
# print(pythons)
#
# # key는 unique 한것으로, 만약 중복된다면 last key만이 출력이 된다.
# some_pythons = {
#     'Graham': 'Chapman',
#     'John': 'Cleese',
#     'Eric': 'Idle',
#     'Terry': 'Gilliam',
#     'Michael': 'Palin',
#     'Terry': 'Jones' # Terry가 두개이고 Gilliam, Jones 중 Jones가 출력. 순서에 유의.
# }
# print(some_pythons)


"""Get an item by [key] or with get()
dictionary의 가장 흔한 사용법이기도 하다.
예시를 통해 자세히 알아보자."""

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones' # Terry가 두개이고 Gilliam, Jones 중 Jones가 출력. 순서에 유의.
}

print(some_pythons['John'])
# print(some_pythons['Groucho'])

""" 찾고자 하는게 존재하지 않을 경우 exception이 발생하는데 이를 피하는 방법이 있다."""
# 1. 'in'을 통해 해당하는게 있는지 확인하기.
print('Groucho' in some_pythons)




















































































