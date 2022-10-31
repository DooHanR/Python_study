""" 여기서는 Tuple과 List에 대해 공부할 것.
근데 Tuple은 도대체 뭐지?

대부분의 프로그래밍이 조합하고 분해하는 과정이라면
여기서 나오는 Tuple과 List는 톱이나 글루건이 될 것.
그리고 또한 list와 tuple은 기존의 것들이 원자라면
원자의 조합인 분자라고 볼 수 있다.

List와 Tuple의 차이점은 변경 가능 여부이다.
 'Tuple의 경우 immutable이지만 List의 경우 변경이 가능하다."""


"""Tuples. Create with Commas and ()
Tuple의 특징이라면 '()' 로 이 동그라미 괄호로 형성된다."""

empty_tuple = ()
print(empty_tuple)

test = 'abcd'
one_marx = 'Groucho', # 단순 string과 tuple의 차이점에 주의하자.
one_marx = ('Groucho', )
print(test)
print(one_marx)
print(type(test))
print(type(one_marx))

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
print(type(marx_tuple))

one_marx = 'Groucho',
print(type(one_marx))
print(one_marx)
print(type('Groucho'))

'''Tuple의 기능.
한번에 여러개의 변수를 지정할 수 있게 한다.'''

marx_tuple = ('Grucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a, b, c)

print("abc")

print("왜 안되는거야")
