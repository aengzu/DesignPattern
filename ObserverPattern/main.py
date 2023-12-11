from .observer import Cat, Dog
from .owner import Owner

# 강아지, 고양이가 옵저버이고 주인이 이벤트가 된다.
# 주인이 집에 돌아오거나 집합 명령을 내리면 동물들이 반응하는 것
owner = Owner()
cat = Cat()
dog = Dog()

owner.register(cat)
owner.register(dog)


# 업데이트 함수 호출
owner.notify()