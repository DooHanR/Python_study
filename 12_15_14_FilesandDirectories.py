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

# with open('relativity', 'wt') as fout:
#     fout.write(poem)

# 이 이후에는 file이 자동적으로 닫히게 된다.

"""
Change Position with seek()
 파일을 읽거나 쓸때, python은 파일내의 당신의 위치를 추적한다.
- tell() : 파일의 시작위치에서부터의 현재 위치를 return 한다.
- seek() : 파일내의 다른 offset 위치로 이동하게 해준다.
"""

fin = open('bfile', 'rb')
# print(fin.tell())  # 현재 위치를 출력. 시작지점에 존재함.
# print(fin.seek(255))  # 이동한 위치를 출력.

bdata = fin.read()
# print(f"bdata length: {len(bdata)}")
# print(f"bdata[0]: {bdata[0]}")

""" 파일내에 포인터가 가리키는곳이 255이기 때문에, fin.read()시 255 위치에서부터
읽고 255 다음이 바로 끝나는 지점이므로, 아래에 bdata의 길이와 0의 offset에 해당하는
것들이 그것에 맞춰서 나오게 된 것이다.
 이는 read, write와 같이 파일을 다루는 기능이 현재 위치한 offset을 기준으로 행해진다는
것을 알 수 있으며, 평상시에는 시작지점인 0에서부터 시작한다는 것을 알 수 있다."""

""" seek() 함수는 두번쨰 매개변수로 origin을 지정해 몇가지 기능을 수행할 수 있다.
seek(offset, origin) 일때.
- origin == 0 (default) : 시작지점에서부터 offset 만큼 이동한다.
- origin == 1 : 현재 위치에서 offset 만큼 이동.
- origin == 2 : 끝의 위치에서 offset 만큼 이동. """

# 여러가지 방식으로 파일의 마지막 byte를 읽어보자.

fin = open('bfile', 'rb')

# print(fin.seek(-1))
# print(fin.seek(-1, 2))  # 끝지점에서 -1칸만큼 이동. 따라서 255?
# print(fin.tell())

# 파일의 끝까지 읽기.
bdata = fin.read()
# print(f"len bdata: {len(bdata)}")
# print(f"bdata[0]: {bdata[0]}")

# 파일의 현재위치에서 seeking 하기.
fin = open('bfile', 'rb')
# print(fin.tell())  # 현재위치
fin.seek(254, 0)  # 시작지점에서 254만큼 이동!
# print(fin.tell())  # 변경후 위치.

fin.seek(1, 1)  # 현재위치에서 1칸 전진
# print(fin.tell())  # 변경된 위치.

bdata = fin.read()  # 현재 위치에서 파일의 끝까지.
# print(bdata[0])


""" 이러한 기능은 binary file에 유용하며 text 파일에 적용하기는 애매 할 수 있다.
왜냐면 ASCII 와 같이 한 문자에 하나의 byte를 사용하는 경우가 아니라면,
예를들어 UTF-8 과 같은경우, offset 을 계산하는게 매우 어렵기 때문이다."""


"""
Memory Mapping
 Memory-map은 mmap 모듈 내에 있는 기능으로, file의 읽기, 쓰기의 대체제 이다.
이것은 file의 내용물을 메모리 내의 bytearray 처럼 보이게 하는데
자세한 내용은 해당 링크를 확인하자.

documentation: https://oreil.ly/GEzkf
exmaples: https://oreil.ly/GUtdx
"""

"""
File Operations
 Python도 다른 언어들과 마찬가지로, unix 이후에 file operation을 패턴화 했다.
chown(), chmod() 와 같은 함수가 그러한데, 요즘 새롭게 나타난 것들이 있다.
여기서는 일단 python 이 어떻게 기존의 os.path 모듈의 함수와 함께 다루는지 보여주고
새롭게 나온 pathlib 모듈을 사용하는 것을 보여줄 것이다.
"""

"""
Check Existence with exists()
 exists() 함수를 통해 파일의 존재여부를 확인할 수 있다.
이때 상대경로/절대경로의 방식이 있으니, 잘 선택해서 쓰자.
"""

import os
# print(os.path.exists('oops.txt'))
# print(os.path.exists('./oops.txt'))
# print(os.path.exists('waffles'))

"""
Check Type with isfile()
 isfile() 은 매개변수로 받은 이름이 file, directory, symbolic link 인지
여부를 확인 한다.
- isfile(name)
- isdir(directory)
- isabs() : 입력받은 argument가 absolute pathname인지 여부를 결정한다.
"""

# print(os.path.isabs('/big/fake/name'))
# print(os.path.isdir('.'))
# print(os.path.isfile('oops.txt'))
# print(os.path.isdir('oops.txt'))

"""
Copy with copy()
 copy() 는 shutil module 에 속하는 기능이다.
다음의 예시를 한번 보라.
"""

# import shutil
# shutil.copy('oops.txt', 'ohno.txt')

# shutil.move() 는 복사후 원본을 제거한다. 주의해라.

"""
Change Name with rename()
 이름을 변경시킬 수 있다.
"""

import os
# os.rename('ohno.txt', 'ohwell.txt')

"""
Link with link() or symlink() : link(), symlink()로 Link 하기.
 file은 한곳에 존재하지만, 여러이름을 가질 수 있으며 이를 link 라고 한다.

- low level hard link : 주어진 file의 모든 이름을 알기가 어렵다.
- symbolic link : 파일의 모든 이름을 저장해 접근이 가능케하는 대체 방식.

- link() : hard link 생성
- symlink() : symbolic link 생성
"""

# hard link 사용 예시.
# os.link('oops.txt', 'yikes.txt')
# print(os.path.isfile('yikes.txt'))
# print(os.path.islink('yikes.txt'))

# symbolic link 사용 예시.
# os.symlink('oops.txt', 'jeepers.txt')  # 권한이 없다는데??
# print(os.path.islink('jeepers.txt'))

"""
Change Permissions with chmod() : chmod()로 권한 바꾸기?
 Unix 에서, chmod()는 사용자들의 읽기, 쓰기, 실행 권한을 조정할 수 있다.
그리고 사용자의 종류에 따라 user, group, others 로 분류해서 권한을 설정한다.
"""

# owner 만 읽을수 있도록 권한 변경하기.
# os.chmod('oops.txt', 0o400)

# 기존의 방식이 싫다면 stat 모듈을 이용하기.
import stat
# os.chmod('oops.txt', stat.S_IRUSR)

"""
Change Ownership with chown() : chown() 으로 소유권 바꾸기.
 이 기능도 Unix/Linux/Mac 에서 익숙할 것이다.
이것을 통해 uid(user id), gid(group id)를 변경해 소유권을 바꿀 수 있다.
예시를 한번 보자.
"""

uid = 5
gid = 22
# os.chown('oops', uid, gid)

"""
Delete a File with remove() : remove() 로 파일 제거하기.
 oops.txt를 여기서 제거해볼 것이다.
"""

# os.remove('oops.txt')
# print(os.path.exists('oops.txt'))  # 삭제 됐는지?


"""
Directory Operations. : 디렉토리 운영(?)
 대부분의 운영 체제 에는 파일은 계층구조의 형태로 저장되어 있다.
여기서 배우는 os 모듈에서도 마찬가지이며, 다음에 제시 되는
function 등을 통해 그들을 관리한다. 
"""

"""
Create with mkdir() : mkdir() 함수로 디렉토리 만들기.
"""

# os.mkdir('poems')
# print(os.path.exists('poems'))

"""
Delete with rmdir() : rmdir() 로 디렉토리 제거하기.
 rmdir()로 디렉토리를 제거해보자.
"""

# os.rmdir('poems')
# print(os.path.isdir('poems'))

""" 
List Contents with listdir(): listdir()로 내용물 리스트 확인하기.
 직접 예시를 한번 보자. 
"""

# os.mkdir('poems')
# print(os.listdir('poems'))  # 디렉토리 내부의 컨텐츠 list화.
#
# fout = open(r'poems/mcintyre/the_good_man', 'wt')
# fout.write("""Hey this is example.""")
# fout.close()

# print(os.listdir('poems'))

# 뭔가 오류가 있는지 해당 경로로 파일이 생성되지 않는다. 왤까.

"""
Change Current Directory with chdir(): chdir()로 현재 디렉토리 변경.
 디렉토리의 이동을 할 수 있다.
"""

import os
# os.chdir('poems')  # 실행시키진 않는다. 귀찮으니까 !
# os.listdir('.')

"""
List Matching Files with glob() : glob() 함수를 통해 file 매칭.
 glob() 는 Unix 에서도 곧잘 쓰이는 파일, 디렉토리 검색 함수이다.
매우 강력한 기능으로 다음과 같은 규칙이 있다.

- '*": match everything
- ? : match single character
- [abc] : 문자 a, b, or c 를 찾는다.
- [!abc] : 문자 a, b, c 를 제외하고 찾는다.
"""

import glob
# print(glob.glob('1*'))

"""
Pathnames
 현대의 모든컴퓨터는 계층구조로 된 파일과 디렉토리를 가지고 있다.
이때 특정 파일이나, 디렉토리로 가려면 경로가 필요한데 이것을 바로
pathname 이라고 한다.

 이떄 pathname 에는 두가지가 있다
- 절대 경로: root 에서부터 해당 지점 까지의 경로.
- 상대 경로: 현재 위치에서 해당 지점 까지의 경로.

 또한 ('/') 와 ('\\') 사이의 구별도 고려 해야한다.
- Unix, Mac, Web 에서의 경우 : 보통의 slash 를 사용한다.
- Windows 의 경우 : backslash 를 사용한다.

 python 의 경우는 보통의 slash를 separator 로 사용하며,
window 의 경우는 backslash 를 사용하기 때문에 방법이 두개 있다.
1. double backslash 사용하기.
2. python의 raw string 사용하기
"""

# win_file = 'eek\\urk\\snort.txt'
# win_file2 = r'eek\urk\snort.txt'
# print(win_file)
# print(win_file2)

"""
 pathname을 만들때 다음의 세가지를 유의해라.
- 적절한 path separation character 을 사용하라 ('/', '\') 
- pathname 을 만들어라.
- pathlib 을 사용해라. 
"""

"""
Get a Pathname with abspath() : abspath() 함수로 pathname 얻기.
 abspath() 함수는 relative name을 absolute로 바꿔준다.
다음의 예시를 한번 봐보자. 
"""

# print(os.path.abspath('oops.txt'))

"""
Get a symlink Pathname with realpath()
 symlink 가 앞서 oops.txt와 jeepers.txt 끼리 만들어졌는데,
정상적으로 처리했다면 jeeprs.txt를 통해 oops.txt의 경로를
얻어낼 수가 있다.
"""

# print(os.path.realpath('jeepers.txt'))  # symlink 형성에 실패. jeepers의 위치가 나옴.

"""
Build a Pathname with os.path.join() : os.path.join() 으로 pathname build 하기.
 여러개의 경로로된 pathname을 만들때, os.path.join() 을 이용해 적절한 path separation 문자와 함께
여러개의 경로를 결합시킬 수 있다. 다음의 예시를 보자.
"""

import os
# win_file = os.path.join("eek", "urk")
# print(win_file)  # eek 와 urk 가 결합.
# win_file = os.path.join(win_file, "snort.txt")
# print(win_file)  # 위에 적힌 경로들이 모두 적용된것을 볼 수 있다

""" 하지만 이 방식은 어디에서(Mac, Linux, Windows) 실행되느냐에 따라
결과값이 다르게 출격되기 때문에 문제가 될 수 있다.
따라서 pathlib 모듈이 등장하게 된다. """

"""
Used pathlib : pathlib 사용해보기.
 pathlib 기능은 3.4에 추가된것으로, os.path를 대체하기 위해 도입됐다.
아무튼 한번 사용예시를 보자.
"""

from pathlib import Path
file_path = Path('eek') / 'urk' / 'snort.txt'  # 기존의 형식과 상이한것을 볼 수있다.
# print(file_path)  # 내가 윈도우라 그런가? back slash로 나오는데?
# print(file_path.name)

""" 이러한 pathlib 내부의 함수를 통해 다른 시스템에서 실행시 어떻게 나올지를
파악 할 수도 있는데, 다른 운영체제의 사용자들에게 도움을 주고자할때 쓸 수 있겠다. """

from pathlib import PureWindowsPath
# print(PureWindowsPath(file_path))

# https://oreil.ly/yN87f 모든 추가적인 내용은 이 link에 있다.


""" 
BytesIO and StringIO
 만약에 memory 내에 data가 있고, file을 필요로하는 function을 호출하고싶을때는
어떻게 해야할까? 아마도 임시파일에 읽기, 쓰기 없이 data를 수정하고 넘겨주고 싶을것이다.
 
 이럴때 쓸수 있는 두가지의 method가 있다.
이것들은 data를 file-like object로 바꾸어줘서 file function 에서
사용하기 용이하게 바꾸어 준다.

- io.BytesIO : binary data(bytes)
- io.StringIO : text data(str)

 위의 예시로 적합한게 data formant conversion 이다.
여기서는 image data를 읽고, 쓰는 PIL library를 적용해볼 것이다.
PIL library 내의 image object의 open(),save() 함수의 첫번째 매개변수는
'filename', 'file-lie object' 이다.

 아래의 예시로 나올 코드는 BytesIo를 이용해 읽고 in-memory data를 출력한다.
한개 이상의 image 파일을 읽어서, 세가지 다른 format으로 전환시키는데
이때 길이와 첫 10byte를 출력한다.
"""

from io import BytesIO
from PIL import Image
import sys

def date_to_img(data):
    """ PIL Image object를 return함. with data from in-memory <data> """
    fp = BytesIO(data)
    return Image.open(fp)  # memory 에서 읽음.

def img_to_data(img, fmt=None):
    """ PIL Image 에서부터 image data를 리턴. fmt의 형식으로. """
    fp = BytesIO()
    if not fmt:
        fmt = img.format  # original format를 keep.
    img.save(fp, fmt)  # memory에 입력.
    return fp.getvalue()

def convert_image(data, fmt=None):
    """ image data를 PIL image data로 convert. """
    img = date_to_img(data)
    return img_to_data(img, fmt)

def get_file_data(name):
    """ Return PIL Image object for image file <name> """
    img = Image.open(name)
    print("img", img, img.format)
    return img_to_data(img)

if __name__ == "__main__":
    for name in sys.argv[1:]:
        data = get_file_data(name)
        print("in", len(data), data[:10])
        for fmt in ("gif", "png", "jepg"):
            out_data = convert_image(data, fmt)
            print("out", len(out_data), out_data[:10])


























