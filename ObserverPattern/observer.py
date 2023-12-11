# 옵저버 인터페이스
class Observer:
    def update(self):
        pass


# Observer 베이스 클래스 상속받는 Cat, Dog
class Cat(Observer):
    # 이벤트에 반응했을 때 update
    def update(self):
        print('meow')

class Dog(Observer):
    def update(self):
        print('bark')