'''python에서 주요한 반북문으로는 2가지 방식이 있다.
1. while
2. for
'''

# count = 1
# while count <=5:
#     print(count)
#     count += 1
#
# print(count)

'''break를 통해 탈출하기. 보통 특정 출력이 나오면 멈추고 싶지만
그 해당시점을 특정하기 어려울때 if와 while 그리고 break를 사용해 탈출.'''

# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == 'q':
#         break
#     print(stuff.capitalize())

'''이번에는 break를 하기보다는 해당 경우를 skip하고 싶을때'''

# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == 'q': # quit
#         break
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, "squraed is", number * number)


'''else를 이용, 반복이 끝났을때 행동 지정해주기'''

# numbers = [1, 3, 5]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print('Found even number', number)
#         break
#     position += 1
# else:
#     print('No even number found')


''' for와 in을 이용해서 반복하기. 굉장히 유용하다
일단 여기서는 6장까지만 배웠고 우리는 string에 대해서만 배웠기 때문에
string을 통해서만 할 것이다. tuple이나 list를 이용한 방식은
나중에 할 듯 하다.'''

# word = 'thud'
# offset = 0
# while offset < len(word):
#     print(word[offset])
#     offset += 1
# for letter in word:
#     print(letter)

'''Cancel with break for와 in 에서.'''

# word = 'thud'
# for letter in word:
#     if letter == 'u':
#         break
#     print(letter) # break를 이용. u를 만나면 탈출. 그전까지는 계속 출력.

''' Skip with continue in IN.
continue를 사용하는것도 while과 마찬가지이다.
마찬가지로 continue를 사용하면 해당 루프의 다음 반복으러 넘어간다.'''

''' Check Break Use wtih Else in IN
반복문이 끝날때 braek 대신 else가 실행.
loop가 제대로 끝났는지 확인하고 싶을떄 유용하다'''

# word = 'thxud'
# for letter in word:
#     if letter == 'x':
#         print("Eek! An 'X'!")
#         break
#     print(letter)
# else:
#     print("No 'x' in there.")


'''Generate Number sequences with range()
range 함수를 통해 메모리의 낭비나 충돌없이 huge range를 만들 수 있다.
이떄 range를 어떻게 사용하느냐에 따라 slice와 유사하게도 사용 가능하다
ex)range( start, stop, step ) 이때 stop은 반드시 있어야하며
step의 경우 -1을 지정해줄 수 있다. 그리고 마지막값은 stop의 바로 직전,
그러니까 stop -1에 생성된다. 아래 예시를 보라.'''

# for x in range(0,3):
#     print(x)
#
# print(list(range(0,3)))

# for x in range(2,-1,-1):
#     print(x)
#
# print(list(range(2,-1,-1)))
# print(list(range(0,11,2)))


'''Things to Do
어라 loop쪽은 Things to do가 왤케 빨리 나오지.'''

''' 6.1 Use a for loop to prin the values of the list [3,2,1,0]'''

# for x in list(range(3,-1,-1)):
#     print(x)


'''6.2 Assign the value 7 to the variable guess_me, and the value
1 to the variable number. Write a while loop that compares number
with guess_me. Print 'too low' number is less than guess me.
if Number euqals guess_me, print 'found it!' and then exit the loop.
if number is greater than guess_me, print 'oops' and then exit the loop.
increment number at the end of the loop.'''

# guess_me = 7
# number = 2
# while True:
#     if number < guess_me:
#         print('too low')
#     elif number == guess_me:
#         print('found it!')
#         break
#     else:
#         print('oops')
#         break
#     number += 1


'''Assign the value 5 to the variable guess_me. Use a for loop
to iterate a variable called number over range(10) if number
is less than guess_me, print 'too low' if it equals
guess_me, print found it! and then braek out of the for loop.
if number is greater than guess_me print 'oops' and then exit 
the loop.'''

# guess_me = 5
# for number in range(10):
#     if number < guess_me:
#         print('too low')
#     elif number == guess_me:
#         print('found it!')
#         break
#     else:
#         print('oops')
#         break

















