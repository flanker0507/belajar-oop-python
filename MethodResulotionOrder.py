# method resolution order // multiple inheritance

class A:
    def show(self):
        print("ini adalah show A")

class B:
    def show(self):
        print("ini adalah show B")

class C(A,B):
    pass

object = C()
object.show()
help(object)