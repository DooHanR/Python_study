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
print(snowman)






















