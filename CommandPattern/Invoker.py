from command import  Command
class Invoker:
    def __init__(self):
        self.command_list = []

    def addCommand(self, command:Command):
        self.command_list.append(command)

    def runCommands(self):
        for command in self.command_list:
            command.execute()
