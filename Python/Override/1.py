class C1:
    def m(self):
        return 'parent'


class C2(C1):
    def m(self):
        return 'child'


class C3(C1):
    def m(self):
        return super().m() +" child"

a = C3()
print(a.m())
