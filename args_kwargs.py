#  args, kwargs를 사용하는 예제 코드
def add(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)

add(1, 2, 3, 4)


def user_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

user_info(name="김코딩", age="16")
