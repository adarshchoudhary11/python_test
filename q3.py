# Q3. Create a Hybrid Inheritance program: (3 Marks)
# • Father: property(), business() • Son(Father): study() 
# • Daughter(Father): dance()
# • GrandChild(Son, Daughter): gaming()
# Create object of GrandChild and call ALL methods.

class Father:
  def property(self):
    print("father has property")
  def business(self):
    print(" Father runs a business")


class Son(Father):
  def study(self):
    print("son is study")


class Daughter(Father):
  def dance(self):
    print("daughter is dancing")


class GrandChild(Son,Daughter):
  def gaming(self):
    print("grandchild is gaming")



GC = GrandChild()

GC.property()
GC.business()
GC.study()
GC.dance()
GC.gaming()