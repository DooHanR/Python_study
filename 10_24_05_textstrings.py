# print('Snap')
# print("Crackle")
# 모두 똑같이 작동한다.

# 왜 '', 와 ""가 따로있는걸까.
# 그 이유는 '' 안에 ""을, ""안에 ''을 포함하기 위함이다.

# print("'Nay!' said the naysayer. 'Neight'? siat the horse")
# print('"i hate you" he said, i also said "me too"')
# print("""Dont do that""")
# print('''okay''')

""" 삼중 따옴표는 보통 이렇게 여러줄의 주석을 남기거나
혹은 여러줄의 string을 만드는데에 사용된다.
보통 경우의 "", ''를 사용할 경우 다음줄로 넘기지 못한다. """

# print("Hello world")
# poem2 = '''i do not like thee, Docter Fell
#     The reason why, i cannot tell
#     but this i know, and know full well:
#     i do not like thee, Doctor Fell.
#     '''
#
# print(poem2)
#
# print(str(98.6))
# print(str(1.0e4))

# palindrome = 'A man, \nA plan, \nA canal:\nPanama.'
# print(palindrome)
# print('\tabc')
# print('a\tbc')
# print('ab\tc')

# testimony = "\"i did nothing\" he said. \"or that other thing\""
# print(testimony)

# speech = 'the backslah (\\) bends over backwards...'
# print(speech)

# info = r'Type a \n to get a new line in a normal string'
# print(info)
# poem = r'''boys and girls sdfsf
# asdfsdfsdfsdfsdfasdfsdfsdf'''
# print(poem)
# r을 따옴표 앞에 넣어줌으로써 안에있는것 그대로(raw string)을 출력할 수 있다.

# print('Relase the kraken ' + 'No, wait!')
# print('hey dont do that ' 'okay wait!')

# 파이썬의 경우 다음과 같을 때에는 문장 사이사이에 space를 추가한다.
# a = 'Duck.'
# b = a
# c = 'Grey Duck!'
# print(a + b + c)
# print(a, b, c)
# a + b + c의 형태는 스페이스바가 추가되지 않지만 a, b, c 의 형태는 스페이스바 추가.

# start = 'Na ' * 4 + '\n'
# middle = 'Hey ' * 3 + '\n'
# end = 'GoodBye.'
# print(start + start + middle + end)
# print(start, start, middle, end)

# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters[0])
# print(letters[1])
# print(letters[-1])
# print(letters[-2])
# print(letters[25])

''' 아래와 같은 방식은 오류만이 일어나기 떄문에 또다른 방식이 필요하다. '''
# name =  'Henny'
# name[0] = 'p'
# print(name)

# name = 'Henny'
# name.replace('H', 'P')
# print(name.replace('H', 'P'))
# print('P' + name[1:])
# print(name)

# print(letters[:])
# print(letters[20:])
# print(letters[10:])
# print(letters[12:15])
# print(letters[-3:])
# print(letters[-1:])
# print(letters[18:-3])
# print(letters[-4:-3])
# '''이 경우 -4에서 -3으로 두글자가 나와야 할 것 같지만
# -4에서 -4나 다름이 없기떄문에 한글자만 나오게 된다.'''
# '''[start:end:step] 으로 구성되는데 end의 경우 -1이 추가 된다.
# 예를 들어 letters[10:-3]인 경우 -3에서 -1을 한 -4에서부터이다.'''
#
# print(letters[::7])
# print(letters[4:20:3])
# print(letters[19::4])
# print(letters[-1::-1])
# print(letters[::-1])

# letters = 'abcdefghijklmnopqrstuvwxyz'
# print(letters[-50:])
# print(letters[-50:-51])
# print(letters[70:])
# print(letters[70:71])
#
# print(len(letters))
# empty = ""
# print(len(empty))

# tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
# print(tasks.split(','))
# print(tasks.split())
#
# crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
# crypto_list = ', '.join(crypto_list)
# print("Found and signing book deals:", crypto_list)

# setup = "a duck goes into a bar..."
# print(setup.replace('duck', 'marmoset'))
# print(setup)

'''이때 항상 string과 관련한 함수들 replace, join, split 등등은
대상이되는 스트링의 이름.기능()형식으로 사용 된다는 것에 주의하자
ex)setup.replace('doo', 'han), setup.split(','), join은 좀 다른듯?'''

# print(setup.replace('a ', 'a famous ', 100))
# print(setup.replace('a', 'a famous ', 100))

'''위 처럼 replace 하고자하는 a의 범위를 잘해야한다. a로 한결과
출력된 결과가 개판임을 알 수가 있다.'''

# world = "     earth     "
# print(world.strip())
# print(world.strip(' '))
# print(world.lstrip())
# print(world.rstrip())
#
# blurt = "What the..?!!"
# print(blurt.strip('.?!'))

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

# print(poem[:13])
# print(len(poem))
# print(len(poem[:13]))
# print(poem.startswith("All"))
# print(poem.endswith('That\'s all. folks'))

'''python에서 find함수의 기능은 해당 단어의 offset의 위치를
도출해낸다. 그러니까 peom.find(word)를 통해 word를 찾게된다면
해당 위치의 offset을 반환한다.'''

# word = 'the'
# print(poem.find(word))
# print(poem.index(word))
# print(poem.rfind(word))
# print(poem.rindex(word))
#
# word = "duck"
# print(poem.find(word))
# print(poem.rfind(word))
# print(poem.index(word))
# print(poem.rindex(word))

# word = 'the'
# print(poem.count(word))
# print(poem.isalnum())

# '''10월 26일 공부 시작.'''
#
# setup = 'a duck goes into a bar...'
# print(setup.strip('.'))
#
# '''string은 immutable 변수이다. 따라서 본래의 setup은
# 바뀌지않고, 해당 작업을 수행한 새로운 string이 출력되는 것.'''
#
# print(setup.capitalize())
# print(setup.title())
# print(setup.upper())
# print(setup.lower())
# print(setup.swapcase())
#
# print(setup.center(100))
# print(setup.ljust(50))
# print(setup.rjust(50))


# thing = 98.6
# print(thing)
# print('%f' % thing)
# print('%12f' % thing)
# print('%+12f' % thing)
# print('%-12f' % thing)
# print('%.3f' % thing)
# print('%12.3f' % thing)
# print('%-12.3f' % thing)

# thing = 'woodchuck'
# print('{}'.format(thing))

''' 여기 나오는건 fstring이 아니다. python 3.0 버전 까지에서
사용되는 string 방식.'''

# thing = 'woodchuck'
# place = 'lake'
# dog = 'dog'
#
# print('The {} is in the {}'.format(thing, place))
# print('The {} is in the {}'.format(place, thing))
# print('The {2} is in the {1} and {0}'.format(thing, place, dog))
#
# print('The {thing} is in the {place}'.format(thing='duck', place='lake'))
#
#
# d = {'thing': 'duck', 'place': 'bathhub'}
# print('The {0[thing]} is in the {0[place]}.'.format(d))


''' 지금부터 f-string. python 3.6 부터 지원하기 시작하는 신기능으로
가장 추천되는 방식.'''


# thing = 'wereduck'
# place = 'werepond'
# print(f'The {thing} is in the {place}')
#
# print(f'The {thing.capitalize()} is in the {place.capitalize()}')
# print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
# print(f'The {thing:>20} is in the {place:.^20}')
#
# print(f'{thing =}, {place =}')
# print(f'{thing[-4:] =}, {place.title() =}')
# print(f'{thing = :>4.4}')

'''5챕터의 things to do.'''

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(song.replace(' m', ' M'))

questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest.",
    "What makes the sound 'Sis! Boom! Bah!'?"
    ]

answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop'  goes the weasel."
]

print(f'Q:{questions[0]}\n'
      f'A:{answers[1]}\n\n'
      f'Q:{questions[1]}\n'
      f'A:{answers[0]}\n\n'
      f'Q:{questions[2]}\n'
      f'A:{answers[2]}\n')


"""5.3 Write the following poem by using old-style formatting.
Substitute the strings 'roast beef', 'ham', 'head', and 'clam'
into this string:"""

a = 'roast beef'
b = 'ham'
c = 'head'
d = 'clam'

print("""My kitty cat likes %s,
    My kitty cat likes %s,
    My Kitty cat fell on his %s,
    And now thinks he's a %s.""" % (a, b, c, d))


"""5.4 Write a form letter by using new-style formatting
Save the following string as letter"""

letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for you support

Sincerely,
{spokesman}
{job_title}"""

"""5.5 Assign values to variable strings named 'salutation',
'name', 'product', 'verbed' (past tense verb), 'room', 'animals', 
'percent', 'spokesman', and 'job_title'. Print letter with
these values, using letter.format()"""

print(letter.format(salutation = 'salutation',
                    name = 'name',
                    product = 'product',
                    verbed = 'verbed',
                    room = 'room',
                    animals = 'animals',
                    amount = 'amount',
                    percent = 'percent',
                    spokesman = 'spokesman',
                    job_title = 'job_title'))


"""After public polls to name things, a patter emerged: an English submarine
(Boaty McBoatface), an Australian racehorse (Horsey McHorseface), and a Swedish
train (Trainy McTrainface). Use % formatting to print the winning name at the state
fair for a prize duck, gourd, and spitz."""

"""이 교재를 계속 쓰는게 맞나 싶은, 그런 느낌이 든다."""