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
# 'is' operator 를 사용한 모습이다.

# thing = None
# if thing is None:
#     print("It's Nothing")
# else:
#     print("It's Something")


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

# 매우 흔하지만, positional argument의 단점은 위치를 기억해줘야 한다는 것이다.
# 그렇지 않으면 의도된 바와 다르게, 의미가 매우 달라질 것이다. 다음 예시를 보라'

# def menu(wine, entree, dessert):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}
#
# print(menu('chardonay', 'chicken', 'cake', ))
# print(menu('beaf', 'bagel', 'bordeaux'))  # 와인이 beef가 됐다!


""" Keyword Arguments
keyword Arguemnts 는 앞서말한 positional argument 의 혼란은 피하기 위해,
argument에 상응되는 parameter 를 명시해서, 순서가 달라도 제대로 출력되게
하는 것이다. 다음 예시를 보자. """

# 순서는 다를지 언정 제대로 매칭시켜줬기 때문에 정상 출력될 것이다.
# 함수 자체에는 별 차이가 없다, 하지만 call 하는 과정에서 차이가 생기는 것.
# print(menu(entree='beef', dessert='bagel', wine='bordeaux'))


""" Specify Default Parameter Values
parameter 에 default value를 구체화 할 수 있다.
이 경우 argument를 명시하지 않아도 기본값이 그대로 출력되게 된다.
특히 매우 유용한 기능이다. """


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert, }


# default value 가 있어서 정상출력 되는 모습이다.
# print(menu('chardonnay', 'chicken'))

# argument를 넣으면 기존의 default value가 대체된다.
# print(menu('chardonnay', 'chicken', 'coffee'))


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
single tuple of parameter values로 바꿔준다.
혹은 함수외부에서 사용시 explode 의 기능을 보인다."""


def print_args(*args):
    print('Positional Tuples:', args)

# print_args('beyond', 'compare')
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
# print_more('not')  # args를 제외한 positional argument보다 적은 수의 argument를 넣었을 때.

""" 또한 *args는 function의 inside냐 outside냐에 따라 그 기능도 달라진다.
inside의 경우 values들을 gather 하는 기능을하고
outside 에서는 valuse들을 explode 시킨다. """

""" 또한 *args는 다음과 같은 2가지의 경우에만 사용가능 하다는것에 주의해라. 
1. function call
2. function definition. """
# *args를 통해 explode 시키는 모습

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


# 내부의 선언이 보다 간단해졌고, dict 의 형태로 return 됨을 알 수 있다.
# print(print_kwargs())
# print(print_kwargs(wine='merlot', entree='mutton', dessert='macaroon'))

""" Argument의 order는 다음과 같다.
1. Required Positional arguments: 함수 선언시 명시한 것들
2. Optional Positional arguments: (*args)
3. Optional keyword arguments: (**kwargs) """

# 마찬가지로 kwargs도 explode, gather 하는 기능을 한다!


""" Keyword-Only Arguments
무슨소린지 모르겠다, 예시를 통해좀 알아보자."""


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


""" 여기서 *가 의미하는것은 다음의 start와 end 는 그들의 default 값이
쓰고싶은게 아니라면 named arguments로 제공되어야 한다는것을 의미한다. 
다음의 예시를 통해 한번 같이 살펴보자."""

data = ['a', 'b', 'c', 'd', 'e', 'f']
# print_data(data)
# print_data(data, start=4)
# print_data(data, start=1)
# print_data(data, end=2)

# data는 반드시 들어가지만 * 다음의 두 변수들은 들어가기도, 생략되기도 한다.


""" Mutable and Immutable Arguments
list는 할당후에도 변경이 가능했지만, integer나 string은
할당후에는 변경이 불가능하다. 이들이 Mutable, Immutable 의 특징을 갖고 있기 때문이다.
이는 function에 argument를 passing 할때도 마찬가지다.

만약 argument가 mutable 이라면, value는 function 내부에서 상응하는 parameter
를 통해서 변경될 수 있다. 다음의 예시를 참고해보자."""

outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible!'


# 이렇게 하지 않는게 바람직하다. 변경이 마구잡이로 일어나기 때문.
# print(outside)
# mangle(outside)
# print(outside)


""" Docstrings
function body의 시작 부분에 string을 넣어 함수에 대한 document를
추가 해줄 수 있다. 또한, 매우 길게 설정할 수도 있으며(세개의 따옴표를 이용)
python의 help 함수를 통해 이러한 docstrings를 불러올 수 있다.
다음 예시를 보자."""


def echo(anything):
    'echo return its input argument'
    return anything


# print(echo('get out!'))
# print(help(echo))  # help 명령어를 통해 함수에대한 docstring을 출력할 수 있다.
# print(echo.__doc__)  # formatting 없이 docstring 출력하는 방법

""" __doc__ 는 docstring의 python internal variable이다.
이러한 double underscore('__')는 많은 python 내부 변수로 사용되므로
잘 알아두도록 하자. """


""" Functions Are First-Class Citiznes
python 에서는 심지어 함수조차도 object로 취급된다.
이점을 이용해서 변수를 할당하거나, 다른 함수의 argument로 사용하거나
return 조차 할 수 있기 때문에 여타 다른 언어에서 할 수 없었던,
혹은 어려웠던 것들도 python 에서는 해낼 수 있다. 
한번 다음을 통해 실험해보자. """


def answer():
    print(42)


# print(answer())는 answer()이 return 하는게 없기 때문에 none이 출력됨.
# print(answer())
# answer()

# 함수의 매개변수로 함수를 받는 함수.
def run_something(func):
    func()


# run_something(answer)
# print(type(run_something))
""" 이때 parentheses(괄호) 가 없는것에 주의하라. 괄호는 이 function을 호출
하겟다는 것을 의미하는것이며, 괄호가 없다면 함수는 object 처럼 다루어진다.
그래서 저렇게 호출이 가능해지는 것이다."""


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


# 여기에 *args 와 **kwargs 를 결합하는 것도 가능하다.
# run_something_with_args(add_args, 1, 2)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


# print(run_with_positional_args(sum_args, 1, 2, 3, 4, 5))
""" function 은 마찬가지로 list, tuple, set, dictionary 등의 element로
사용 할 수 있으며, 또한 immutable 요소 이기 때문에 dictionary의 key로도 
사용이 가능하다."""


""" Inner Functions.
function 내부에 function 을 정의 할 수 있다."""


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


# print(outer(4, 7))

"""Inner function은 다른 function과 함께 복잡한 task를 처리할때 특히 유용하다.
Inner function을통해 loop나, code duplication 을 방지 할 수 있다.
다음의 예시를 한번 보자. """


def knights(saying):
    def inner(quote):
        return f"We are the Knights who say: {quote}"  # fstring.
    return inner(saying)


# print(knights('Yo!'))


""" Closures 
내부의 function은 closure 로 작동될 수 있다.
closure function은 다른 function에 의해 동적으로 생성된 function 으로
외부에서 생성된 변수의 value를 변경하거나, 혹은 저장할 수 있다."""

"""다음의 예시를 한번 살펴보자. 여기서 몇가지 차이점이 있다.
1. inner2()는 외부의 saying parameter를 인자로 받지않고 바로 사용한다
2. knights2()는 이전과 다르게 function call을 return 하는게 아니라
함수 자체의 이름을 리턴한다."""


def knights2(saying):
    def inner2():
        return f"We are the knights who say: {saying}"
    return inner2


""" 내부의 inner2() function은 saying value가 passed 됐음을 알고있고, 이를
기억한다. 그 이후 return inner2 라인에서는 inner2 function의 specialized copy
를 return 한다.
 이를 어디서 왔는지를 기억하는 동적으로 생성된 closure 라고 한다."""

# a = knights2('Duck')
# b = knights2('Hasenpfeffer')

# print('a:', type(a), 'b:', type(b))  # 함수가 리턴되기 때문에 a, b는 함수가된다.

# 함수가 리턴 됐기 때문에 함수 호출이 된다
# print(a())
# print(b())


""" Anonymous Functions:lambda 
python 에서 lambda function은 single statement로 나타낼 수 있는
이름이 없는 function 이다. 자세한건 다음의 예시를 통해 알아보자. """


# 일반적으로 구성했을 경우.
def edit_story(words, func):
    for word in words:
        print(func(word))


def enliven(word):
    return word.capitalize() + '!'


stairs = ['thud', 'meow', 'thud', 'hiss']
# edit_story(stairs, enliven)


# lambda 를 사용했을 경우. enliven 이라는 함수가 lambda 식으로 대체됨.
# edit_story(stairs, lambda word: word.capitalize() + '!')

""" lambda 식보다는 함수명을 사용하는게 더 나을수는 있지만 
lambda가 유용한 경우는, 크기가 작은 여러개의 function을 정의하고
그 이름을 기억해야 할때 그냥 한줄로 퉁칠 수 있기 때문에 
그런 면에서는 더욱 간단하다. """


""" Generators
generator는 python 의 sequence creation object이다.
generator를 통해 매우 큰 연속체를 이용할 수 있는데, 굳이
메모리에 생성하고 저장할 필요 없이 즉석에서 사용 할 수 있다.
ex)range(1,101) -> 다른 언어처럼 크기 100짜리를 만들 필요없이
즉석에서 가볍게 만들고 제거됨."""

# print(sum(range(1, 101)))


""" Generator Functions
generator function은 크기가 큰 연속체를 만들고 싶을때 사용한다.
얼핏보면 normal function 과 유사하지만, value 를 return 할 때
'yield' statement를 사용한다. return a말고. """


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


# print(my_range) # normal function 이긴 하다.
ranger = my_range(1,10)
# print(ranger) # 리턴 되는것은 generator object이다.

""" 이때 generator 는 일회용이다. 메모리에 저장되지 않기 때문이다
따라서 만약에 ranger를 두번 사용하려 하면 출력이 되지 않는걸 볼 수가 있다."""

# print(list(ranger))  # 한번쓰면 사라져서 ranger 두번 사용 불가.
for x in ranger:
    print(x)


""" Generator Comprehensions
기존의 list, comprehension, set과 같이 유사하게 사용되지만
둘러 싸고있는게 ()로, []나 {}이 아니다. 다음의 예시를 보자."""

# 이 경우는 yield가 invisibly 됐다, generator object를 return 하는 경우이다.
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)

for thing in genobj:
    print(thing)


""" Decorators 
decorator는 한 function을 input으로 받아서 다른 function 으로 return 하는 기능을 한다.
보통 존재하는 function을 소스 코드의 변경없이 수정하고자 할때 사용하는 듯 하다. """

""" 다음 세가지를 이용할 것이다.
1. *args, **kwargs
2. Inner functions
3. Fucnitons as arguments"""

"""정의되는 decorator function은 다음의 일들을 할 것이다.
1. function의 name과 argument를 print 할 것이다. 
2. argument 들로 function을 실행시킬 것이다.
3. 결과를 출력
4. modified function을 return 한다. """


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
cooler_add_ints = document_it(add_ints) # manual decorator assignment
cooler_add_ints(3, 5)




















































































