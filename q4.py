# Q4. Create class AgeVerification: (4 Marks)
# • Method set_age(age):
# → If age < 0 : raise ValueError 
# → If age < 18 : raise custom UnderAgeError
# → If age > 100 : raise custom InvalidAgeError 
# → Else : print 'Valid age!'
# • Handle all exceptions with finally block.


class AgeVerificatrion:
    def set_age(self,age):
     try: 
       if age< 0:
           print(" ValueError")
       elif age<18:
           print(" UnderAgeError")
       elif age>100:
           print("InvalidAgeError")
       else:
           print("valid Age")
     except ValueError:
        print("valueError")
Age1=AgeVerificatrion()
Age1.set_age(20)
Age1.set_age(6)
Age1.set_age(105)