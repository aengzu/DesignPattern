from command import Command,PrintCommand, DogCommand
from Dog import Dog
from Invoker import Invoker

first_cmd = PrintCommand('first command')
second_cmd = PrintCommand('second command')

first_cmd.execute()
second_cmd.execute()

baduk = Dog()
dog_command = DogCommand(baduk, ['stay','sit','sit'])
dog_command.execute()


print('-------Using invoker--------')
# 인보커 사용하여 한번에 명령 처리
invoker = Invoker()
invoker.addCommand(first_cmd)
invoker.addCommand(dog_command)
invoker.addCommand(second_cmd)

invoker.runCommands()


