# Q5. Create a Login System: (4 Marks) 
# • Private variable __password = 'python@123'
# • Private variable __attempts = 3 
# • Method login(password):
# → Wrong password: attempts -= 1, show remaining
# → If attempts == 0: raise AccountLockedError
# → Correct: print 'Login successful!' 
# • Handle AccountLockedError with finally block.


class AccountLockedError(Exception):
  pass

class loginSystem:
  __password='python@123'
  __attempts=3
  def login(self,password):
    try:
      if password!=self.__password:
        self.__attempts-=1
        print(f"Wrong password: attempts {self.__attempts}")
        if self.__attempts==0:
          raise Exception("AccountLockedError")
      else:
        print("Login successful")
    except AccountLockedError:
      print("AccountLockedError")


user= loginSystem()


user.login("python@1234")
user.login("python@123")
user.login("paython@123")
user.login("python@123")