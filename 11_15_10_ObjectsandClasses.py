""" 먼저 Object 에 대해 배우게 될 것이다.
지금까지 배운 거의 모든것들, 그러니까 대부분이 object 이다.
object의 내부를 봐야할때는 다음과 같다.
1.존재하는 object의 behavior을 수정하거나
2. 스스로의 것으로 만들고 싶을때 이다.
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
#     def __init__(self):  # init의 parameter 로는 반드시 self이여야한다.
#         pass

class Dog:
    def __init__(self, name):
        self.name = name


a_dog = Dog('doggy')
""" 위의 한줄이 하는 일은 다음과 같다.
1. Dog class 의 definition 을 찾는다.
2. memory 에 새로운 object 를 생성한다.
3. object의 init method를 호출한다. 이때 인자로 self와 name을 넘겨준다.
4. 넘겨받은 name을 object의 name에 저장 한다.
5. 생성된 object를 return 한다.
6. object에 a_dog 라는 변수를 붙여준다. """
