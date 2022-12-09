"""
 여기서 부터 python 의 실질적인 실제 세계 프로그래밍에 들어갈 것이다.
우린 여기서 먼저 data를 다루는 방법에 대해 공부 할 것인 데, data 와 관련해서
data science 는 현재 아주 중요한 산업 분야 이기 때문에 알아두는게 좋다.
 먼저 기초적인 data format 에 대호 공부하고 data science를 한번 경험해보자.
data format은 text, binary로 나뉘어 지는데 지금까지 스킵한 것들에 대해 배워 볼것이다.

1. string
- unicode character
- regular expression patter matching

2. binary
- bytes for immutable eight-bit values
- bytearrays for mutable ones.
"""

"""
Text Strings:Unicode
 Python 3 에서 string은 unicode character 의 연속체이다.
이것이 2 에서 3으로의 최대의 변경점이라고 볼 수 있겠다.

 computer storage 에서 basic unit은 byte(8 비트로 이루어진) 이지만
ASCII 에서는 오직 7 bit로 여러가지의 대문자, 소문자, 마침표 등등을 표현한다.

 하지만 실제 세계에서는 ASCII가 제공하는 것보다 더 많은 것들이 있기 때문에
8 개의 digit에 더 많은 letter 와 symbole을 넣으려는 시도가 많이 있었다.
"""

"""
Python3 Unicode Strings
 만약 Unicode id와 문자에 해당하는 name을 알고잇따면 pything string 내에서도
사용 가능하다.
 특히 python의 unicodedata module은 양방향으로 번역해주는 기능을 가지고 있다.
1. lookup() : case-insensitive name을 받아 Unicode character를 리턴.
2. name() : Unicode character를 받아 uppercase name을 리턴.
 다음의 함수 예시를 보자.
"""

# python unicode 를 통해 name을 검색하고, name을 통해 character를 검색하는 함수.

import unicodedata

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

# 한글도 된다!!
# unicode_test('ㅁ')  # 무조건 1개의 unicode character 이여야먄 되는듯. string은 안됨.

# ASCII Punctuation
# unicode_test('$')

# unicode currency character
# unicode_test('\u20ac')
# unicode_test('\u00a2')

""" 이 과정에서 우리가 겪을수 있는 문제는 font에 관한 것이다.
몇몇의 font는 모든 unicode 문자의 이미지를 갖고 있지 않기 때문이다. """

# unicode_test('\u2603')

name = unicodedata.name('\u00e9') # 일반적으로 typing을 통해 못나타내는 글자.
# print(f"name: {name}")
# print("lookup name:", unicodedata.lookup(name))

# cafe를 code, name을 통해 string 으로 구체화 해보기.
place = 'caf\u00e9'
# print(place)

place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
# print(place)

# 하지만 이렇게 쓰면 너무 길다. 따라서 변수에 저장후 사용이 가능하다.
# test = '\N{LATIN SMALL LETTER E WITH ACUTE}'
test = unicodedata.name('\u00e9')
test2 = unicodedata.lookup(test)
# print(test)  # 해당 코드의 이름.
# print(test2)  # 이름을 통해 검색한 결과의 문자.
# print('caf' + test2)

# len()은 unicode 문자의 수를 센다. 따라서 다음의 두개를 보면 같다.
# print(len('$'))
# print(len('\U0001f47b'))

""" 만약에 해당 문자의 Unicode numeric ID를 알고 있다면
ord() 와 char() function을 사용해서 integer id와 single character
간에 전환 시킬 수 있다."""

# print(chr(233))
# print(chr(0xe9))
# print(ord(chr(0xe9)))
# print(ord(chr(233)))


"""
UTF-8
 Unicode character 를 다룰때, 일반적인 string 처리의 경우에는 별 문제가 없다.
하지만 data를 외부 세계와 교환 할때, 몇가지 필요한게 있다.

1. character string-> byte 로 encoding 할 방법.
2. byte -> character string 로 decoding 할 방법.

 만약 Unicode 내의 문자 수가 65536보다 적었다면 2byte로도 충분히 표현하겠지만
실제로는 이보다는 더 많이 있으므로, 불가능하고 따라서 대안이 떠오른다.
 그래서 Ken Thompson과 Rob Pike는 UTF-8 dynamic encoding scheme를 고안했다.
이 방식은 Unicode 문자를 나타내기 위해 1~4개의 byte를 사용한다.

- One byte : ASCII
- Two Bytes : Latin-derived languages
- Three bytes : rest of the basic multilingual plane
- Four bytes : for the rest, including asian languages and symbols.

UTF-8 standard text encoding은 python, linux, html등 에서 사용되며
빠르고 완전하고 작동도 잘한다. 부디 많이 사용해주길 바란다.

특히 외부에서 python string으로 변경시키고자 할때, 원본이 UTF-8 format으로
encoding 되도록 해라. 그렇지 않으면 exception 이 발생하게 도리 것이다.
"""

# byte를 표준으로 byte로 만들기->encoding, byte 풀어헤치기->decoding ?


"""
Encode
 string을 byte로 encoding 할 수 있다. 바로 encode() function 인데,
첫번째 argument는 encoding name으로 어느 형태로 할것인지 를 나타낸다.

- 'ascii' : 옛 7bit ASCII
- 'utf-8' : 8 bit variable-length 엔코딩, 가장 많이 쓰이는 것.
- 'latin-1' : ISO 8859-1
- 'cp-1252' : common window encoding
- 'unicode-escape' : python unicode format (위에서 한것들)

한번 예시를 통해 한번 보자.
"""

snowman = '\u2603'
# print(snowman)
# print(len(snowman))  # 1글자 unicode character.

# 이제 snowman 을 encoding 해보자.
ds = snowman.encode('utf-8')  # utf-8 형식으로 encode
# print(len(ds))  # 달라진 길이.
# print(ds)  # 출력도 달라진다.

""" 물론 UTF-8 말고 다른 encoding 방식을 사용하는것도 가능은 하지만, 만약에
해당 encoding 방식으로 호환되지 않는 unicode string라면 오류가 발생한다.
예를 들어 지금 상태에서 ascii encoding 을 사용하면 에러가 발생하게 된다."""

# ds = snowman.encode('ascii') #  error 발생.

"""
encode() function 의 두번째 argument.
두번째 argument는 encoding exception을 피하기 위해 취해진다.
앞서 봤듯이, encoding 양식에 따라 지원하지 않으면 에러가 발생한다.
하지만 두번째 argument를 이용해 그 error의 발생을 방지 할 수 있다.
"""

# encode 되지 않을때 그냥 던져버리는 'ignore'
# print(snowman.encode('ascii', 'ignore'))

# 알수없는 character 에 대해 '?'로 대체되는 'replace'
# print(snowman.encode('ascii', 'replace'))

# python unicode character string 으로 변환되는 'backslashreplace'
# print(snowman.encode('ascii', 'backslashreplace'))

# 출력가능한 unicode escape sequence 로 나타내고 싶을때 'xmlcharrefreplace'
# print(snowman.encode('ascii', 'xmlcharrefreplace'))


"""
Decode
 Decoding은 byte string을 unicode text string으로 바꾸는 것을 의미한다.
우리가 외부에서 text를 받아올때, byte string으로 encoding 한다.
여기서 까다로운 부분은 바로 실제로 무슨 encoding 기법이 사용됐는지를 파악하는 것이다.
왜냐면 unicode string을 얻기위해 decoding 해야 되기 때문이다.

 문제는 byte string 내에 어느 encoding이 쓰였는지 나타내지 않는 다는 것이다.
아무튼 예시를 통해 한번 살펴보자.
"""

place = 'caf\u00e9'
# print(place)
# print(type(place))

# 위의 것을 UTF-8 방식으로 encoding 하기.
place_bytes = place.encode('utf-8')
# print(place_bytes)
# print(type(place_bytes))
# print(len(place_bytes))  # 크기가 5임에 주의. 마지막의 e 가 2개로 취급된듯.

# 아무튼 다시 decoding 해보자.
place2 = place_bytes.decode('utf-8')
# print(place2)  # 원본으로 돌아왔다.

# 이것은 우리가 똑같이 utf-8으로 encoding, decoding 한 결과. 만약 다른걸로 하면?
# place3 = place_bytes.decode('ascii')  # ascii의 경우 error가 발생한다.

place4 = place_bytes.decode('latin-1')
place5 = place_bytes.decode('windows-1252')
# print(place4, place5)

# 이처럼 다양하게 할 수 있지만 가능하면 UTF-8으로 나타내도록 하자.


"""
HTML Entities
 python 에서는 unicode 대신 HTML character entities 를 이용해 conver 하는
또 다른 방식을 제공한다. 이 방식은 특히 web 에서 작업하는 경우 더 간단한 방식이다.
게다가 unicode name을 일일히 찾아볼 필요도 없다. 다음 예시를 보자.
"""

import html
# print(html.unescape("&egrave;"))
# print(html.unescape("&#xe9;"))

""" named entity translation 을 dictionary 형태로 import도 가능하다.
이 경우 '&', ';' 둘다 drop 가능하다."""

from html.entities import html5
# print(html5["egrave"])
# print(html5["egrave;"])  # 둘이 똑같음.

""" single python unicode 문자 -> HTML entity name 의 경우
ord() 에 character의 decimal value를 사용하라."""

import html
char = '\u00e9'
dec_value = ord(char)
# print(html.entities.codepoint2name[dec_value])

# unicode string이 1글자 보다 더많은경우. 아래와 같이 한다

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
# print(byte_value)
# print(byte_value.decode())  # byte_value를 HTML compatible string으로 바꾸기 위함.


"""
Normalization.
 몇몇의 unicode characters 들은 한번의 이상의 unicode encoding 으로 나타낼 수 있다.
겉보기에는 같아보이지만, 내부 byte sequence가 다르기 때문에 같지는 않다.
한번 예시를 통해 알아보자.
"""

eacute1 = 'é'  # UTF-8, pasted
eacute2 = '\u00e9'  # Unicode code print
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'  # Unicode name
eacute4 = chr(233)  # decimal byte value
eacute5 = chr(0xe9)   # hex byte value
# print(eacute1, eacute2, eacute3, eacute4, eacute5)
# print(eacute1 == eacute2 == eacute3 == eacute5 == eacute5)

# 몇가지 sanity check를 해보자
import unicodedata
# print(unicodedata.name(eacute1))
# print(ord(eacute1))  # decimal integer
# print(0xe9)

# 이제 평범한 e와 accent를 합쳐 accented e를 한번 만들어 보자.
eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
# print(eacute_combined1, eacute_combined2, eacute_combined3)
# print(eacute_combined1 == eacute_combined2 == eacute_combined3)
# print("length of combined:", len(eacute_combined1))
# print("length of basic:", len(eacute2))

# 두개를 결합해 하나의 Unicode character를 만들었다. 그렇다면 이게 오리지널과 같을까?
# print(eacute1 == eacute_combined1)  # 다르다.
# print(eacute1, eacute_combined1)

""" 그리고 위와같이 서로같은 형태처럼 보이지만 막상 그것을 이용해 뭔가를 하려고 하면
똑같이 작동하지 않을 가능성이 높다. 
 이 경우에는 unicodedata module 내부의 normalize() function을 사용하면 된다."""

import unicodedata
eacute_normalize = unicodedata.normalize('NFC', eacute_combined1)  # 원본과 같아짐.
# print(len(eacute_normalize))
# print(eacute_normalize == eacute1)
# print(unicodedata.name(eacute_normalize))

""" 더 많은 정보를 원한다면 pg229 의 여러가지 Unicode 대한 정보들이 간략하게
정리된 링크들이있으니 한번 참고해보라. """


"""
Text Strings:Regular Expressions.
 앞서 까지는 간단한 string opeartion에 대해 공부했지만, 이제는 
regular expression를 통해 보다 복잡한 pattern matching에 대해 공부할 것이다.
이러한 것들은 모두 standard module 're' 에서 제공된다.
match 하고싶은 pattern이라는 string을 정의하고, source 라는 string을 match 한다.
한번 예시를 통해 살펴보자.
"""

import re
result = re.match('You', 'Young Frankenstein')
# print(result)

""" 여기서 'You' 는 우리가 찾고있는 pattern 이며,
'Young Frankenstein'은 우리가 원하는 string인 source 이다.
match() 함수는 source가 pattern 으로 시작하는지를 확인한다.
반면에 search() 함수는 source 내에 해당하는 pattern이 위치 상관없이 찾는다. """

# pattern 을 compile 하는것은 match를 빠르게 하기 위함.
import re
youpattern = re.compile('You')

# compiled 된 pattern 에 match를 수행.
import re
result = youpattern.match('Young Frankenstein')

""" match()만이 pattern 과 soruce를 비교하는 유일한 방법은 아니다. 
이외에도 아래와 같이 여러개 방식이 있다.
- search() : 아무 위치에나, 처음으로 match 되는것을 return 한다. 
- findall() : match 되면서 겹치지 않는 모든것들의 list를 return 한다.
- split() : pattern 과 match 되는 source를 split 하고 string piece의
list를 return 한다. 
- sub() : replacement argument를 받아서 source의 pattern에 해당하는 것들을
replacement로 대체 한다. """


"""
Find Exact Beginning Match with match()
 그래서 string 'Young Frankenstein'이 word 'You'로 시작한다고 볼 수 있을까?
다음의 코드를 한번 봐보자.
"""

import re
source = 'Young Frankenstein'
m = re.match('You', source)  # match starts at the beginning of source
# if m:  # match returns an object, do this to see what matched
#     print(m.group())

m = re.match('^You', source)  # start anchor does the same
# if m:
#     print(m.group())


import re
source = 'Young Frankenstein'
# m = re.match('Frank', source)
# if m:
#     print(m.group())  # 이 경우에는 아무것도 출력 되지 않는다.

# walrus operator 를 이용하면 위의 예시를 짧게 할 수 있다.
# if m := re.match('Frank', source):
    # print(m.group())  # 그래도 맨처음에 Frank가 없어서 작동은 안된다.

# 이제는 match() 말고 search()를 통해 해당 string 내에 Frank가 있는지 확인해보자.
import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
# print(m)  # m에는 search, match 등을 실행한 정보가 담겨있음을 알 수 있다.
# if m:
#     print(m.group())

# 한번 여기서는 pattern 을 변화시켜서 match를 다시 진행해보자.
import re
source = 'Young Frankenstein'
m = re.match('.*Frank', source)
# if m:
#     print(m.group())

""" .*Frank 에 대한 설명
- '.' : any single character 를 의미.
- '*' : zero or more of the preceding thing.
- '.*' : any number of character(0개도 포함) 
- 'Frank': 우리가 찾고자하는 것."""


"""
Find First Match with search()
 search() 를 이용하면 string 내에 어디있든 찾고자하는 pattern을 찾을 수 있다.
"""

import re
source = 'Young Frankenstein'
# if m := re.search('Frank', source):
#     print(m.group())

"""
Find All Matches with findall()
 지금까지는 match 되는 1개만 찾았었다.
그런데 만약 당신이 string 내에 'n'이 몇개나 있는지 확인하고 싶다면
무슨 방법을 써야 할까?
"""

# 일반적인 string 내의 n이 몇개있는지 파악하는 방법.
import re
source = 'Young Frankenstein'
# if m := re.findall('n', source):
#     print(m)

# print(f'Found {len(m)} Mathces')

# How about 'n' followed by any character
import re
source = 'Young Frankenstein'
# if m := re.findall('n.', source):
#     print(m) # 근데 n 자체는 출력이 되질 않는다. 어떻게해야할까?

# 대안 방법.
import re
source = 'Young Frankenstein'
# if m := re.findall('n.?', source):
#     print(m)

"""
Split at Matches with split()
여기서는 pattern 으로 string 을 list로 나누는 예시를 보여줄 것이다.
(string의 split() method가 하는일과 유사함!)
"""

import re
source = 'Young Frankenstein'
m = re.split('n', source)
# print(m)

"""
Replace at Matches with sub()
string의 replace()와도 비슷하다. 하지만 pattern을 기준으로 한다.
"""

import re
# if m := re.sub('n', '?', source):  # 'n'을 '?'로 대체.
#     print(m)

"""
Patterns:Special Characters
일단 우리가 앞서 배운 기초들이다.
- literal match with any nonspecial characters
- Any single character except \n with '.'
- Any number of the preceding character (including zero) with '*'
- Optional (zero or one) of the preceding character with '?'
"""

# alphanumeric : 숫자와 글자를 쓴.
# whitespace : 공백문자(탭, 스페이스바, 개행 문자 등등)
# word boundary : 단어경계, 컴퓨터에서 사용되는 데이터를 단어 단위로 구별하는 경계

""" 
Special characters
- \d : A single digit
- \D : A single nondigit
- \w : An alphanumeric character
- \W : An non-alphanumeric character
- \s : A whitespace character
- \S : A nonwhitespace character
- \b : A word boundary (between a \w and a \W)
- \B : A nonword boundary
"""

""" Python의 'string' module 은 우리가 테스트에 쓸 string 상수를 사전에 정의해놨다.
여기서는 'printable' 을 사용하는데, 100개의 출력가능한 ASCII 문자들인데
문자, 숫자, 공백문자, punctuation 등을 포함하고 있다. """

import string
printable = string.printable
# print(len(printable))  # 정말 크기가 100인지?
# print(printable[0:50])  # 무슨내용들이 있는지.
# print(printable[50:])  # 50부터 끝까지. 공백문자들은 안보인다.

# print(re.findall('\d', printable))  # 숫자를 모두 출력.
# print(re.findall('\w', printable))
# print(re.findall('\s', printable))

"""
정규 표현식(Regualr expression)은 ASCII에만 국한되는게 아니다.
예를들어 '\d'는 unicode가 호출하는 모든 digit 에 대해 match 될 수 있다.
한번 좀 변화된 예제를 사용해보자. 
"""

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
# print(re.findall('\w', x))

"""
Patterns: Using Specifiers
 이제 'punctuation pizza'를 만들어보자. 무엇을 이용해서?
main pattern specifers for regualr expressions 들로 말이다.
그리고 pattern sepcifiers 의 목록은 다음과 같다.
expr과 이탈릭체의 단어는 any valid regular expression 을 의미한다.

 상당히 많은 pattern specifiers 들이 있지만 여기에 적기에는
너무 번거로우므로, 공부하는 교재의 235pg(pdf 기준 265)를 참고하라.
"""

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

""" 이제 좀 다른 regular expression pattern string을 사용해서
source string과 match 시켜보려 할 것이다. """

# wish를 찾기.
# print(re.findall('wish', source))

# wish, fish를 찾기.
# print(re.findall('wish|fish', source))

# 시작지점에서 wish 찾기
# print(re.findall('^wish', source))  # 없으니 안나온다.

# 시작지점에서 'I wish' 찾기
# print(re.findall('^I wish', source))

# 끝 지점에서 fish 찾기
# print(re.findall('fish$', source))  # 없다 !

# 끝지점에서 fish tonight. 찾기
# print(re.findall('fish tonight.$', source))

""" 이런 '^' 과 '$' 들은 anchor 라고도 불린다.
'^' anchor는 string의 시작지점에서 검색을 하고 '$' anchor는 끝에서 한다.
'$' anchor를 사용할때 dot 을 escape 화 시키면 보다 정확하게 될 수 있다."""

# print(re.findall('fish tonight\.$', source))  # 무슨 차이인지는 모르겠다.

# w, f로 시작하는 ish 찾기.
# print(re.findall('[wf]ish', source))  # wish, fish가 출력됨.

# w, s, h중에서 최소한 1개는 포함하는 것.
# print(re.findall('[wsh]+', source))

# ght 와 함께있는 1개의 non-alphanumeric.
# print(re.findall('ght\W', source))

# wish가 뒤따르는 I 찾기.
# print(re.findall('I (?=wish)', source))

# i가 선행하는 wish 찾기.
# print(re.findall('(?<=I) wish', source))

""" 가끔 regular expression patter 과 python string rule이 충돌할 때가있다.
바로 '\b' 를 사용하는 경우인데, 정규 표현식에서는 word의 beginning를 의미하지만
python string 에서는 backspace를 의미한다.
 이와 같은 출동을 피하기 위해서는 escape 문자를 사용해, python의 raw string을 사용해
정규 표현식과 python 의 string rule 과 충돌하는 것을 막아주어야 한다. """

# print(re.findall('\bfish', source))  # fish로 시작하는것 찾기인데, 출력이 안됨!
# print(re.findall(r'\bfish', source))  # raw string 형태로 사용하니 정상처리 되는모습.

"""
Patterns:Specifying match() output
 match(), search() 함수등을 이용할때 모든 결과들은 object m에서 m.group()의 형태로
리턴된다. 그리고 만약에 pattern을 괄호 안에 넣었다면, match는 그것의 group에 생성된다.
그리고 m.groups()로 tuple의 형태로 접근가능하게 된다.
"""

m = re.search(r'(. dish\b).*(\bfish)', source)
# print(m.group())
# print(m.groups())


# delve : (찾기위해)뒤지다.
""" 
Binary Data
 Text data는 다소 어려울 수 있지만, binary data는 다소 흥미로울 수 있다.
여기서 당신은 'endianness'(컴퓨터의 프로세서가 data를 어떻게 byte로 바꾸는지)와
정수에대한 'sign bit'를 알아야 한다.
 또한 binary file format이나 network packet을 data를 추출하고 변경시키기 위해서라도
뒤져봐야할 수도있다.
 따라서 이 section 에서는 python 에서의 기초적인 binary data에 대한 wrangling등을
다뤄볼 것이다. (근데 wrangling 가 뭐지?)
"""

"""
bytes and bytearray
 python 3 에서는 8비트의 정수(0~255)를 사용하는데, 두가지의 타입이 있다.
- bytes : immutable, tuple of bytes 와 같다.
- bytearray : mutable, list of bytes 와 같다.
예제와 함께 살펴보자.
"""

# list인 blist, bytes 변수인 the_bytes, bytearaay 변수인 the_byte_array 생성.
blist = [1, 2, 3, 255]
# print(type(blist))
the_bytes = bytes(blist)
# print(the_bytes)
the_byte_array = bytearray(blist)
# print(the_byte_array)

# the_bytes[1] = 255 , 변경이 불가능함을 알 수 있다.

# print(the_byte_array)
the_byte_array[1] = 127
# print(the_byte_array)  # 변경된 모습.

the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0,256))
# print(the_bytes)
# print(the_byte_array)

""" bytes가 bytearray data를 출력할때 python은 nonprintable byte에 \엑스(x) 를
사용하며, printable 가능한것들에는 ASCII equivalents 들을 사용한다.
한번 다음의 예시를 보자. """

# print(the_bytes)


"""
Convert Binary Data with struct
 python 은 text를 다루는데는 많은 도구가 있지만, 비교적으로 binary data를 다루는데에는
도구가 다소 적은 경향이 있다. 그래서 나타나는게 바로 struct module 이다.
 struct module 에서는 data를 C나 C++ 에 있는 struct 와 같이 다룰 수 있다.
그리고 struct를 사용해서 binary data를 pyhon data structures 간에 전환이 가능하다.

 위의 방식을 설명하기 위해, png 파일을 통해서 너비와 높이를 추출해내는 프로그램을 작성해볼것이다.
"""

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
       b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    # print('Valid PNG, width', width, 'height', height)
    print(f'Valid PNg, width: {width} height: {height}')
else:
    print('Not a vaild PNG')


"""
 이 코드에 대한 간략한 설명을 첨부한다.
- data : data 에는 PNG file 로 부터 처음의 30 bytes 를 포함한다. 여기서
분리해놓은 이유는 page 크기에 맞추려고..
- valid_png_header : png 파일의 시작점을 표시해주는 8 bit sequence를 포함한다.
- width, height : width는 bytes 16~19, height는 20~23 에서 추출했다.

 여기서 LL 은 format string 으로 unpack() 함수로 하여금 byte sequence를 어떻게 해석하고
그들을 python data type으로 어떻게 assemble 할지를 의미한다.
- '>' : 정수들이 big-endian 형식으로 저장된다 라는것을 의미.
- '<' : 정수들이 little-endian 형식으로 저장됨.
- '각각의 L' : 네개의 unsigned long integer를 의미.
"""

# 각각의 four-byte value를 직접적으로 검사하기.
# print(data[16:20])
# print(data[20:24])

""" big 과 little endian 의 방식은 최우측, 최좌측 어느 지점에 숫자를 나타내는가이다.
- big endian 의 경우: b'\x00\x00\x00\x9a'
- little endian 의 경우: b'\x01\x00\x00\x00' """

# python data를 byte로 convert 하고싶다면 struct의 pack() function 을 사용하라.

import struct
print(struct.pack('>L', 154))
print(struct.pack('<L', 1))

exam = struct.pack('>L', 154)
print(struct.unpack('>L', exam))  # little endian 방식으로 하면 overflow 발생하는듯?


"""
Convert Bytes/Strings with binascii()
"""

"""
Bit Operators
"""