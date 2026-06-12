# Q9. Perform the following Set and Tuple operations: (2 Marks) 
# • Create a set of 5 programming languages (include 2 duplicates) — print to show uniqueness 
# • Create another set of 3 languages and perform: union, intersection, difference 
# • Create a tuple of 5 city names 
# • Count occurrences of a city, find its index, and check if a city exists in the tuple 
# • Try to modify the tuple and handle the error with a proper message


languages1 = {"Python", "Java", "C++", "Python", "Java", "JavaScript"}

print("Set 1:", languages1) 


languages2 = {"Python", "C", "Java"}


print("Union:", languages1.union(languages2))
      
print("Intersection:", languages1.intersection(languages2))


print("Difference:", languages1.difference(languages2))




cities = ("Pune", "Mumbai", "Delhi", "Pune", "Bhopal")

print("Count of Pune:", cities.count("Pune"))


print("Index of Delhi:", cities.index("Delhi"))


if "Mumbai" in cities:
    print("Mumbai exists in the tuple")
else:
    print("Mumbai does not exist in the tuple")


try:
    cities[0] = "Indore"
except TypeError:
    print("Error: Tuple cannot be modified because it is immutable.")