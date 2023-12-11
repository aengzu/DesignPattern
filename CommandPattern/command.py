from Dog import Dog
class Command:
    def execute(self):
        pass

class PrintCommand(Command):
    def __init__(self, print_str : str):
        self.print_str = print_str
    def execute(self):
        print(f'from print command: {self.print_str}')

class DogCommand(Command):
    def __init__(self, dog:Dog, commands):
        self.dog = dog
        self.commands = commands
    def execute(self):
        for command in self.commands:
            if command=='sit':
                self.dog.sit()
            elif command=='stay':
                self.dog.stay()