class PyCharm:
    def execute(self):
        print("compile")
        print("run")

class MyEditor:
    def execute(self):
        print("spell checker")
        print("compile")
        print("run")

class Laptop:
    def code(self,ide):
        ide.execute()

ide=MyEditor()
lap = Laptop()
lap.code(ide)


