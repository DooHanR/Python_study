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



















