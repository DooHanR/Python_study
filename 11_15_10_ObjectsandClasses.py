""" 먼저 Object 에 대해 배우게 될 것이다.
지금까지 배운 거의 모든것들, 그러니까 대부분이 object 이다.
object의 내부를 봐야할때는 다음과 같다.
1. 존재하는 object의 behavior을 수정하거나
2. 스스로 만들고 싶을때.
여기서는 그 두가지 방법에 대해 배울것이다."""


""" What Are Objects?
object(custom data structure) = data(variable, attributes) + code(functions, methods)
object = 명사, method = 동사라고 여겨라. object 는 각각의 것들을 나타내고
그것의 method는 어떻게 다른것들과 상호작용 하는지를 나타낸다.
 단적으로 string도 object 인데, string.capitalize()와 같이 method가 
있다는 것을 알 수 있을 것이다.
 또한 모듈과 다르게 여러개의 object를 동시에 소유할 수 있다."""


"""Simple objects.
먼저 간단한 것들 부터 시작해보자. 먼저 우리는 상속에 대해 이야기 해볼 것이다."""


"""Define a Class with class
class는 마치 box를 만들어내는 형판과도 같아서 이를 통해 object를 만들어낸다.
따라서 만약에 자신만의 custom object가 갖고싶다면 먼저 class를 정의해야 한다.
'class' keyword를 사용하며 다음의 예시를 통해 직접 알아보자"""

class Dog():  # == class Cat:
    pass  # class가 비어있다는 뜻, object 를 만들기 위한 최소한의 정의.

a_dog = Dog()  # function 쓰던것처럼 class로 object 생성하기.
another_dog = Dog()

# 하지만 여기서 dog class 는 코드가 없기때문에
# 생성된 object 들의 기능은 아무것도 하지 못한다!


""" Attributes
attribute 는 object, class 내부의 변수를 의미한다.
object, class 를 생성하는 도중 혹은 생성후에도 만들어질 수 있으며,
다른 object 일수도 있다. 다음의 예시를 한번 살펴보자."""

class Dog():
    pass

a_dog = Dog()
# print(a_dog)
another_dog = Dog()
# print(another_dog)

""" dog class 에서 object 가 어떻게 행동하라고
명시하지 않았기 때문에 아무것도 출력되지 않는 모습이다. """

# attribute 할당하기.
a_dog.age = 10
a_dog.name = "Danchu"
a_dog.nemesis = another_dog

another_dog.name = "Flowerbutton"

# print(f"dog age: {a_dog.age},"
#       f" dog name: {a_dog.name},"
#       f" dog nemesis: {a_dog.nemesis.name}")

""" 보통 attribute라 하면 object의 attribut이다.
하지만 class 의 attribute도 있으므로 이에 주의하라.
어찌보면 구조체를 쓰는것과 비슷한 부분이다."""


""" Methods
Method는 class나 object 내부의 function을 의미한다.
마찬가지로 다양하게 사용 될 수 있으며 뒤에서 더 자세히 다뤄볼 것이다."""

"""Initialization(초기화)
만약 생성시에 object attributes를 부여하고 싶다면
python의 object 초기화 method 인 '__init__()' 를 사용해야 한다. """

# 선언과 동시에 attribute 할당하기.
class Dog:
    def __init__(self):  # init의 parameter 로 반드시 self가 있어야 한다.
        pass

class Dog:
    def __init__(self, name):
        self.name = name

a_dog = Dog('doggy')
# print('a_dog\'s name:', a_dog.name)

""" 위의 한줄이 하는 일은 다음과 같다.
1. Dog class 의 definition 을 찾는다.
2. memory 에 새로운 object 를 생성한다.
3. object의 init method를 호출한다. 이때 인자로 self와 name을 넘겨준다.
4. 넘겨받은 name을 object의 name에 저장 한다.
5. 생성된 object를 return 한다.
6. object에 a_dog 라는 변수를 붙여준다. """

# print('Our latest addition:', a_dog.name)

""" '__init__()' method가 반드시 모든 class definition 에 필요한 것은 아니다.
이것은 같은 class 에서 생성된 다른것들과 해당 object를 비교하기 위한 것이다.
그리고 init() 함수는 여타 다른 언어의 생성자와는 엄연히 다르며,
init() method는 initializer로 생각하라.

- class의 유일성 : class 로 많은 object를 생성할 수는 있지만, 해당 class는 프로그램에
오직 하나뿐이라는 것을 기억해라. """


""" Inheritance(상속)
가끔 문제를 해결하다보면, 문제를 풀기에 기존의 코드가 매우 적합한데
함부로 수정하자니 너무 복잡해지고, 새로 만들자니 시간과 공간의 낭비다.
그래서 이에 대한 해답으로 나온것이 상속이다.
 상속은 기존의 클래스를 이용해, 약간의 수정을 거치거나 추가해서 새로운
클래스를 만드는 것을 의미하며, 코드를 재사용하기에 매우 좋다."""

""" Inherit from a Parent Class
상속할때 오직 추가하거나, 변경할 것만 추가해주면 나머지는 모두 부모 클래스에서
물려 받게 된다. 한번 실습을 통해 알아보자."""

class Car():
    pass

class Yugo(Car):  # 정말 상속하기 편하다. python 은 신이야.
    pass

# 상속관계인지 여부를 확인하는 방법.
# print(issubclass(Yugo, Car))


# 각각의 클래스로 object 생성하기.
give_me_a_car = Car()
give_me_a_Yugo = Yugo()

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_Yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_Yugo.exclaim()

""" 상속은 보기에 매우 편해보일지는 모르겠지만, 다년간의 객체 지향 프로그래밍 경험에서 나온
결론은 너무 잦은 상속의 사용은 프로그램을 유지보수 하기 힘들어진다는 것이다.
 따라서 우리는 다른 방식을 추천하는데, 다음의 2가지이다.
aggregation, composition 이다. 이 챕터에서 이 대체제 들을 공부 해볼것이다. """


"""Override a Method
앞서 말했듯이 기존의 클래스를 상속한 새로운 클래스는 모든것을 상속받는다.
그럼 이때, 부모의 것을 대체할 때를 알아보자."""

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo, Much like a Car, but more Yugo-ish")
# 여기서 exclaim method를 override 하였다. init도 override 가능하다!

this_is_Car = Car()
this_is_Yugo = Yugo()
# this_is_Car.exclaim()
# this_is_Yugo.exclaim()
# 동일한 method가 override 된 모습.

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)


""" Add a Method
자식 클래스는 또한 부모 클래스에 없는 method를 추가할 수 있다.
다음의 예시를 한번 보자."""

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo, very yugo-ish")
    def need_a_push(self):  # 새로운 method의 추가.
        print("A little help here?")

this_is_a_Car = Car()
this_is_a_Yugo = Yugo()

# this_is_a_Car.exclaim()
# this_is_a_Yugo.exclaim()
# this_is_a_Yugo.need_a_push()  # 새롭게 추가된 Method 이다. 당연히 부모는 사용불가.


""" Get Help from Your Parent with super()
만약에 자식에서 부모의 method를 호출하고 싶으면 어떻게 해야할까 ?
그럴때는 super() 를 사용하면 된다. 다음 예시를 한번 보자."""

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):  # 상위 클래스 -> person
    def __init__(self, name, email):
        super().__init__(name)
        # super().__init__ 에서 self argument를 pass.
        # 따라서 optional argument 만 추가하면됨.
        self.email = email

class VirtualPerson(Person):  # 상위 클래스 -> person
    def __init__(self, name, platform):
        super().__init__(name)
        self.platform = platform

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
# print(f"his name: {bob.name}, his mail: {bob.email}")

# Question. 왜 번거롭게 super를 이용할까? 아래처럼은 안되는 것일까?

# class EmailPerson(Person):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

""" 답변: 상속성을 유지하기 위함이면서도, 만약에 추후에 상위 클래스의
method가 변경되었을때, 자연스럽게 자식클래스도 해당 변경점이 반영 될 수 있도록
하기 위함이다.
 super()는 자식 클래스가 직접 무언가를 하려고 하지만, 부모의 것이 필요하다면
사용해봐라."""


"""Multiple Inheritance
object의 경우 여러개의 부모 클래스로부터 상속받을 수 있다.
각각의 python class 에는 mro()라는 method와 __mroo__ 라는 attribute가 있다.

1. mro() method는 특정 class의 object가 지닌 method, attribute를
가지고 있는 class 들의 list를 리턴 한다.
2. __mroo__ attribute 는 그러한 class들을 tuple로 나타낸 것이다.
이때 여러개가 있으면 첫번째 것이 win 하는듯 하다.(상속이되나?)"""

class Animal():
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

""" Mule의 method, attribute를 찾는다면 python 에서는 다음과 같은 순서로 실행된다.
위의 Mule의 경우에는. 
1. object itself(of type Mule)
2. object's class(Mule)
3. class first parent class(Donkey)
4. class second parent class(Horse)
5. grandparent class(Animal)"""

# print(Mule.mro())  # 위에 적힌것과 순서가 정확히 같음을 알 수 있다.
# print(Hinny.mro())

mule = Mule()
hinny = Hinny()
# print(mule.says())  # donkey
# print(hinny.says())  # horse


""" Mixins
class 정의에 extra 부모 클래스를 포함 할 수 있는데, 오직 helper 로써만 기능한다.
이것은 다른 부모 클래스와 method를 전혀 공유하지 않는것을 의미하며, 이렇게 함으로써
method resolution ambiguity 를 피할 수 있다."""

class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = 'eldritch'
# t.dump()


"""In self Defense
python 에 대한 비판중 하나는 instance method에 'self'라는 키워드를
첫번째 argument로 넣어야 한다는 것이다.
 파이썬은 이러한 self argument를 obejct의 올바른 attribute 와
method를 찾는데에 이용한다. 다음 예시를 통해 한번 살펴보자"""

a_car = Car()
# a_car.exclaim()
# Car.exclaim(a_car)  # 이렇게 해도 작동은 된다.

""" 위의 것이 실행됐을때 과정을 봐보자.
1. object a_car에 할당될 Class(Car)를 탐색한다.
2. Car class의 self parameter를 통해 클래스의 method를 object에 넘겨준다."""


""" Attribute Access
python 에서 대부분의 object attribute와 method 들은 public이다.
한번 direct approach를 다른 대체제들과 비교해보자."""

"""Direct Access"""
class Duck:
    def __init__(self, input_name):
        self.name = input_name

fowl = Duck('Daffy')
# print(fowl.name)

fowl.name = 'Daphne'
# print(fowl.name)


""" Getters and Setters
몇몇 언어에서는 object attribute 에 대해 private 속성을 지원하기 때문에
그들에 접근하기 위해서는 getter나 setter 처럼, 간접적으로 접근하고 쓰기 위한것들이 필요하다.

 하지만 python 에서도 이름을 혼란스럽게 지어서 privacy 를 확보한 경우에
getter나 setter를 사용해서 이용이 가능하다.
(가장 좋은 방법은 'properties'를 사용하는것이다, 나중에 이야기 할것)

 이후에 등장하는 예제에서는, Duck class에 hidden_name 이라는 attribute 를 작성했다.
아무나 접근하는걸 원치 않기 때문에, getter와 setter를 정의할 것이다. 자세한것은
예제를 통해 살펴보자."""


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

# 내부 hidden_name을 노출시키지 않고 함수를 통해 우회적으로 표현하는 모습.
# don = Duck('Donald')
# print(don.get_name())
# don.set_name('Doo')
# print(don.get_name())


""" Properties for Attribute Access
하지만 attribute privacy에 관해서 가장 pythonic 한 방식은
바로 'property'를 사용하는 것이다. 두가지 사용 방법이 있는데,
1. name = property(get_name, set_name) 을 가장 마지막 줄에 추가하기."""

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)  # 기존에 단 한줄이 추가됐다.

# 이전의 것들도 여전히 작동은 한다.
# don = Duck('donald')
# print(don.get_name())
# don.hidden_name = 'abc'
# print(don.get_name())


# name 이라는 키워드로 get_name, set_name이 사용되는 것을 볼 수 있다.
# don = Duck('DooHan')
# print(don.name)
# don.name = 'Eol'
# print(don.name)


""" 2번째 방식으로는 decorater를 추가해서 method 의 이름을 대체하는 것이다."""

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter  # method명.setter 의 형식인듯 ex)
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

""" 기존의 name = property(get_name, set_name)과 비슷하지만
선언부의 이름이 모두 name으로 동일하고 @property와 @name.setter가 추가된 점이 다르다."""

# don = Duck('donald')
# print(don.name)
# don.name = 'Ronaldo'
# print(don.name)

""" Properties for Computed Values 
앞서 우리는 name property를 object 내의 single attribute를
refer 하는데에 사용했다. 또한 property는 computed value를 return 할 수 있다.
radius attribute 와 ddiameter property가 있는 Circle class를 통해 알아보자."""

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter  # method명.setter 의 형식.
    def diameter(self, radius):
        self.radius = radius

c = Circle(5)
# print(c.radius)
# print(c.diameter)

# c.radius = 7
# print(c.diameter)  # 자동 계산되는 모습을 볼 수 있다.
# c.diameter = 20
# print(c.radius)
# setter property 설정후 변경 가능한 모습.

"""
 direct attribute access 보다 property 사용이 더 나은점.
attribute 의 definition을 변경한다면, 오직 class definition 내부에 있는
코드만 바꾸면 된다. 모든 caller 들이 아니라.
"""


"""
Name Mangling  for Privacy
(Mangling=변수, 함수의 이름을 짓이겨서 다르게 바꿔버리는것)
class definition 외부에서 attribute가 노출되지 않도록 하는
명명 규칙으로, (__) 으로 사용한다.
"""

# 기존의 함수명 hidden_name 을 __name 으로 한번 바꿔보자.

class Duck():
    def __init__(self, input_name):
        self.__name = input_name  # self.name -> self.__name
    @property
    def name(self):
        print('inside the getter')
        return self.__name  # 바뀐부분
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name  # self.name -> self.__name


# fowl = Duck('Howard')
# print(fowl.name)  # property 를 통한 접근. 따라서 접근가능.
#
# fowl.name = 'Donald'  # setter 호출.
# print(fowl.name)

# print(fowl.__name)
# 변수명을 이용한 접근에서는 오류가 발생한다. 접근할 수 없게 Mangling 된 것이다.

""" 이와 같은 Mangling 은 우발적으로, 혹은 의도적으로 attribute에 접근하는 것을
방지한다. 하지만 꼭꼭 접근하고 싶다면 다음과 같은 방법이 있다."""

# print(fowl._Duck__name)  # inside the getter 가 출력 안되는것에 주의.


"""
 Class and Object Attributes 
class에 attribute 를 할당할 수 있다. 그리고 할당된 것들은 자식에게 상속된다.
"""

class Fruit():
    color = 'red'

# 변경 전의 동일한 상태.
blueberry = Fruit()
# print(Fruit.color)
# print(blueberry.color)

# 자식의 것을 바꿔도 class attribute 에 영향을 주진 않는다.
blueberry.color = 'Blue'
# print(f'Fruit :{Fruit.color}, blueberry :{blueberry.color}')

# class 의 것을 바꿔도, 존재하는 자식 오브젝트의 것을 바꾸진 않는다.
Fruit.color = 'Green'
# print(f'Fruit :{Fruit.color}, blueberry: {blueberry.color}')

# 하지만 새롭게 생성되는 오브젝트 의 것에는 반영된다.
Watermelon = Fruit()
# print(f'Fruit: {Fruit.color}, watermelon: {Watermelon.color}')


"""
Method Types
몇몇 method는 class의 일부이기도 하고, 몇몇은 class 내부의 object의 일부이기도하고
어떤것들은 둘다 아니기도 하다.

 1. instance method: 선행하는 decorator 가 없는경우.
첫번째 argument는 반드시 invidual object itself 를 refer 하는 'self' 이여야 함..

 2. class method: 선행하는 '@classmethod' 가 있는 경우.
첫번째 argument는 class 자체를 refer하는 cls(class 말고)이여야 한다.

 3. static method: 선행하는 '@staticmethod' decorator 가 있는 경우.
첫번째 argument는 object나 class가 아니다.
"""

"""
Instance Methods
- Instance Methods : class 정의 할때, 첫번째 argument로 self 가 들어가는 method.
대부분의 직접 만든 class 에서 자주 보게 될 것이다. 그리고 지금까지 본 대부분의
method 등이 Instacne Method 이다. 
"""

"""
Class Methods
- Class Method : class definition 단계에서, 
선행하는 @classmethod 가 존재하는 경우, class method 라고 칭한다.
class method는 class 에 완전히 영향을 끼친다, 그 예시로 이를 통해 만들어내는
변경점들은 그 오브젝트 모두에 영향을 끼친다.
 class method 의 parameter는 'cls' 라고 약속되어 있다.
class 는 예약어 이기 떄문에 사용이 불가능 하기 때문!
다음의 예시를 통해 한번 알아보자.
"""

class A():
    count = 0
    def __init__(self):
        A.count += 1  # self.count 대신 A.count를 사용하는 모습.
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):  # class method 에서 매개 변수로 cls가 사용 된다는 것에 주의해라!
        print(f"A has {A.count} little objects")  # A.count == cls.count


test_a = A()
test_a2 = A()
test_a3 = A()

# A.kids()  # class method의 호출.
# test_a.exclaim()


"""
Static Methods
 static method는 object나 class 모두 영향을 끼치지 않으며 편의를 위해 존재한다.
@staticmethod 라는 decorator 선행하며 argument로 self나 cls등도 받지 않는다.
다음의 예시를 통해 한번 살펴보자.
"""

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

# CoyoteWeapon.commercial()
# 해당 method 에 접근하기위해 object 만들 필요없이 바로 접근 가능하다는 점에 주목.


"""
Duck Typing
 python 은 loose implementation of polymorphism(다형성에 대한 느슨한 이행?)이다.
그들의 클래스 와는 무관하게, method의 이름이나 argument에 따라 다른 object여도
같은 operation 을 적용한다.
 다음의 Quote class에 동일한 initializer 를 사용해보자. 이때, 두개의 새로운 function을 넣자.
1. who() : 저장된 'person' string의 value를 return 한다.
2. says() : 저장된 'words' string를 리턴한다. 구체적인 punctuation 과 함께.
"""

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

"""
하위클래스인 QuestionQuote나 Exclamation 에서 init method를 초기화 하지 않았기 때문에,
상위 클래스의 것을 그대로 가져오며 따라서 override 된 method 에서도 self를 그대로 사용 할 수 있다.
"""

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
# print(f"{hunter.who()} says: {hunter.says()}")

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
# print(f"{hunted1.who()} says: {hunted1.says()}")

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
# print(f"{hunted2.who()} says: {hunted2.says()}")

"""
 기존의 객체 지향 프로그래밍과 마찬가지로, says method는 다양한 형태로 작동된다.
하지만 python 에서는 여기서 더 나아가서 해당 method를 가지고 있는 어느 object 라도
실행 할 수 있게 해준다.
"""

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):  # obj를 실행시키는 함수인듯.
    print(f"{obj.who()} says {obj.says()}")

# 모든 object에 적용이 되는 모습이다.
# who_says(hunter)
# who_says(hunted1)
# who_says(hunted2)
# who_says(brook)


"""
Magic Methods
 Magic methods 는 뭘까? 일단 여기서 말하는 Magic method는
두개의 언더바(__)로 시작하고 끝나는 method 들을 지칭한다.
그리고 Magic method를 통해 python 에서 연산자의 작동 방식을 원하는 대로
변경 시킬 수 있다. ex)'=='가 string의 대문자/소문자 구분없이 비교 하도록.
"""

# 두 단어를 비교하는 'Word' class가 있다고 가정해보자. 이때 대소문자는 구별하지 않는다
class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()  # 대소문자 구별하지 않기위해.

first = Word('Ha')
second = Word('hA')
third = Word('eh')

# print(first.equals(second))
# print(first.equals(third))

# 여기서 기존의 equals() method를 특별한 이름인 '__eq__()'로 변경해볼것.
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('Ha')
second = Word('hA')
trhid = Word('No')

# print(first == second)  # 기존의 first.equals(second) 와 다른모습, 연산자가 사용됨.
# print(second == third)
# print(first.__eq__(second))
# print(first.__eq__(third))


""" __eq__ 왜에도 __ne__(!=), __lt__(<), __gt__(>), __le__(<=), __ge__(>=)
혹은 __add__(+), __sub__(-), __mul__(*), __floordiv__(//), __truediv__(/)
__mod__(%), __pow__(**) 등이 있다. 이때 self 가 좌측, other이 우측에 해당한다.
 이외에도 __str__, __repr__ 등이 있다.
1. __str__ 은 object를 어찌 print 할 것인지.
2. __repr__ output으로 variable을 출력 하도록 한다.
"""

# __str__ , __repr__ 사용예시
first = Word('ha')
# print(first)

"""
Aggregation(집합) and Composition(구성)
 때때로 상속이 매력적인 선택지 일수도 있지만, composition 이나
aggregation이 더 나은 선택일 수도 있다.
 Composition은 전체와 부분이 강력한 연관 관계를 가지며, 같은 생명주기를 갖는다.
ex) Car 와 Engine, House와 Room, 오리와 오리의 꼬리.
 Aggreagation 은 전체와 부분이 연관 관계를 맺기는 하지만, 동일한 생명 주기는 아니다.
ex) Person과 Address, 역사과목과 학생, 오리와 호수.
"""

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print(f"This duck has a {self.bill.description} bill "
              f"and a {self.tail.length} tail")


a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
# duck.about()


"""
When to Use Objects or Something Else.
여기서는 언제 class나 module 등을 사용할지에 대한 가이드 라인을 제시해준다.

 - Object 는 당신이 여러개의 instance가 필요하고, 각각의 행동(method)는 유사하나
각각의 내부상태(attribute)는 다를때 대부분 유용하게 사용할 수 있다.

 - Class 는 상속을 지원하지만, module 은 상속을 지원하지 않는다.
 
 - 무언가를 오직 1개만 있기를 원한다면, module 이 가장 좋다. program 에서 python
module을 아무리 참조해도 오직 한개의 copy만이 load 된다.(java, c++ 에서의 singleton)

 - 만약에 여러개의 변수와 변수안에 여러 value가 있고 여러 function 으로 전달되어야 한다면
class 로 구현하는게 훨씬 나을 수 있다. 점점 많은 변수가 추가되고 넘겨짐에 따라 프로그램이
알아보기 너무 어렵게 바뀔 가능성이 있기 때문에 class 내부에 한번에 정의하는게 나을 것이다.

 - 가능한 가장 간단한 solution 을 사용하라. 복잡한 기능 보다는 보다 단순하게
해결하는게 가장 좋은 방법이다.

- dataclass 라는것도 있는데 추후에 알아보게 될 것이다.
"""

"""
Named Tuples
 Named Tuple 이란 tuple의 subclass로 value를 position(offset방식)에 더불어
name(.name 형식)을 통해서도 접근 가능한 tuple을 의미한다.
 앞서 다뤘던 Duck class를 한번 named tuple로 바꿔보자.
이때 namedtuple function은 두개의 argument를 가지게 될 것이다.

1. The name
2. A string of the field names, separated by spaces.

 하지만 Name tuple은 python 에서 자동적으로 지원되지 않는다.
따라서 Module 을 불러와야 한다. 다음 예시를 통해 한번 보자.
"""

# namedtuple 을 불러와 사용하는 예시.
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
# print(duck)
# print(duck.bill)
# print(duck.tail)

# dictionary 를 통해 named tuple을 만들 수 있다.

# parts = dict(bill='wide orange', tail='long')
parts = {'bill': 'wide orange', 'tail': 'long'}

duck2 = Duck(**parts)  # '**' : keyword argument, dict의 key,value를 argument로.
# duck2 = Duck(bill = 'wide orange', tail = 'long')  # 위와 똑같다.

# print(duck2)

""" Named tuple은 immutable 이지만, replace로 field를 대체하고 
또 다른 named tuple을 return 할 수 있다. """

duck3 = duck2._replace(tail='magnificent', bill='crushing')
# print(duck3)

# 또한 duck을 dictionary로 정의할 수도 있다.
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
# print(duck_dict)

duck_dict['color'] = 'green'  # dictionary 에 field 추가도 가능.
# print(duck_dict)


# duck.exam = 'good' name_tuple 방식으론 추가가 안된다.


"""
Named Tuple 에 대한 몇가지 특징을 정리하자면 다음과 같다.
1. Named Tuple은 immutable object 처럼 보이고, 행동한다.
2. object 보다는 공간, 시간적으로 효율적이다.
3. attribute 접근방식이 offset 방싞뿐만아니라 .name 형식으로 접근가능하다.
4. Named Tuple을 dictionary key로 사용 가능하다.
"""


"""
Dataclasses
 많은 사람들은 object 를 주로 데이터를 저장하기 위해 만들고는 한다.
방금 우리가 앞서 공부한 named tuple도 마찬가지로 data store 로 사용됐다.
python 3.7 에서는 dataclasse 가 도입됐다.
"""

# 기존의 간단한 object
class TeenyClass():
    def __init__(self, name):
        self.name = name

teeny = TeenyClass('itsy')
# print(teeny.name)

# 똑같은 기능을 하는 dataclass.
from dataclasses import dataclass
@dataclass  # dataclass decorator 를 필요로 하는 모습.
class TeenyDataClass:
    name: str = 'basic'
    age: int = 5

"""
attribue 선언 방식도 다소 다르다.
name:type, name:type = val
ex)color:str, color:str = 'red'
"""

teeny = TeenyDataClass('modified', '25')
# print(teeny.name)
# print(teeny.age)


"""
dataclass 내에서 argument 를 제공할때, 반드시 class 내부에서
정해진 대로 제공하거나 혹은 named arguement를 이용해야 한다.
"""

from dataclasses import dataclass
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0  # default value가 있어서 object 생성시 따로 지정안해줘도 문제x.

snowman = AnimalClass('yeti', 'Himalayas', 46)
nyaong = AnimalClass(habitat='anywhere', name='cat', teeth=24)
# print(nyaong)
# print(snowman)

""" 다른 object 들처럼 attribute에 접근 가능하다. """
# print(nyaong.habitat)
# print(snowman.teeth)


"""
Attrs
attr 없이 class를 만들고 무엇을 하자니 매우 복잡하고 함수도 여러번나와야하고
typing도 여러번 해야하고 번거로운게 너무나 많다.
그런데 이 attr 을 잘사용하면 이런 피곤함을 줄일 수 있는거 같다.
한번 예제를 통해 살펴보자.
"""

import attr
@attr.s
class Point3D(object):
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()

# print(Point3D(1,2,3))
#
# print(Point3D(1,2,3) == Point3D(2,3,1))
# print(Point3D(1,2,3) == Point3D(1,2,3))
# print(Point3D(3,2,3) > Point3D(1,2,3))
#
# print(attr.asdict(Point3D(1,2,3)))

""" 사실 아직 내 단계에서는 attr의 유용성이 아직 안와닿는게 사실이다.
이론의 학습을 끝내고 실제 예제 단계로 넘어가면서 하게 될것들에 집중하고 싶다."""


"""Things to Do"""

# 10.1
class Thing():
    def __init__(self):
        print(self)


example = Thing()
print(Thing)
print(example) # its same.

# 10.2

class Thing2():
    def __init__(self):
        self.letters = 'abc'
        # print(self.letters)

# Thing2()
Thing2 = Thing2()
print(Thing2.letters)

# 10.3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'
        print(self.letters)

Thing3()





















































