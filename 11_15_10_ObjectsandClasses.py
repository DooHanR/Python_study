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

# dog class 에서 object 가 어떻게 행동하라고
# 명시하지 않았기 때문에 아무것도 출력되지 않는 모습이다.

# attribute 할당하기.
a_dog.age = 10
a_dog.name = "Danchu"
a_dog.nemesis = another_dog

another_dog.name = "Flowerbutton"

# print(a_dog.age, a_dog.name, a_dog.nemesis.name)

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
# class Dog:
#     def __init__(self):  # init의 parameter 로 반드시 self가 있어야 한다.
#         pass

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
 mro() method는 해당 class이 object가 지닌 method, attribute를 가진
class 들의 list를 리턴 한다.
 __mroo__ attribute 는 그러한 class들을 tuple로 나타낸 것이다.
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
print(mule.says())
print(hinny.says())


























































