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
fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

""" 만약 large source string이 있다면, chunk를 입력할 수 있다.(slices를 이용)
소스가 모두 끝날떄까지(until the source is done). 한번 예시를 보자."""

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()
# slice를 통해 exception 없이 끝을 넘어서까지도 가능하게해준다.
# 크기는 150인데 100, 100 2번 반복하니까!

# x를 사용하면 이미 존재하는 경우에는, 쓰기가 불가능. 이 경우는 에러가 생긴다
# fout = open('relativity', 'xt')

# 이 경우에는 exception handler를 통해 해결 볼 수 있다
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('Error: hey! relativity is already exists! Be careful dude!')














