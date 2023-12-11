from .observer import Observer
class Owner:
    def __init__(self):
        self.animals = []
    def register(self, animal:Observer):
        self.animals.append(animal)

    def notify(self):
        # 주인의 동물들에게 오너가 신호를 보내면 동물들이 반응함.

        for animal in self.animals:
            animal.update()
