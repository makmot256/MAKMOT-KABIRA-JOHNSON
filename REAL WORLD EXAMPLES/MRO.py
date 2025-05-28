# Scenario: Multi-role Access System
class Admin:
    def access(self):
        print("Admin access")

class Editor:
    def access(self):
        print("Editor access")

class SuperUser(Admin, Editor):
    pass

s = SuperUser()
s.access()
print(SuperUser.__mro__)
