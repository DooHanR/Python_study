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


"""0개 에서부터 그 이상까지의 elements로 구성되며,
',' 와 '[, ]'로 구성된다."""
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
first_names = ['Grahm', 'John', 'Terry', 'Terry', 'Michael'] # values
leap_years = [2000, 2004, 2008]

print(first_names)


