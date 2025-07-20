### Concept 1 : 

    # How can we access variables/data members of 1 class inside another without using inheritance ?

class A():
    def __init__(self, value):
        self.my_var = value

    def test(self, value_1):
        self.my_var_1 = value_1

class B():
    def access_var(self, new_val):
        print(f"{new_val.my_var}")
        print(f"{new_val.my_var_1}")

obj_a = A(10)
obj_a.test(20)

obj_b = B()
obj_b.access_var(obj_a)

### Concept 2 : 

    # How can we access member functions of 1 class inside another class without using inheritance ?

class A():
    def method_A(self):
        print(f"Hello from class A..!!")

class B():
    def method_B(self):
        obj_aa = A()
        obj_aa.method_A()
        print(f"Hello from class B..!!") 
    
obj_bb = B()
obj_bb.method_B()