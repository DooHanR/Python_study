""" 여기서는 Tuple과 List에 대해 공부할 것.
근데 Tuple은 도대체 뭐지?

대부분의 프로그래밍이 조합하고 분해하는 과정이라면
여기서 나오는 Tuple과 List는 톱이나 글루건이 될 것.
그리고 또한 list와 tuple은 기존의 것들이 원자라면
원자의 조합인 분자라고 볼 수 있다.

List와 Tuple의 차이점은 변경 가능 여부이다.
Tuple의 경우 immutable이지만 List의 경우 변경이 가능하다."""

"""Tuples. Create with Commas and ()
Tuple의 특징이라면 '()' 로 이 동그라미 괄호로 형성된다."""


# empty_tuple = ()
# print(empty_tuple)

# test = 'abcd'
# one_marx = 'Groucho',  # 단순 string과 tuple의 차이점에 주의하자.
# one_marx = ('Groucho', )
# print(test)
# print(one_marx)
# print(type(test))
# print(type(one_marx))

""" 괄호 없이도 튜플 정의 가능. but 가시성 측면에서 괄호를 사용하는게 더 좋다. """
# marx_tuple = ('Groucho', 'Chico', 'Harpo')
# print(marx_tuple)
# print(type(marx_tuple))


""" 괄호를 사용하지 않았을 경우, single element tuple은
 function의 argument로 pass불가 """  # 이거 솔직히 뭔소린지 모르겠다.

# one_marx = ('Groucho',)
# one_marx = 'Groucho',
# print(type(one_marx))
# print(one_marx)
# print(type('Groucho')) # 'Groucho' 자체는 string 취급을 받는 모습.


"""Tuple의 기능.
한번에 여러개의 변수를 지정할 수 있게 한다."""

# marx_tuple = ('Grucho', 'Chico', 'Harpo')
# print(len(marx_tuple))
"""for i in len(marx_tuple) 하니까 문제 발생.
범위를 지정해줘야 하는듯."""
# a, b, c = marx_tuple
# print(a, b, c)
# for i in range(len(marx_tuple)):
#     print(marx_tuple[i])


# 위의 것을 tuple unpacking 이라고도 불린다.


"""tuple을 이용해 temporary variable을 사용하지 않고 values를 바꿀 수 있다."""

# password = 'swordfish'
# icecream = 'tuttifrutti'
# print(password)
# print(icecream + '\n')
#
# password, icecream = icecream, password
# print(password)
# print(icecream)


"""tuple() 함수를 이용해 다른 타입의 것들로 tuple을 만들 수 있다.
list에 '\n'을 같이 쓰는게 안되는 거 같다."""

# marx_list = ['Groucho', 'Chico', 'Harop']
# print(marx_list)
# print(type(marx_list))
# tupled_marx_list = tuple(marx_list)
# print(tupled_marx_list)
# print(type(tupled_marx_list))


""" +를 이용해서 tuple combine 하기."""

# print(('Groucho', ) + ('Chico', 'Harpo'))
# tuple1 = ('Groucho',)
# tuple2 = ('Chico', 'Harpo',)
# tuple3 = tuple1 + tuple2
# print(type(tuple3))
# print(tuple3)

# 여타 다른곳에서 쓰는거랑 똑같은 거 같다.


"""Compare Tuple. list comparison 과 흡사하게 작동된다."""

# a = (7, 2)
# b = (7, 2, 9)
# c = (1, )
# d = (2, )
#
# print(type(a), type(b))
# print(a == b)
# print(a <= b)
# print(a < b)
# print(c < d)
# print(c > d)


"""Tuple interation with for and in, 다른 type들의 iteration
과 거의 유사하게 작동된다."""

# words = ('fresh', 'out', 'of', 'ideas')
# for word in words:
#     print(word)


"""Tuple을 수정하기는 불가능하다. string과 마찬가지로 immutable variable 이기때문.
하지만 string과 마찬가지로 combine이나 concatenate를 할 수는 있다."""

# t1 = ('Fee', 'Fie', 'Foe')
# t2 = ('Flop', )
# print(id(t1))
# t1 += t2
# print(t1)
# print(id(t1))

# 바뀐것처럼 보이지만 실제로는 변수가 새로운 값을 나타내고 있음을 알 수 있다.


"""LIST
list는 순서나 내용이 변할 수 있을때, 그들을 추적하기 용이하다.
또한 string이나 tuple과 다르게 mutable이며, 대체, 삭제, 삽입 등등
다양한 작업을 진행 할 수 있다."""


"""List는 0개 부터 그 이상까지의 elements로 구성되며,
',' 와 '[, ]'로 구성된다."""

# empty_list = []
# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# first_names = ['Grahm', 'John', 'Terry', 'Terry', 'Michael'] # values
# leap_years = [2000, 2004, 2008]
#
# print(first_names)

"""순서에 상관없이 특정 value를 keep track 하고 싶다면 list보단 set이 더 적합하다.
set 에 대해서는 chapter7에서 더 자세히 알아보게 될 것."""


"""Create or Convert with list()
list() function을 통해 empty list를 만들 수 있다.
혹은 다른 iterable data type 등을 list로 변경 할 수 있다."""

# another_empty_list = list()
# print(another_empty_list)
#
# print(list('cat')) # string의 list화 되시겠다.
# a_tuple = ('ready', 'fire', 'aim')
# print(list(a_tuple)) # ()가 []로 바뀌는 차이정도?


"""Create From a string with split()"""

# # split()을 이용, separator를 기준으로 string을 나눌 수 있다.
#
# talk_like_a_pirate_day = '9/19/2019'
# print(talk_like_a_pirate_day.split('/'))
#
# # 만약에 separtor 가 원본 string에 여러개가 있다면?"""
#
# splitme = 'a/b/c//c/d///e'
# print(splitme.split('/'))
# print(splitme.split('//'))


"""Get an item by [ offset ]"""

# # string에서 했던것처럼 list 에서도 offset을 이용, single value를 추출 할 수 있다.
# marxes = ['Groucho', 'Chico', 'Harpo']
# for i in range(0,3):
#     print(marxes[i])
# for i in range(2,-1,-1):
#     print(marxes[i])


"""Get items with a Slice"""

# # list에서도 마찬가지로 slice를 통해 추출해낼 수 있다.
# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes[0:3])
# print(marxes[::-1])

""" 이런 slice 들을 통해서는 list 자체를 변화시킬 수는 없다.
따라서 바꾸기 위해서는 list.reverse()와 같은게 필요하다."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# marxes.reverse()
# print(marxes)

""" slice는 초과해도 exception을 나타내지는 않지만 아무것도 출력하지 않는다."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes[4:])
# print(marxes[-6:])


"""Add an item to the End with append()
일반적인 방식으로는 append()를 이용해서 덧붙인다.
 이것은 끝에 덧붙이는 것임을 주의하라."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes)
# marxes.append('Zeppo')
# print('after append :', marxes) # print시 +는 합치는거 ,는 연달아서 ,가 더 좋은듯.

"""Add an item by Offset with insert
insert를 사용해서 리스트의 특정 offset에 삽입할 수 있다.
이때 그 범위를 초과해도 끝에 알아서 삽입하니 걱정 말라."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# marxes.insert(3, 'Gummo')
# print(marxes)
#
# marxes.insert(10, 'Zeppo')
# print(marxes)


"""Duplicate All items with *
*를 이용해서 string이나 혹은 list에서도 복사할 수 있다."""

# print(["blah"] * 3)
# print("go " * 3)
# print(["hey", "why"] * 3)

"""Combine Lists by Using extend() or +
extend()를 사용해서 list끼리 merge할 수 있다.
다음을 한번 살펴보자."""

# marxes = ['Hey', 'You']
# others = ['Why', 'something wrong?']
# marxes.extend(others)
# print(marxes)

# start = ['This', 'is']
# end = ['Where', 'we', 'go']
# start.extend(end)
# print(start)

"""혹은 '+'나 '+='를 쓰는 방법도 있다."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# others = ['Gummo', 'Karl']
# print(marxes)
# marxes += others
# print(marxes)

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# others = ['Gummo', 'Karl']
# marxes.append(others)
# print(marxes)

# 이 경우 others 라는 list가 list안에 들어가게 되는것으로
# 리스트는 여러 종류의 type을 포함할 수 있다라는 것임을 나타낸다.


""" Change an item by [ offset ] """

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes)
# marxes[2] = 'Wanda'
# print(marxes)

# List는 위와 같은 방식으로 변경이 가능하지만
# String은 immutable 이기 때문에 안된다는 점에 유의하라.


"""Change Items with a Slice
앞서서는 slice를 통해 sublist를 얻는 방법에 대해 알아봤다.
하지만 여기서는 slice를 이용해 sublist에 value를 assign하는
방식에 대해 알아볼 것이다."""

# numbers = [1, 2, 3, 4]
# print(numbers)
# numbers[1:3] = [8, 9] # slice [1:3] 1~2를 의미.
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers[1:3] = [7, 8, 9] # 범위가 정확하지 않아도 해당 내용을 모두 삽입한다.
# print(numbers)

# numbers = [1, 2, 3, 4]
# print(numbers)
# numbers[1:3] = []
# print(numbers)


""" Slice를 통해서 item을 바꿀때, 이 경우에는 숫자를 예시로 들었지만
righthand 쪽이 반드시 같이 숫자일 필요는 없다."""

# numbers = [1, 2, 3, 4]
# print(numbers)
# numbers[1:3] = 'wat?' # 이 경우 해당 범위내에 'wat?' 를 삽입하게 된다.
# print(numbers)


""" Delete an item by Offset with del 
del을 이용해 offset에 있는 특정 item 삭제하기."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
# print(marxes[-1])
# print(marxes)
# del marxes[-1]
# print(marxes)
#
# print()
#
# marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
# print(marxes)
# del marxes[1]
# print(marxes)

# test = ['hey', 'you', 'can', 'do', 'this']
# print(test)
# del test[-2]
# print(test)

"""이때 del 명령어가 string에 포함되어있는게 아닌
python의 자체적인 명령이기 때문에 string.del 과 같은 사용에 주의하라."""


"""Delete an item by Value with remove()
만약 어디있는지도 모르겠고 뭘 삭제하건간에 별 관심이 없다면
string의 string.remove() function을 사용하라."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes)
# marxes.remove('Groucho')
# print(marxes)
#
# test = ['hey', 'stop', 'there']
# print(test)
# test.remove('stop') # 명시적으로 표시해야함. test.remove() <-exception 발생.
# print(test)

# 만약 duplicate 해서 동일한게 여러개가 있다면
# 발견 되는 최초의 것을 remove 함수가 제거한다.


"""Get an Item by Offset and Delete it with pop()
pop()를 이용해서, list에서 item을 얻는것과 동시에 list 에서 제거할 수 있다."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# print(marxes)
# abcd = marxes.pop()
# abc = marxes.pop(2)
# print(abcd)
# print(abc)
# print(marxes)

# 이는 어찌보면 stack에서의 LIFO나 FIFO를 구현하는 것과 마찬가지이다!.


"""Delete All items with clear()"""

# work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
# print(work_quotes)
# work_quotes.clear()
# print(work_quotes)

# for_test = ['hey', 'you', 'do', 'this', 'shit']
# print(for_test)
# for_test.clear()
# print(for_test)

"""Find an Item's Offset by Value with Index()
value를 통해 list 내의 offset을 알고싶다면, index()를 사용하라!."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# print(marxes)
# print(marxes.index('Groucho'))
# print(marxes.index('Zeppo'))
#
# simpsons = ['Lisa', 'Bart', 'Marge', 'Bart']
# print(simpsons.index('Bart')) # 여러개가 있는경우는 최초의 것의 index만 출력.

# for_test = ['this', 'is', 'one', 'of', 'you']
# print(for_test)
# print(for_test.index('is'))
# print(for_test.index('one'))

# 해당 value의 index를 알고자 할때 유용하다.

"""Test for a Value with in
해당 list내에 해당 value가 있는지 pythonic 한 방식으로 
확인하는 방법이다."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# print('Groucho' in marxes)
# print('Bob' in marxes)

# for_test = ['i', 'hate', 'this', 'way']
# print('hate' in for_test)
# print('ohamma' in for_test)


""" Count Occurrences of a Value with count()
list에 특정 value 가 얼마나 occur 하는지 확인하고 싶다면
count()함수를 이용해라."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes.count('Harpo'))
# print(marxes.count('Bob'))

# snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
# print(snl_skit.count('cheeseburger'))


# begin at 11/02 3:24 pm
"""Convert a List to a String with join()"""

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes)
# print(type(marxes))
# joined_marxes = ', '.join(marxes) # list가 아닌 string method라 형태가 이런식.
# print(joined_marxes) # 결과 output도 string이다.
# print(type(joined_marxes))

""" join에서는 argument로 string이나 혹은 iterable 한 것들이 모두 올 수 있다.
왜냐면 join이 단순히 list의 method가 아니기 떄문이다. string의 method이다.
join()이 split()의 정반대임을 기억한다면 도움이 될 것."""

# friends = ['Harry', 'Hermione', 'Ron']
# separator = ' * '
# joined = separator.join(friends) # separator 로 friends 들을 join한다.
# print(joined)
# # ', '.join(marxes), separator.join(marxes) 의 차이점에 유의하라.
# separated = joined.split(separator)
# print(separated)
#
# print(separated == friends)

# finished at 11/02 5:47 pm
# start at 11/02 9:18 am

""" Reorder Items with sort() or sorted()
value를 기준으로 list 내에서 정렬하고 싶을때, python 에서 2가지 방식을 제공.
(1)list method: sort()
(2)general function: sorted()
숫자->올림차순, 문자->알파벳순"""

# marxes = ['Groucho', 'Chico', 'Harpo']
# sorted_marxes = sorted(marxes) # sorted는 원본을 변경 x
# print(sorted_marxes)
# print(marxes)
#
# marxes.sort()
# print(marxes) # sort()는 원본을 변경시키는 모습을 보여준다.

"""string 내에 여러 type이 혼용 되어있을 수도 있다. 예를 들어
integer와 float등. 수식 에서는 어차피 통합되기 때문에 별 상관이 없을 수 있다."""

# numbers = [2, 1, 4.0, 3]
# print(numbers)
# numbers.sort()
# print(numbers)
# print(type(numbers[0]))
# print(type(numbers[3]))
# print(numbers[0] + numbers[3])
#
# # 내림차순으로 하고 싶을때
# numbers = [2, 1, 4.0, 3]
# numbers.sort(reverse=True)
# print(numbers)


""" Get Length with len()
list 에서 length는 item이 몇개나 있는지를 리턴한다."""

# marxes = ['Groucho', 'this', 'sleep']
# print(len(marxes))
# print(len(marxes[0])) # offset 0에 있는것의 길이.


""" Assign with = """
# a = [1, 2, 3]
# print(a)
# b = a
# print(b)
#
# a[0] = 'surprise'
# print(a) # 흥미롭다. a 만 바뀌었는데 b도 바뀌는 모습을 볼 수 있을것이다.
# print(b)
#
# b[0] = 'is it real?'
# print('this is a: ', a)
# print('this is b: ', b)

""" 이것은 앞서 말한 box 예시 때문인데, 똑같은 box를 서로다른 이름으로만
가리키고 있는 상황이기 때문에 안에 내용물이 변경되면서 자연스레 똑같이 변하는것."""


""" Copy with copy(), list(), or a Slice 
다음의 method 들을 이용해 기존 list의 value들을
독립적이고, 새로운 list에 copy 할 수 있다.
1. list copy() method, 
2. list() conversion method,
 3.list slice [:] """

# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
#
# print('a, b, c, d: ', a, b, c, d)

""" assign 과는 다르게 여기서는 copy 취급을 한다.
이전과 다르게, a가 바뀌어도 b,c,d 의 내용이 변치않음을 의미한다."""

# a[0] = 'hey stop this shit. i gonna go to home!'
# print('this is a: ', a)
# print('and b, c, d: ', b, c, d)


""" Copy Everything with deepcopy()
copy() function은 list의 value가 immutable일때는 제대로 작동한다.
하지만 mutable value(lists, tuples, dicts ...)들은
reference가 되기 때문에 origin의 변경은 copy에도 반영이 된다."""

# a = [1, 2, [8, 9]]
# # b = a.copy()
# b = [1, 2]
# c = list(a)
# d = a[:]
#
# list = a, b, c, d
# a[2][1] = 10
#
# for i in list:
#     print(i)

""" a[2]는 [8,9]로 list에 해당한다. 따라서 이는 mutable요소이고
따라서 이렇게 바뀌게 되는데, 이러한 경우를 방지하기위해
deepcopy() function을 사용해야 한다."""

# import copy
# a = [1, 2, [8, 9]]
# b = copy.deepcopy(a)
# print(a, b)
#
# a[2][1] = 10
# print(a, b)


"""Compare Lists
list도 마찬가지로 '==', '<' 등등을 이용해 비교를 할 수 있다."""

# a = [7, 2]
# b = [7, 2, 9]
# print(
#       a == b,
#       a <= b,
#       a < b
#       )


"""Iterate with for and in
앞서 chapter 6 에서 string 에서 iterate 해봤을텐데,
사실 list를 통해 iterate 하는게 보다 common하다."""

# cheeses = ['bri', 'gjetost', 'havarti']
# for cheese in cheeses:
#     print(cheese)

# cheeses = ['brie', 'gjetost', 'havarti']
# for cheese in cheeses:
#     if cheese.startswith('g'):
#         print("i won't eat anything that starts with 'g'")
#         break
#     else:
#         print(cheese)

# cheeses = ['brie', 'gjetost', 'havarti']
# for cheese in cheeses:
#     if cheese.startswith('x'):
#         print("i won't eat anything that starts with 'x'")
#         break
#     else:
#         print(cheese)
# else: # for가 break없이 끝났을때 실행되도록.
#     print("Didn't find anything that started with 'x")

# # 최초의 for가 절대 run 하지않는다면, control은 else로 간다.
#
# cheeses = [] # cheeses가 비어있기 때문에 아래의 for문은 작동x!
# for cheese in cheeses:
#     print("This shop has some lovely", cheese)
#     break
# else:
#     print("This is not much of a cheese shop, is it?")


""" Iterate Multiple Sequences with zip() 
zip()을 이용해서 multiple sequence들을 iterate 할 수 있다.
멈추는 시점 : 가장 짧은 sequence 가 끝날때."""

# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'icecream', 'pie', 'pudding']
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
#     # 여기서는 가장 짧은게 3개로 desserts의 pudding은 절대 출력되지 못한다.

"""또한 Zip을 이용해서 sequence 들로 list를 만들어 볼 수 있다."""

# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'
# print(list(zip(english, french)))
# print(dict(zip(english, french)))  # 조그만 영,프 사전이 완성됐다!


""" Create a List with a Comprehension.
여기서는 list comprehesion과 for/in 등을 활용해 list를 만드는
방법에 대해 알아볼 것이다."""

# # 1에서 5까지의 숫자가 있는 list를 만들어보자.
# list_test = list(range(1,6)) # 가장 간단한 방법인줄 알았는데 아니래! 더 간단한게있대!
# print(list_test)

# # 위의 방식보다, list comprehension 이 가장 pythonic 한 방식이다.
# number_list = [number for number in range(1,6)]
# print(number_list)

# # 이게 앞서 사용했던 방식보다는 쉽지는 않지만 다양한 응용이 가능하기 때문에 유용하다.
# number_list = [number-1 for number in range(1,6)] # 맨앞의 variable은 list에 들어가게 될 값이다.
# print(number_list)

# a_list = [number for number in range(1,6) if number % 2 == 1]
# print(a_list)
#
# # 동일기능을 하는 이전의 것.
# a_list = []
# for number in range(1,6):
#     if number % 2 == 1:
#         a_list.append(number)
#
# print(a_list)

# # 지금까지는 한 set에 대해 해봤지만 이번에는 2개 이상의 set으로 한번 해보자.
# rows = range(1, 4)
# cols = range(1, 3)
# for row in rows:
#     for col in cols:
#         print(row, col) # 굉장히 번거로운 버전이다.
#
# rows = range(1, 4) # 아주 간단하다, 아니 보기 편하다 !
# cols = range(1, 3)
# cells = [(row, col) for row in rows for col in cols]
# for cell in cells:
#     print(cell)
#
# for row, col in cells:  # tuple unpacking을 사용하는 모습.
#     print(row, col)


""" Lists of Lists
list는 얘기햇듯이, 다른 종류의 element등을 포함할 수 있다."""
# small_birds = ['hummingbird', 'finch']
# extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
# carol_birds = [3, 'French hens', 2, 'turtledoves']
# all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
#
# print(all_birds)
# for i in all_birds:
#     print(i)


""" Tuple Versus Lists
대부분의 경우에서 tuple은 list보다 기능도 적고 생성후 수정도 불가능하다.
그런데 왜 tuple을 사용하는 걸까? 다음과 같은 이유가 있다.

1. Tuple은 공간을 덜 차지 한다.
2. Tuple은 실수로 훼손되지 않는다 (수정이 안되기 떄문)
3. Tuple을 dictionary key로 사용할 수 있다.
4. Named tuple은 object의 대체제가 될 수 있다.

하지만 역시 대부분의 경우에서 list나 dictionary 를 쓰게 될 것이다."""


""" There Are No Tuple Comprehensions
Mutable Types (lists, dictionaries, and sets)들은 comprehension이 있다.
하지만 Immutable Types(strings, tuples) 들은 그들의 section 안에있는 method
를 통해 생성되어야 한다.
 이때 단순히, list의 square brackets 를 수정해서 사용하면 된다고 생각할 수도 있다.
 ex)number = (number for number in range(1,6)) 과 같이.
 하지만 이는 실제로는 type을 해보면 generator 이며 tuple이 아님을 알 수 있다.
 generator 에 대한 이야기는 추후에 더 다룰 것이다."""

# number = (number for number in range(1,6))
# print('type of number: ', type(number))

# finished at 11/03 5:40 pm


"""Things to Do
다양한 종류의 실세계의 요소들을 lists, tuples, numbers, strings 등으로 나타낼 것이다."""