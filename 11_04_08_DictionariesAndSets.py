# 정보를 머리속에 조직화하는게 중요하다!!

"""Dictionaries
dictionary는 list와 비슷하지만 여러모로 다른점이 많다.
1. item의 순서는 상관이 없다.
2. 각각의 value에 특정한 key를 associate 시키는 형식이다.
(이때 key들은 python의 immutable type들이다. string, boolean, tuple ..)
3. dictionary는 mutable이다. 따라서 수정이 가능하다."""


""" Create with {}
Dictionary 만드는 방법.
Dictionary는 다음과 같은 구성요소로 이루어진다.
1. curly bracket '{}'
2. comma로 분리돼있는 key : value pairs."""

# empty_dict = {}
# print(empty_dict)
#
# bierce = {
#     "day": "A period of twenty-four hours, mostly misspent",
#     "positive": "Mistaken at the top of one's voice",
#     "misfortune": "The kind of fortune that never misses", # 가시성을 위한 comma
#     }
#
# print(bierce)

# list 나 tuple, dictionary 에서 last item의 뒤에
# comma 를 붙이는게 흔한데, 가시성을 위한것으로 해두면 유익하다


""" Create with dict()
dict를 dict() 함수로 만들어보기.
너무 많은 quote와 curly bracket은 입력하기만 번거로울 뿐이다.
따라서 이를 방지하기 위해 dict() function이 있다."""

# # traditional way
# acme_customer = {'first': 'While', 'middle': 'E', 'last': 'Coyote'}
# print(acme_customer)
#
# # using dict
# name = dict(Doo='HanEol', Lee='HaNa', Yee='MinHo')
# acme_customer = dict(first="While", second="E", last="Coyote")
# print('what is type of name: ', type(name))
# print(name)
# print(acme_customer)
#
# # 이때 argument name은 반드시 legal variable names 이여야한다.
# # no space, no reserved words.


"""Convert with dict()
기존의 자료를 dict() 을 이용해 dict로 만들기. 조건에 유의.
dict() function 을 이용해서 two-value sequences를
dictionary로 convert 할 수 있다. 예시와 함께 살펴보자."""

# lol = [['a', 'b'], ['c', 'd'], ['e', 'f']] # list를 dict으로
# print(dict(lol))  # 길이가 오직 2이여야만 한다. 그렇지않으면 error 발생하는 모습.
# print(type(lol))
# print(lol)  # 원본은 그대로인 모습.
#
# lot = [('a', 'b'), ('c', 'd'), ('e', 'f')] # list을 dict로, tuple 인줄.
# print(dict(lot))
# print(type(lot))
# print(lot)
#
# los = ['ab', 'cd', 'ef'] # list 를 dict로
# print(dict(los))
# print(type(los))
# print(los)
#
# tos = ('ab', 'cd', 'ef') # tuple을 dict로
# print(dict(tos))
# print(type(tos))
# print(tos)
#
# # zip과 함께 dict를 사용하면 더 쉽게 사용할 수 있다.
# print(dict(zip(los, tos)))


"""Add or Change an item by [key]
Dictionary에 key를 이용해 item을 바꾸거나 추가하기
ictionary에 item을 추가하는 것은 쉽다. 그저 item을 key와 value에
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
# print(pythons['Chapman'])  # key를 이용해 value를 호출하는 모습.
#
# # 이때 우리가 Terry Gilliam 을 빼먹었다고 가정, 넣으려고 해보자.
# pythons['Gilliam'] = 'Gerry' # key와 value를 삽입.
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
dictionary 에서 [key] 혹은 key() 함수로 item 을 얻어내기.
dictionary의 가장 흔한 사용법이기도 하다.
예시를 통해 자세히 알아보자."""

# some_pythons = {
#     'Graham': 'Chapman',
#     'John': 'Cleese',
#     'Eric': 'Idle',
#     'Terry': 'Gilliam',
#     'Michael': 'Palin',
#     'Terry': 'Jones' # Terry가 두개이고 Gilliam, Jones 중 Jones가 출력. 순서에 유의.
# }

# print(some_pythons['John'])
# print(some_pythons['Groucho'])
""" 찾고자 하는게 존재하지 않을 경우 exception이 발생하는데 이를 피하는 방법이 있다."""
# # 1. 'in'을 통해 해당하는게 있는지 확인하기.
# print('is it there \'Groucho\'?: ', 'Groucho' in some_pythons)
#
# # 2. get()을 사용해서 key를 통해 value를 얻기.
# print(some_pythons.get('John')) # key를 입력하면 value가 반환됨.
# print(some_pythons.get('Groucho', 'Not there'))  # 해당 key에 상흥하는 value가 없을때.
# print(some_pythons.get('Groucho')) # None을 반환한다.


""" Get All Keys with keys()
key() 함수를 통해 dictionary 내의 모든 key 얻기.
keys() function을 통해 dictionary 내에 모든 key를 얻을 수 있다.
다음에서는 좀 다른 dictionary sample을 사용 할 것이다."""

# signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
# print(signals.keys())  # list로 변경시키고 싶다면 list(signals.keys())를 사용하자!
# print(list(signals.keys()))


"""Get All Values with values()
values()를 통해서도 얻을 수 있다."""

# print(signals)
# print(list(signals.keys()))  # key
# print(list(signals.values()))  # key에 상응하는 value


"""Get All Key-Value Pairs with items()
dictionary 에서 key-value pair를 얻고싶다면 items() 함수를 사용하라."""

# print(signals.items())
# print(list(signals.items()))  # tuple의 형태로 return 된다.


"""Get Length with len()"""

# print(len(signals))  # key-value pair의 개수를 알려줌.


"""Combine Dictionaries with {**a, **b)
dictionarie를 merge 하는 새로운 형식의 방법이다."""

# first = {'a': 'agony', 'b': 'bliss'}
# second = {'b': 'bagels', 'c': 'candy'}
# exam = {**first, **second} # 두 dict를 합치는 모습.
#
# print(exam)
# print({**first, **second})
#
# third = {'d': 'donuts'}
# print({**first, **second, **third})


"""Combine Dictionaries with update()
한 dictionary 에서 다른 dictionary로 key와 value를 복사하고 싶을때
update() function을 사용할 수 있다."""

# pythons = {
#     'Chapman': 'Graham',
#     'Cleese': 'John',
#     'Gilliam': 'Terry',
#     'Idle': 'Eric',
#     'Jones': 'Terry',
#     'Palin': 'Michael',
#     }
# print(pythons)
#
# others = {'Marx': 'Groucho', 'Howard': 'Moe'}
#
# # 이제 pythons에 others를 추가해보자.
# pythons.update(others)
# print(pythons)
#
# # 만약 second dictionary가 same key를 가지고 있으면 어떻게 될 까?
# first = {'a': 1, 'b': 2}
# second = {'b': 'platypus'}
# first.update(second)
# print(first)  # 두번째 dictionary 가 이기게 된다.


"""Delte an Item by Key with del
여기서는, dictionary 내에의 item을 del 명령어를 통해
제거하는 방법에 대해 알아 볼것이다."""

# print(pythons)
# del pythons['Marx']
# print(pythons)


"""Get an Item by Key and Delete It with pop()
Dictionary 에서도 마찬가지로 pop()을 통해 item 을 제거함과 동시에
key를 얻어낼 수 있다. get()과 del의 combine 이라고도 볼 수 있다. 
다음 예시를 보자."""

# pythons = {
#     'Chapman': 'Graham',
#     'Cleese': 'John',
#     'Gilliam': 'Terry',
#     'Idle': 'Eric',
#     'Jones': 'Terry',
#     'Palin': 'Michael',
#     }

# print('length of pythons before pop():', len(pythons))
# exam = pythons.pop('Palin')
# print('pop has done, what extracted:', exam)
# print('pop() has done, now left:', len(pythons))
# # print(pythons.pop('You')  # 존재하지 않을 경우 error 발생.
# print(pythons.pop('You', 'I')) # 하지만 두번째 인자를 넣을경우에는 정상 출력. 처리는 X.


"""Delete All Items with clear()
dictionary의 모든 item을 제거하고 싶으면 두개의 방법이 있다.
1. clear() 함수를 사용하거나.
2. empty dictionary 를 재 할당하거나."""

# print(pythons)
# pythons = {}
# print('python deleted:', pythons)
# pythons.clear()
# print('python deleted:', pythons)


"""Test for a Key with in
dictionary 내에 특정 key가 존재하는지 확인하기 위해 'in' 키워드를 사용한다."""

# pythons = {
#     'Chapman': 'Graham',
#     'Cleese': 'John',
#     'Gilliam': 'Terry',
#     'Idle': 'Eric',
#     'Jones': 'Terry',
#     'Palin': 'Michael',
#     }
#
# print('is there \'Chapman\' in pythons?:', ('Chapman' in pythons))
# print('is there \'Robert\' in pythons?:', ('Robert' in pythons))


"""Assign with '='
list를 통해서 dictionary를 통해 변경이 일어나면, 모두 반영/적용 된다."""

# signals = dict(green='go', yellow='go faster', red='smile for the camera')
# save_signals = signals
# signals['Blue'] = 'confuse everyone'
# print(save_signals)  # 놀랍게도 save_signals 도 마찬가지로 변경된 모습.


"""Copy with copy()
위에서 겪은 복사본까지 변하는 경험을 copy() 함수를 통해 방지 할 수 있다."""
# signals = dict(green='go', yellow='go faster', red='smile for the camera')
# original_signals = signals.copy()
# signals['Blue'] = 'hey stop'
# print('is it same?:', (signals == original_signals))

"""위의것은 shallow copy라고 하는데, dictionary values 들이 immutalbe 일경우
에 해당한다. 만약에 그들이 mutable 이라면 deepcopy()를 사용해야 한다."""


"""Copy Everything with deepcopy()
앞서 했던 것과 다르게 red의 value가 이번에는 list 라고 가정해보자."""

# signals = {'green': 'go',
#            'yellow': 'go faster',
#            'red': ['stop', 'smile'], }
#
# signals_copy = signals.copy()
# signals['red'][1] = 'sweat'
# print('is it equal?: ', (signals_copy == signals))  # 똑같이 바뀌었다. 문제 발생!

# deepcopy 를 사용하면 list와 같이 mutable variable도 변하는 것을 방지할 수 있다.

# import copy
# signals = {'green': 'go',
#            'yellow': 'go faster',
#            'red': ['stop', 'smile'], }
#
# signals_copy = copy.deepcopy(signals)
# signals['red'][1] = 'hello'
# print('is it same? signals vs signals_copy:', (signals_copy == signals))
# # list 내용도 변하지 않은 모습! 잘 알아두자.


"""Compare Dictionaries
list와 tuple처럼 dictionary도 '==' 와 '!=:' 로 비교 할 수 있다."""

# a = {1:1, 2:2, 3:3}
# b = {3:3, 1:1, 2:2}
# print('is it same? a,b:', (a == b))


"""Iterate with for and in.
dictionary 에서 iterate 하는것은 key 를 return 한다."""

# accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
#               'person': 'Col. Mustard'}

# for card in accusation.keys():
# for card in accusation.values():  # 이 경우에는 value 값들이 출력 된다.
# for card in accusation.items():  # 이 경우 에는 value, key 둘다 출력됨.
# for card in accusation:
#     print(card)  # key 가 출력됨.

# for card, contents in accusation.items():
#     print('Card', card, 'has the contents', contents)


"""Dictionary Comprehensions.
dictionary 에서도 마찬가지로 comprehension을 사용할 수 있다."""

# 예시) {key_expression : value_expression for expression in iterable}
# word = 'letters'
# letter_counts = {letter: word.count(letter) for letter in word}
# print(letter_counts)

# 위의 방식이 약간 비효율적이어서, 더 pythonic 한 것이 있다.
# word = 'letters'
# letter_counts = {letter: word.count(letter) for letter in set(word)}
# print(letter_counts)

# list comprehension 처럼, dictionary 에서도 'if' 와 'multiple for'를 지원한다.
# {key_expression : value_expression for expression in iterable if condition}
# vowels = 'aeiou'
# word = 'onomatopoeia'
# vowel_counts = {letter: word.count(letter) for letter in set(word)
#                 if letter in vowels}
#
# print(vowel_counts)

"""PEP 274에 dictionary comprehension에 대한 더 많은 예시가 있다.
그리고 dictionary의 comprehension이 다소 복잡한듯? 이해가 약간 안되는 여지가 있다."""


"""Sets
set은 value없이 key만 있는 dictionary와 유사하다.
보통 무언가가 존재한다 라는것만을 알고싶을때, 보통 사용되며
key들만 있는 형태이다. 만약 key에 정보를 덧붙이고 싶으면
value와 함께있는 dictionary를 써라."""


"""Create with set()
set을 만드는데는 두가지 방식이 있다.
1. set()을 사용하기
2. {} 사용하기.
다음 예시를 통해 확인해보자."""

# empty_set = set()
# print('here is set:', empty_set, type(empty_set))
#
# even_numbers = {0, 2, 4, 6, 8}
# print('is it set too?:', even_numbers, type(even_numbers))

"""왜 empty_set 에서 {}을 사용하지 않느냐고 물을 수 있다.
그 이유는, {}을 사용하면 empty dictionary 를 만들기 때문이다.
이는 dictionary 가 {}에 대한 우선권을 가지고 있기 때문이며 마찬가지로
표시될때 {}가 아닌 set()으로 나오는것도 이 이유 때문이다."""


"""Convert with set()
list, string, tuple이나 dictionary등의 duplicate value를 제거해서
set으로 만들 수 있다. 다음의 예시를 통해 한번 살펴보자."""

# print(set('letters'))  # 출력 결과를 보면 중복되는것도 하나만 있다.
# print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
# print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
# print(set({'apple': 'red', 'orange': 'orange', 'cheery': 'red'}))

# dictionary 의 경우 key만 출력 된다.


"Get Length with len()"

# reindeer = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
# print('what is length of set:', len(reindeer))


"""Add an Item with add()
add() 함수를 통해 item을 set에 추가 시킬 수 있다."""
