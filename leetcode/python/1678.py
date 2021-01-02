class Solution:
    def interpret(self, command: str) -> str:
        command = 'o'.join(command.split("()"))
        command = 'al'.join(command.split("(al)"))
        return command