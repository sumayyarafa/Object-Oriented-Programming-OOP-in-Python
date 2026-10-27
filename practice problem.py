class EnrollmentError(Exception):
   def __init__(self, message):
       print(message)
class AssignmentError(Exception):
   def __init__(self, message):
       print(message)
class GradeError(Exception):
   def __init__(self, message):
       print(message)

def student_id_gen(semester):
   def generator(dept):
       nonlocal semester
       ids = {"cse": [121, 300],
        "ds":[122, 300]}
       while True:
           yield f"{semester}{ids[dept][0]}{ids[dept][1]}"
           ids[dept][1] += 1
   return generator

def faculty_id_gen(semester):
   def generator(dept):
       nonlocal semester
       ids = {"cse": [911, 1],
        "ds":[ 922, 1]}
       while True:
           yield f"{semester}{ids[dept][0]}{ids[dept][1]}"
           ids[dept][1] += 1
   return generator

def limit_checker(func):
   def wrapper(self, student, course):
       total_credits = sum(c.credit for c in student.currently_enrolled_courses)
       if total_credits + course.credit > student.max_credit:
           raise EnrollmentError(
               f"Cannot enroll Name: {student.name} Email: ({student.email}) in {course.code}: "
               f"max credit {student.max_credit} would be exceeded."
           )
       return func(self, student, course)
   return wrapper

def assignment_checker(func):
   def wrapper(*args):
       if args[1].dept != args[2].dept:
           raise AssignmentError(
               f"Cannot assign {args[2]} in {args[1]} due to department missmatch."
           )
       return func(*args)
   return wrapper


class Faculty:
   faculty_members = dict()
   def __new__(cls, name, email, dept):
       if email[-9:] == "uiu.ac.bd":
           raise Exception("Official email should be generated automatically. Please use personal email instead.")
       if email not in cls.faculty_members:
           faculty = super().__new__(cls)
           cls.faculty_members[email] = faculty
       return cls.faculty_members[email]
   def __init__(self, name, email, dept):
       try:
           if self.email == email:
               pass
       except AttributeError:
           self.name = name
           self.personal_email = email
           self.dept = dept
           self.courses = []
   def __repr__(self):
       return f"[ID: {self.id}, Email: {self.email}]"


class Student:
   students = dict()
   def __new__(cls, name, email, dept):
       if email[-9:] == "uiu.ac.bd":
           raise Exception("Official email should be generated automatically. Please use personal email instead.")
       if email not in cls.students.keys():
           student = super().__new__(cls)
           cls.students[email] = student
       return cls.students[email]


   def __init__(self, name, email, dept):
       global flag
       try:
           if self.email == email:
               pass
       except Exception:
           self.name = name
           self.personal_email = email
           self.dept = dept
           self.cgpa = 0
           self.currently_enrolled_courses = []
           self.results = {}
           self.max_credit = 6


   def __repr__(self):
       return (f"[ID: {self.id}, Email: {self.email}, CGPA: {self.cgpa}]")


class Utility:
   utilities = dict()
   def __new__(cls, semester):
       if semester not in cls.utilities.keys():
           obj = super().__new__(cls)
           cls.utilities[semester] = obj
       return cls.utilities[semester]


   def __init__(self, semester):
       try:
           if self.semester == semester:
               print("initialized")
       except Exception:
           self.semester = Utility.get_semester(semester)
           self.student_id_gens = {"ds":student_id_gen(self.semester)("ds"), "cse":student_id_gen(self.semester)("cse")}
           self.faculty_id_gens = {"ds": faculty_id_gen(self.semester)("ds"), "cse":faculty_id_gen(self.semester)("cse")}


   def recruit_faculty(self, name, email, dept):
       faculty = Faculty(name, email, dept)
       faculty.id = next(self.faculty_id_gens[dept])
       faculty.email = self.get_email(faculty)
       return faculty


   def admit_student(self, name, email, dept):
       student = Student(name, email, dept)
       student.id = next(self.student_id_gens[dept])
       student.email = self.get_email(student)
       return student


   @limit_checker
   def enroll_student(self, student, course):
       if student not in course.students:
           course.students.append(student)
           student.currently_enrolled_courses.append(course)
           print(f"{student} is enrolled in {course.code}")
       else:
           raise EnrollmentError(f"Can't Enroll. Student {student.id} is already enrolled in {course.code}.")


   def add_grade(self, student, course, grade):
       if course not in student.currently_enrolled_courses:
           raise GradeError(f"Can't Add grade [{grade}]. Student: {student.id} is not enrolled in {course.code}.")
       if grade not in [4.00, 3.70, 3.30, 3.00, 2.70, 2.30, 2.00, 0.00]:
           raise GradeError(f"Can't Add grade [{grade}] for student: {student.id}. Not a valid grade.")
       student.currently_enrolled_courses.remove(course)
       student.results[course] = grade
       student.cgpa = self.update_cgpa(student)


   def update_cgpa(self, student):
       total_credits = sum(c.credit for c  in student.results.keys())
       weighted_grade = sum(c.credit * student.results[c] for c in student.results.keys())
       return weighted_grade/total_credits


   @assignment_checker
   def assign_faculty(self, course, faculty):
       course.faculty = faculty
       faculty.courses.append(course)
       print(f"{faculty} is assigned to {course}")


   @classmethod
   def get_semester(cls, smstr):
       names = ("Summer", "Fall", "Spring")
       ans = None
       for i in range(len(names)):
           if smstr.split()[0] == names[i]:
               ans = f"{i}{smstr[-2:]}"
               break
       return ans


   def get_email(self, person):
       return f"{person.id}@{person.dept}.uiu.ac.bd"
   def display(self, obj):
       print(obj)


class Course:
   courses = dict()
   def __new__(cls, code, name, dept, credit):
       if code not in cls.courses:
           course = super().__new__(cls)
           cls.courses[code] = course
       return cls.courses[code]


   def __init__(self, code, name, dept, credit):
       try:
           if self.code == code:
               return
       except AttributeError:
           self.code = code
           self.name = name
           self.dept = dept
           self.students = []
           self.faculty = None
           self.credit = credit


   def __repr__(self):
       return f"[{self.code}: {self.name}: {self.credit} credits]"


u = Utility("Spring 25")

c1 = Course("C101", "Intro to Programming", "cse", 3)
c2 = Course("C102", "OOP Fundamentals", "ds", 3)
c3 = Course("C103", "Data Structures", "cse", 3)
c4 = Course("C104", "Algorithm Basics", "cse", 3)
c5 = Course("C105", "Algorithm Basics Lab", "ds", 1)

f1 = u.recruit_faculty("A", "a@gmail.com", "cse")
f2 = u.recruit_faculty("B", "b@gmail.com", "ds")
try:
    u.assign_faculty(c4, f2)
except AssignmentError:
    pass

u.assign_faculty(c1, f1)
u.assign_faculty(c5, f2)

try:
    u.assign_faculty(c3, f2)
except AssignmentError:
    pass

s1 = u.admit_student("Faria Afreen", "faria@gmail.com", "ds")
s2 = u.admit_student("Zinia Amin", "zinia@gmail.com", "cse")

try:
    u.add_grade(s2, c1, 4.5)
except GradeError:
    pass

u.enroll_student(s1, c2)
u.enroll_student(s2, c2)

try:
    u.enroll_student(s1, c2)
except EnrollmentError:
    pass

try:
    u.add_grade(s1, c2, 3.9)
except GradeError:
    pass

u.add_grade(s1, c2, 4.0)
u.enroll_student(s1, c1)
u.add_grade(s1, c1, 3.0)

u.enroll_student(s1, c3)
u.enroll_student(s1, c4)

try:
    u.enroll_student(s1, c5)
except EnrollmentError:
    pass

u.enroll_student(s2, c3)
u.add_grade(s2, c3, 4.0)
u.enroll_student(s2, c1)

try:
    u.enroll_student(s2, c2)
except EnrollmentError:
    pass

