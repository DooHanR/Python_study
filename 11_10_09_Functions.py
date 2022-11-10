# string = 'money'
# print(f'the {string} is not yours')  # fstring!

""" Chapter 9, Functions
앞서 했던것처럼, 짧은 코드를 통해 여러 기능을 구현할 수 있지만
항상 이것을 retype 할 수 없는게 현실이다.
그래서 우리는 이것을 조정가능하게 블록화 하기로 했는데,
그게 바로 function(함수)가 되시겠다.
you can do two things with a function.
1. Define it, with zero or more parameters
2. Call it, and get zero or more results """

""" Define a Function with def
python function을 정의하기 위해서는
def 를 입력, 이름, parentheses enclosing any input parameter
그리고 colon(:) 등을 입력후 행동을 이어 입력하면 된다.
이때 이름은 변수 이름을 짓는 방식과 같다. """

# def do_nothing():
#     print("Hello world!")
# parameter 가 없어도 괄호는 반드시 있어야 한다.
# pass 의 경우, function이 아무 기능도 하지 않음을 보여주는 것.


# do_nothing()


""" Call a Function with Parentheses
함수명(매개변수)의 형태로 함수를 호출 할 수 있다.
ex)do_nothing() """

# def make_a_sound():
#     print('quack')
# make_a_sound()


# def agree():
#     return False


# if agree():
# print('Splendid!')
# else:
#     print('That was unexpected..')


""" Arguments and Parameters
이제는 함수의 괄호 사이에 parameter를 넣어보자. """

# def echo(anything):
#     return anything + ' ' + anything
#
#
# print(echo('hello'))
# 위의 코드처럼 외부에서 arguments를 넣으면
# 내부에 상응하는 parameter에 이값이 복사되어 function이 작동된다.


# def commentary(color):
#     if color == 'red':
#         return "It's a tomato."
#     elif color == 'green':
#         return "It's a green pepper"
#     elif color == 'bee purple':
#         return "i don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color " + color + "."
#
#
# exam_color = commentary("123")
# print(exam_color)


""" None Is Useful
None은 python의 특별한 value로 아무것도 없음을 나타낼때 쓰인다.
이는 종종 false 처럼 취급을 받기는 하지만, false 와는 다르다라는 것을
명심해야한다. """

# 마치 None 을 false 취급하는 예시.
# thing = None
# if thing:
#     print("It's some thing")
# else:
#     print("It's no thing")

# 반면에 이 예시에서는 None이 false 취급이 아니다.
# thing = None
# if thing is None:
#     print("It's Nothing")
# else:
#     print("It's Something")
# 'is' operator 를 사용한 모습이다.

""" None이 필요한 이유는, empty value와 missing value를 구분하기 위함이다.
분명 입력이 잘못됐을수는 있지만, 이는 없는것과는 다르기 때문이다."""

# argument가 True, False, None 인지 구별하는 함수.


# def whatis(thing):
#     if thing is None:
#         print(thing, "is None")
#     elif thing:
#         print(thing, "is True")
#     else:
#         print(thing, "is False")
#
#
# whatis(None)
# whatis(0)
# whatis(1)
# whatis(True)
# whatis(False)
# whatis('')
# whatis([' '])

# None을 제외한 뭘 넣든간에 조건에 맞는 입력이 아니면 false 가 출력된다.


""" Positional Arguments
python은 function argument를 여타 언어와 다르게 매우 융통성있게 취급한다.
특히 그중에서도 우리에게 익숙한 것은 positional arguments 인데,
이것은 value가 대응되는 parameter 에 순서대로 들어가는 것이다.
예시를 통해 알아보자 """

# def menu(wine, entree, dessert):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}


# print(menu('chardonay', 'chicken', 'cake', ))
#
# # 매우 흔하지만, positional argument의 단점은 위치를 기억해줘야 한다는 것이다.
# # 그렇지 않으면 의도된 바와 다르게, 의미가 매우 달라질 것이다. 다음 예시를 보라
#
# print(menu('beaf', 'bagel', 'bordeaux'))  # 와인이 beef가 됐다!


""" Keyword Arguments
keyword Arguemnts 는 앞서말한 positional argument 의 혼란은 피하기 위해,
argument에 상응되는 parameter 를 명시해서, 순서가 달라도 제대로 출력되게
하는 것이다. 다음 예시를 보자. """

# print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
# 순서는 다를지 언정 제대로 매칭시켜줬기 때문에 정상 출력될 것이다.


""" Specify Default Parameter Values
parameter 에 default value를 구체화 할 수 있다.
이 경우 argument를 명시하지 않아도 기본값이 그대로 출력되게 된다.
특히 매우 유용한 기능이다. """


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert, }


# print(menu('chardonnay', 'chicken'))
# default value 가 있어서 정상출력 되는 모습이다.

# print(menu('chardonnay', 'chicken', 'coffee'))
# argument를 넣으면 기존의 default value가 대체된다.

"""default 변수는 immutable variable로 설정해야 하며,
초보 python programmer가 종종 list나 dictionary와 같이
변경가능한 변수들로 설정하곤 한다. 이에 주의해라!"""


""" 뜬금없지만 python job interview 질문.
어느 함수가, 매번 실행될때마다 비어있는 list를 통해
입력받은 argument를 입력받는다고 했을때, 2번째 실행때
이전에 실행한 값이 함께 나오는 경우 어떻게 고쳐야 할까? """


def works(arg):  # 이곳에서 result를 선언하면 안된다.
    result = [arg]  # 이게 없어지면 result에 점점 쌓이게 된다.
    return result


# print(works('a'))
# print(works('b'))


""" Explode/Gather Positional Arguments with *(asterisk)
c, c++ 에서와 다르게 파이썬에서의 *는 기능이 다르다.
파이썬에서 *는 여러개의 positional arguments를
single tuple of parameter values로 바꿔준다. """


def print_args(*args):
    print('Positional Tuples:', args)


# print_args(1, 2, 3, 'wait', 'hello', 'Doo')  # 놀랍게도 모두 출력된다!

""" 이처럼 *는 매우 유용한데, function이 positional arguments를
필요로 할때 필요로 하는것을 먼저 넣고 마지막에 *를 사용하면 필요한것 보다
많은 것들도 넣어줄 수 있다. 이떄 tuple의 형태가 된다는것에 주의."""


# 반드시 *args 라고 할 필요는 없지만 관습적으로 args 라고 한다.
# def print_more(required1, required2, *args):
# def print_more(required1, required2, *abcd):
#     print('Need this one', required1)
#     print('Need this one too', required2)
#     print('All the rest', args)
#     print('All the rest', abcd)

# print_more('essential', 'essential', 1, 2, 3, 'ahrararara')

""" 또한 *args는 function의 inside냐 outside냐에 따라 그 기능도 달라진다.
inside의 경우 values들을 gather 하는 기능을하고
outside 에서는 valuse들을 explode 시킨다. """

# *args를 통해 explode 시키는 모습

""" 또한 *args는 다음과 같은 2가지의 경우에만 사용가능 하다는것에 주의해라. 
1. function call
2. function definition. """
# print_args(2, 5, 7, 'x')
# args = (2, 5, 7, 'x')
# print_args(args)
# print_args(*args)


""" Explode/Gather Keyword Arguments with **
'**'는 keyword arguments를 dictionary로 group 하는 기능을 한다.
argument의 name은 key가 되고 상응하는 것들이 value가 되는것이다.
기존의 형식을 잘 생각해보면 이해가 될 것이다. 예시를 보자 """


# function 내부에서 kwargs 는 dictionary parameter이다.
def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)


print(print_kwargs())
print(print_kwargs(wine='merlot', entree='mutton', dessert='macaroon'))

""" Argument의 order는 다음과 같다.
1. Required Positional arguments: 함수 선언시 명시한 것들
2. Optional Positional arguments: (*args)
3. Optional keyword arguments: (**kwargs) """

# 마찬가지로 kwargs도 explode, gather 하는 기능을 한다!


""" Keyword-Only Arguments
"""



