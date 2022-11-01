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

# marx_tuple = ('Groucho', 'Chico', 'Harpo')
# 괄호 없이도 튜플 정의 가능. but 가시성 측면에서 괄호를 사용하는게 더 좋다.
# print(marx_tuple)
# print(type(marx_tuple))


""" 괄호를 사용하지 않았을 경우, single element tuple은
 function의 argument로 pass불가 """

# one_marx = ('Groucho',)
# one_marx = 'Groucho',
# print(type(one_marx))
# print(one_marx)
# print(type('Groucho'))


"""Tuple의 기능.
한번에 여러개의 변수를 지정할 수 있게 한다."""

# marx_tuple = ('Grucho', 'Chico', 'Harpo')
# a, b, c = marx_tuple
# print(a, b, c)
# print(a)
# print(b)
# print(c)

# 위의 것을 tuple unpacking 이라고도 불린다.


"""tuple을 이용해 temporary variable을 사용하지 않고 values를 바꿀 수 있다."""

# password = 'swordfish'
# icecream = 'tuttifrutti'
# password, icecream = icecream, password
# print(password)
# print(icecream)


"""tuple() 함수를 이용해 다른 타입의 것들로 tuple을 만들 수 있다."""

# marx_list = ['Groucho', 'Chico', 'Harop']
# print(type(marx_list))
# print(tuple(marx_list))
# print(type(tuple(marx_list)))


""" +를 이용해서 tuple combine 하기."""

# print(('Groucho', ) + ('Chico', 'Harpo'))

# 여타 다른곳에서 쓰는거랑 똑같은 거 같다.


"""Compare Tuple. list comparison 과 흡사하게 작동된다."""

# a = (7, 2)
# b = (7, 2, 9)
# print(type(a), type(b))
# print(a == b)
# print(a <= b)
# print(a < b)

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
# print(t1 + t2)
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


"""Create or Conver with list()
list() function을 통해 empty list를 만들 수 있다.
혹은 다른 iterable data type 등을 list로 변경 할 수 있다."""

# another_empty_list = list()
# print(another_empty_list)

# print(list('cat'))
# a_tuple = ('ready', 'fire', 'aim')
# print(list(a_tuple)) # ()가 []로 바뀌는 차이정도?


"""Create From a string with split()"""

# split()을 이용, separator를 기준으로 string을 나눌 수 있다.
# talk_like_a_pirate_day = '9/19/2019'
# print(talk_like_a_pirate_day.split('/'))

# 만약에 separtor 가 원본 string에 여러개가 있다면?
# splitme = 'a/b/c//c/d///e'
# print(splitme.split('/'))
# print(splitme.split('//'))


"""Get an item by [ offset ]"""

# string에서 했던것처럼 list 에서도 offset을 이용, single value를 추출 할 수 있다.
# marxes = ['Groucho', 'Chico', 'Harpo']
# for i in range(0,3):
#     print(marxes[i])

# for i in range(2,-1,-1):
#     print(marxes[i])


"""Get items with a Slice"""

# list에서도 마찬가지로 slice를 통해 추출해낼 수 있다.
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
# marxes.append('Zeppo')
# print(marxes)

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


"""Combine Lists by Using extend() or +
extend()를 사용해서 list끼리 merge할 수 있다.
다음을 한번 살펴보자."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# others = ['Gummo', 'Karl']
# marxes.extend(others)
# print(marxes)

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
# marxes[2] = 'Wanda'
# print(marxes)

# List는 위와 같은 방식으로 변경이 가능하지만
# String은 immutable 이기 때문에 안된다는 점에 유의하라.


"""Change Items with a Slice
앞서서는 slice를 통해 sublist를 얻는 방법에 대해 알아봤다.
하지만 여기서는 slice를 이용해 sublist에 value를 assign하는
방식에 대해 알아볼 것이다."""

# numbers = [1, 2, 3, 4]
# numbers[1:3] = [8, 9]
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers[1:3] = [7, 8, 9] # 범위가 정확하지 않아도 해당 내용을 모두 삽입한다.
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers[1:3] = []
# print(numbers)


""" Slice를 통해서 item을 바꿀때, 이 경우에는 숫자를 예시로 들었지만
righthand 쪽이 반드시 같이 숫자일 필요는 없다."""

# numbers = [1, 2, 3, 4]
# numbers[1:3] = 'wat?' # 이 경우 해당 범위내에 'wat?' 를 삽입하게 된다.
# print(numbers)


""" Delete an item by Offset with del 
del을 이용해 offset에 있는 특정 item 삭제하기."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
# print(marxes[-1])
# del marxes[-1]
# print(marxes)

# marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
# del marxes[1]
# print(marxes)

"""이때 del 명령어가 string에 포함되어있는게 아닌
python의 자체적인 명령이기 때문에 string.del 과 같은 사용에 주의하라."""


"""Delete an item by Value with remove()
만약 어디있는지도 모르겠고 뭘 삭제하건간에 별 관심이 없다면
string의 string.remove() function을 사용하라."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# marxes.remove('Groucho')
# print(marxes)

# 만약 duplicate 해서 동일한게 여러개가 있다면
# 발견 되는 최초의 것을 remove 함수가 제거한다.


"""Get an Item by Offset and Delete it with pop()
pop()를 이용해서, list에서 item을 얻는것과 동시에 list 에서 제거할 수 있다."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
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

"""Find an Item's Offset by Value with Index()
value를 통해 list 내의 offset을 알고싶다면, index()를 사용하라!."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# print(marxes)
# print(marxes.index('Groucho'))
# print(marxes.index('Zeppo'))
#
# simpsons = ['Lisa', 'Bart', 'Marge', 'Bart']
# print(simpsons.index('Bart')) # 여러개가 있는경우는 최초의 것의 index만 출력.


"""Test for a Value with in
해당 list내에 해당 value가 있는지 pythonic 한 방식으로 
확인하는 방법이다."""

# marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
# print('Groucho' in marxes)
# print('Bob' in marxes)


""" Count Occurrences of a Value with count()
list에 특정 value 가 얼마나 occur 하는지 확인하고 싶다면
count()함수를 이용해라."""

# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes.count('Harpo'))
# print(marxes.count('Bob'))
#
# snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
# print(snl_skit.count('cheeseburger'))

example.





