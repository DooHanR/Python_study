"""
여기서는 file, 그리고 directory 에 대해 배울것이다.
 먼저 file에 대해 알아봅시다. file은 byte의 연속체를 의미합니다.
그리고 filesystem 내부에 저장되며, filename으로 접근 할 수 있습니다.
 directory 는 이런 file들의 모음을 의미합니다. 사실 file과 directory는
같은 의미의 동의어로, 실생활에서 쓰이는 용어를 모방해 나타낸 것입니다.
"""

"""
File Input and Output
 python은 file->memory인 읽기, memory->file인 쓰기 모두 간단하게
해낼 수 있다. 그리고 여타 언어와 마찬가지로, Unix의 그것을 모방한 모습을
보여준다.
"""

"""
Create or Open with open()
 open() 은 읽기, 쓰기, 덮어쓰기, 이어쓰기와 같이 file을 다루기 전에 선행되야 한다.

ex) fileobj = open( filename, mode )
 각각의 구성요소에 대해 한번 간단한 설명을 해보자
- fileobj : open() 함수를 통해 리턴받는 file obj를 의미.
- filename : file의 string name.
- mode : file의 type과 무엇을 할지 나타내는 string.

 mode에 대해 얘기해보면, mode의 첫글자는 다음을 의미한다
- r : read
- w : write, 존재하지 않을시에는 생성. 존재할때는 overwritte.(겹쳐쓰다?)
- x : write, 파일이 이미 존재하지 않을때에만!
- a : append(끝에 이어쓰기), 파일이 존재하는 경우에만.

 mode의 두번째 글자는 file의 type을 의미한다.
- t(or nothing) : text.
- b : binary

 파일을 연후에는 위와 같은 기능을 사용해 읽거나 data를 입력해야한다.
그리고 해당 작업이 끝난후에는, 파일을 닫아 주어야 하는데 추후에 'with' function 과 함께
자동화할 수 있을 것이다. 아무튼 예제를 통해 한번 알아보자.
"""

# oops.txt 파일을 만들고 아무것도 쓰지않고 닫아보자.
fout = open('oops.txt', 'wt')  # 현재
fout.close()

"""
Write a Text File with print()
 oops.txt를 재생성하고 한줄을 첨가한뒤에 닫아보자.
여기서는 print를 통해 file에다가 글을 써봤다. 이게 되네?
"""

fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

# print에 file argument를 안썼다면 정상출력이 됐을 것이다.

"""
Write a Text File with write()
 좀전에 print를 이용해 파일에 입력을 했는데, 이번에는 write를 이용해볼 것이다.
여기에서는 여러줄의 data를 한번 넣어볼 것이다.
"""

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relaitve way,
And returned on the previous night.'''

# print(len(poem))

# fout = open('relativity', 'wt')
# fout.write(poem)
# fout.close()

# 똑같은 동작을 print로도 할 수 있다.
# fout = open('relativity', 'wt')
# print(poem, file=fout)
# fout.close()

""" print와 write의 파일쓰기 기능은 약간 다르다. 
print를 이용하면 끝이나 argument의 뒤에 space가 사용된다.
그런데 이런 print를 마치 write 처럼 사용하고 싶다면,
다음의 두 argument를 사용하면 된다.

- sep : ' ', separator, default는 space 로 되어있다. 
- end : '\n', end string """

# 한번 사용예시를 보자.

# fout = open('relativity', 'wt')
# print(poem, file=fout, sep='', end='')
# fout.close()

""" 만약 large source string이 있다면, chunk를 입력할 수 있다.(slices를 이용)
소스가 모두 끝날떄까지(until the source is done). 한번 예시를 보자."""

# fout = open('relativity', 'wt')
# size = len(poem)
# offset = 0
# chunk = 100
# while True:
#     if offset > size:
#         break
#     fout.write(poem[offset:offset+chunk])
#     offset += chunk

# fout.close()

# slice를 통해 exception 없이 끝을 넘어서까지도 가능하게해준다.
# 크기는 150인데 100, 100 2번 반복하니까!

# x를 사용하면 이미 존재하는 경우에는, 쓰기가 불가능. 이 경우는 에러가 생긴다
# fout = open('relativity', 'xt')

# 이 경우에는 exception handler를 통해 해결 볼 수 있다

# try:
#     fout = open('relativity', 'xt')
#     fout.write('stomp stomp stomp')
# except FileExistsError:
#     print('Error: hey! relativity is already exists! Be careful dude!')

"""
Read a Text File with read(), readline(), readlines() 
(텍스트 파일을 read(), readline(), readlines() 함수로 읽어보기.)

 read() 함수를 통해 매개변수없이 전체파일을 한번에 read 할 수 있다.
이때 크기가 너무 큰 파일이라면 메모리를 그만큼 사용하게 되므로 주의하자.
"""

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
# print(poem)

""" read() 함수가 한번에 몇개를 읽을지도 정하는게 가능하다.
한번에 100개씩 읽고, 그 덩어리를 string에 붙이는것을 한번 해보자. """


# poem = ''
# print(f"before: {len(poem)}")
# fin = open('relativity', 'rt')
# chunk = 100
# while True:
#     fragment = fin.read(chunk) # 끝까지 읽은후에는 empty string return. 따라서 break!
#     if not fragment:
#         break
#     poem += fragment
#
# fin.close()
# print(f"after: {len(poem)}")
# print(poem)

""" readline() 함수를 이용. 한번에 한줄씩 읽을 수 있다. 
다음의 예시를 한번 살펴보자. """

# poem = ''  # poem 리셋.
# fin = open('relativity', 'rt')
# while True:
#     line = fin.readline()  # realine()도 마찬가지로 다 읽으면 empty string을 return!
#     if not line:
#         break
#     poem += line
#
# fin.close()
# print(f"readline(): {len(poem)}")

""" Text file을 읽는 가장 좋은방법은 'iterator'를 이용하는 방식이다. 
한번에 하나의 line 을 return 하는데, 이전의 코드보다 훨씬 간단함을 알 수 있다."""

poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close()
# print(poem)  # 이건 정상적인데?
# print(f"iterator: {len(poem)}")

""" 앞서 한 것은 결국 하나의 string poem을 나타내게 된다.
한번 출력을 해보자. """

fin = open('relativity', 'rt')
lines = fin.readline()
fin.close()
# print(len(lines))

# for line in lines:
#     print(line, end='')  # 이렇게 해야 정상출력됨.
#     print(line)  # 다소 이상하게 출력된다.


"""
Write a Binary File with write()
 만약 파일을 열때 'b' 문자와 함께 사용하면 binary mode로 파일을 열게 된다.
이 경우 읽기, 쓰기를 할때 byte를 다루게 된다. 여기 예제에서는 임의로
0 에서 255 까지의 byte value를 만들어 예시를 다뤄볼 것이다.
"""

bdata = bytes(range(0, 256))
# print(f"length of bdata: {len(bdata)}")

# fout = open('bfile', 'wb')
# fout.write(bdata)
# fout.close()

fout = open('bfile', 'wb')  # 열고
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

fout.close()  # 닫고

"""
Read a Binary File with read()
 read로 binary 파일 읽기. 매우 간단하다.
"""

fin = open('bfile', 'rb')
bdata = fin.read()
# print(bdata)
# print(len(bdata))
fin.close()

"""
Close Files Automatically by Using with
 앞서 했던 작은 예시들은 close 없이도, python이 알아서 꺼지게 된다.
하지만 몇몇 경우의 경우는 남아있는 writes 와 같은 것들이 완료되고
꺼져야하는 경우가 있다.
 이럴때를 대비해 python은 context managers를 가지고 있으며,
다음과 같은 형식으로 사용된다.
- 'with expression as variable:', 예시를 한번 보자.
"""

with open('relativity', 'wt') as fout:
    fout.write(poem)

# 이 이후에는 file이 자동적으로 닫히게 된다.

"""
Change Position with seek()
 파일을 읽거나 쓸때, python은 파일내의 당신의 위치를 추적한다.
- tell() : 파일의 시작위치에서부터의 현재 위치를 return 한다.
- seek() : 파일내의 다른 offset 위치로 이동하게 해준다.
"""

fin = open('bfile', 'rb')
print(fin.tell())




























































































