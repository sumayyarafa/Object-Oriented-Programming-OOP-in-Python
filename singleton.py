class Course:
    code_to_course_map = dict()
    def __new__(cls, name, code, faculty_list):
        if code not in Course.code_to_course_map.keys():
            course = super().__new__(cls)
            Course.code_to_course_map[code] = course
            return course
        else:
            return Course.code_to_course_map[code]


    def __init__(self, name, code, faculty_list):
        self.name = name
        self.code = code
        self.faculty_list = faculty_list

c = Course("OOP", "1115", [])
d = Course("OOP", "1115", [])
e = Course("ENG", "0005", [])

c.faculty_list.append("Amina")
print(d.faculty_list)



class Course:
    course_list = dict()
    def __new__(cls, course_name, course_code):
        if course_code not in cls.course_list.keys():
            course = super().__new__(cls)
            cls.course_list[course_code] = course
            return cls.course_list[course_code]
        else:
            return cls.course_list[course_code]

    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.faculty_list = []

c1 = Course("OOP", "1115")
c2 = Course("DBMS", "2225")
c3 = Course("OOP", "1115")

c1.faculty_list= ["Amina", "Abedin"]

print(c3.faculty_list)



class VC:
    vc_object = None
    def __new__(cls, name):
        if cls.vc_object is None:
            cls.vc_object = super().__new__(cls)
        return cls.vc_object

    def __init__(self, name):
        self.name = name

v1 = VC("Abdul Hamid")


print(type(v1))

















