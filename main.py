#Multi-Level Inheritance : Parent --- Child --- GrandChild

class Parent:      #Passing Single Parameter, Thats Why NOT Using INIT Method
    def get_name(self,name):
        self.name = name
    def show_name(self):
        print("Name : ", self.name)

class Child(Parent):      #Passing Single Parameter, Thats Why NOT Using INIT Method
    def get_age(self,age):
        self.age = age
    def show_age(self):
        print("Age :", self.age)

class GrandChild(Child):    #Passing Single Parameter, Thats Why NOT Using INIT Method
    def get_gender(self,gender):
        self.gender = gender
    def show_gender(self):
        print("Gender :", self.gender)

get_data1 = GrandChild()   #Last Class Take
get_data1.get_name("Javed")
get_data1.get_age(24)
get_data1.get_gender("Male")
get_data1.show_name()
get_data1.show_age()
get_data1.show_gender()

get_data2 = GrandChild()   #Last Class Take
get_data2.get_name("Sajid")
get_data2.get_age(20)
get_data2.get_gender("Male")
get_data2.show_name()
get_data2.show_age()
get_data2.show_gender()

get_data3 = GrandChild()   #Last Class Take
get_data3.get_name("Shafi")
get_data3.get_age(25)
get_data3.get_gender("Male")
get_data3.show_name()
get_data3.show_age()
get_data3.show_gender()



