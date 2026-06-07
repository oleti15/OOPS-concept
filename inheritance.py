# SINGLE INHERITANCE
# class Parent:
#     def display(self):
#         print("Parent Class")
# class Child(Parent):
#     def show(self):
#         print("Child Class")
# a=Child()
# a.display()
# a.show()

# Multilevel Inheritance
# class Grand_parent:
#     def display(self):
#         print("Grand Parent Class")
# class Parent(Grand_parent):
#     def dis(self):
#         print("Parent Class")
# class Child(Parent):
#     def details(self):
#         print("Child Class")
# a=Child()
# a.display()
# a.dis()
# a.details()

# Multiple Inheritance
# class Parent:
#     def show(self):
#         print("1st Parent Class")
# class Paren:
#     def show1(self):
#         print("2nd Parent Class")
# class Par(Parent,Paren):
#     def show2(self):
#         print("This is Child Class")
# a=Par()
# a.show()
# a.show1()
# a.show2()

# Hieraricla Inheritance
# class Parent:
#     def show(self):
#         print("Parent Class")
# class Child(Parent):
#     def showing(self):
#         print("1st Child Class")
# class Child2(Parent):
#     def  showes(self):
#         print("2nd Child Class")
# a=Child()
# a.show()
# a.showing()
# b=Child2()
# b.showes()


# HYBRIDE INHERITANCE
class A:
    def s1(self):
        print("Grand Parent")
class B(A):
    def s2(self):
        print("Parent")
class C(A):
    def s3(self):
        print("Parent2")
class D(B,C):
    def s4(self):
        print("Child")
a=D()
a.s1()
a.s2()
a.s3()
a.s4()