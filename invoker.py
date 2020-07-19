from command import Command

class Invoker:
    _command: Command = None

    def set_command(self, command: Command):
        self._command = command

    def execute_command(self) -> None:
        if isinstance(self._command, Command):
            print(self._command.execute())
