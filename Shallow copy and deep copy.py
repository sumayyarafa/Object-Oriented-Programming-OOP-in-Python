'''1. User-defined copy:
copy_student(kt)
Creates a new list and copies the course elements into it.
    - kt and kt_us have separate course lists.
    - Adding a course to one list does not affect the other.

2. Shallow copy: copy(kt)
Creates a new Student object, but the courses attribute refers to the same list as the original.
    - The objects are different.
    - The course lists are shared.

3. Deep copy: deepcopy(kt)
Creates a new Student object and a separate copy of its course list.
    - The objects are different.
    - The course lists are separate.'''

from copy import copy, deepcopy
class Student:
   def __init__(self, name, courses):
       self.name = name
       self.courses = courses

def copy_student(obj):
   lst = []
   for c in obj.courses:
       lst.append(c)
   return Student(obj.name, lst)

kt = Student("Kotha", ["OOP", "OOP lab"])
kt_us = copy_student(kt)
kt_py = copy(kt)
kt_deep = deepcopy(kt)
kt.courses.append("ENG")

print(kt.courses)
print(kt_deep.courses)

'''----------Trace the code-------------
Initially, the objects look like this:

Before kt.courses.append("ENG")
Original kt
name = "Kotha"
courses → ["OOP", "OOP lab"]

kt_us — user-defined copy
courses → ["OOP", "OOP lab"] (separate list)

kt_py — shallow copy
courses → same list as kt

kt_deep — deep copy
courses → ["OOP", "OOP lab"] (separate list)'''

#--------------------------------------------------------
