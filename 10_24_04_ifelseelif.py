# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# furry = True
# large = False
#
# if furry:
#     if large:
#         print("It's a yeti.")
#     else:
#         print("It's a cat!")
# else:
#     if large:
#         print("It's a whale!")
#     else:
#         print("It's human or a hairless cat")

# color = "green"
# if color == "red":
#     print("It's a tomato")
# elif color == "green":
#     print("It's a green pepper")
# else:
#     print("I've never heard of the color", color)

# x = 7
# if x == 5:
#     print("Yes")
# else:
#     print("No")

# 5 < x and x < 10
# 이와 같은 경우도 헷갈릴 수 있다. 이때 가장 좋은 방법은
# 괄호를 사용하는 것이다.

# (5 < x) and (x < 10)

# some_list = ["a"]
#
# if some_list:
#     print("There's something in here")
# else:
#     print("Hey, it's empty")

# letter = 'o'
# if letter == 'a' or letter == 'b' or letter == 'i' \
#     or letter == 'o' or letter == 'u':
#     print(letter, "is a vowel")
# else:
#     print(letter, "is not a vowel")

# 위의 방식은 매우 pythonic 하지 못하고 번거롭다.
# 아주 간단하게 in을 쓰면 간단하게 해결 할 수 있다.

# vowels = 'aeiou'
# letter = 'b'
# if letter in vowels:
#     print(letter, 'is a vowel')
# else:
#     print(letter, 'is not a vowel')

# tweet_limit = 280
# tweet_string = "Blah" * 50
# diff = tweet_limit - len(tweet_string)
# if diff >= 0: 의 대체이다.
# ':=' 를 이용해서 축약을 이뤄낸것, pythonic 하다!.
# 그리고 ':=' 를 walrus 라고 한다.
# if diff := tweet_limit - len(tweet_string) >= 0:
#     print("A fitting tweet")
# else:
#     print("Went over by", abs(diff))


# Thing To do
# secret = 7
# guess = 5
#
# if secret == guess:
#     print("just right")
# elif secret > guess:
#     print("too low")
# else:
#     print("too high")

# small = True
# green = True
#
# if green:
#     if small:
#         print("it is pea")
#     else:
#         print("it is watermelon")
# else:
#     if small:
#         print("cherry")
#     else:
#         print("pumpkin")


