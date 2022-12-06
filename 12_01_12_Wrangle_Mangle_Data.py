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


"""
































