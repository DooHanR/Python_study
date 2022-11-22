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
init() method는 initializer로 생각하라. """

# class 로 많은 object를 생성할 수는 있지만, 해당 class는 프로그램에
# 오직 하나뿐이라는 것을 기억해라.


""" Inheritance
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
give_me_a_Yogo = Yugo()

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
aggregation과 composition 이다. 이 챕터에서 이 대체제 들을 공부 해볼것이다. """


"""Override a Method
앞서 말했듯이 기존의 클래스를 상속한 새로운 클래스는 모든것을 상속받는다.
그럼 이때, 대체하는 것은 어떻게 되는 것일까? 여기서 살펴보게 될 것이다."""

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
    def need_a_push(self):
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

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        # super().__init__ 에서 self argument pass 따라서 optional argument 만 추가하면됨.
        self.email = email

class VirtualPerson(Person):
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

1. mro() method는 해당 class이 object가 지닌 method, attribute를 가진
class 들의 list를 리턴 한다.
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
# print(mule.says())
# print(hinny.says())


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
getters나 setter를 사용해서 이용이 가능하다.
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
    name = property(get_name, set_name)

# 이전의 것들도 여전히 작동은 한다.
don = Duck('donald')
# print(don.get_name())
# don.hidden_name = 'abc'
# print(don.get_name())

# 하지만 이제는 property name을 사용해 hidden name을 변경시킬 수 있다.
don = Duck('DooHan')
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
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

# 작동은 똑같은 모습.
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

# c = Circle(5)
# print(c.radius)
# print(c.diameter)

# c.radius = 7
# print(c.diameter)  # 자동 계산되는 모습을 볼 수 있다.
# c.diameter = 20
# setter property 를 설정하지 않으면 외부에서 건드릴 수 없다. 위에처럼.

""" direct attribute access 보다 property 사용이 더 나은점.
attribute 의 definition을 변경한다면, 오직 class definition 내부에 있는
코드만 바꾸면 된다. 모든 caller 들이 아니라."""


""" Name Mangling  for Privacy
(Mangling=변수, 함수의 이름을 짓이겨서 다르게 바꿔버리는것)
class definition 외부에서 attribute가 노출되지 않도록 하는
명명 규칙으로, (__) 으로 사용한다."""

# 기존의 hidden_name 을 __name 으로 한번 바꿔보자.

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

# fowl.name = 'Donald'
# print(fowl.name)

# print(fowl.__name)
# 변수명을 이용한 접근에서는 오류가 발생한다. 접근할 수 없게 Mangling 된 것이다.

""" 이와 같은 Mangling 은 우발적으로, 혹은 의도적으로 attribute에 접근하는 것을
방지한다.
 하지만 꼭꼭 접근하고 싶다면 다음과 같은 방법이 있다."""

# print(fowl._Duck__name)  # inside the getter 가 출력 안되는것에 주의.


""" Class and Object Attributes 
class에 attribute 를 할당할 수 있다. 그리고 할당된 것들은 자식에게 상속된다."""

class Fruit():
    color = 'red'

blueberry = Fruit()
# print(Fruit.color)
# print(blueberry.color)

# 자식의 것을 바꿔도 class attribute 에 영향을 주진 않는다.
blueberry.color = 'Blue'
# print(f'class :{Fruit.color}, blueberry :{blueberry.color}')

# class 의 것을 바꿔도, 존재하는 자식 오브젝트의 것을 바꾸진 않는다.
Fruit.color = 'Green'
# print(f'class :{Fruit.color}, blueberry: {blueberry.color}')

# 하지만 새롭게 생성되는 오브젝트 의 것에는 반영된다.
Watermelon = Fruit()
# print(f'class: {Fruit.color}, watermelon: {Watermelon.color}')


""" Method Types
몇몇 method는 class의 일부이기도 하고, 몇몇은 class 내부의 object의 일부이기도하고
어떤것들은 둘다 아니기도 하다.

 1. instance method: 선행하는 decorator 가 없는경우.
첫번째 argument는 반드시 invidual object itself 를 refer 하는 'self' 이여야 함..

 2. class method: 선행하는 @classmethod 가 있는 경우.
첫번째 argument는 class 자체를 refer하는 cls(class 말고)이여야 한다.

 3. static method: 선행하는 @staticmethod decorator 가 있는 경우.
첫번째 argument는 object나 class가 아니다."""

""" Instance Methods"""