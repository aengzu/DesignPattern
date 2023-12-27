
class Component:
    def fn(self):
        pass
class Leaf(Component):
    def fn(self):
        print('leaf')

class Composite(Component):
    def __init__(self, name):
        self.components = []
        self.name = name

    def add(self, component: Component):
        self.components.append(component)

    def fn(self):
        print('composite', self.name)
        for component in self.components:
            component.fn()
