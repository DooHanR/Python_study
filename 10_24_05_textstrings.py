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

print('Relase the kraken ' + 'No, wait!')
print('hey dont do that ' 'okay wait!')