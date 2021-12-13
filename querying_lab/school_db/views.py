from django.shortcuts import render
from .models import Student, Instructor, Course, StudentCourse


def index(request):
    students = Student.objects.all()

    # The following line creates a list that allows you to examine the data 
    # from a Queryset in an easier to visualize way
    # It is not required for functionality!
    # Place a breakpoint on line 14, then compare 'students' and 'data_visualization'
    data_visualization = [item for item in students]

    context = {
        'students': students
    }
    return render(request, 'school/index.html', context)

def problem_one(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    students = Student.objects.filter(gpa__gt=3.0).order_by("-gpa")

    context = {
        'students': students
    }
    return render(request, 'school/one.html', context)

def problem_two(request):
    # Find all instructors hired prior to 2010
    # Order by hire date
    instructors = Instructor.objects.filter(hire_date__range=["1901-01-01", "2009-12-31"])

    context = {
        'instructors': instructors
    }
    return render(request, 'school/two.html', context)

def problem_three(request):
    # Find all students who have a A+ in any class and are NOT getting a C+ in any class. 
    # Order the data by student's first name alphabetically.

    # student_courses = StudentCourse.objects.filter(course_id = 4).filter(grade = "A")
    
    student_courses = StudentCourse.objects.filter(grade = "A+").exclude(student__studentcourse__grade = "C+").order_by("student__first_name")
    data_visualization = [item for item in student_courses]

    context = {
        'student_courses': student_courses
    }
    return render(request, 'school/three.html', context)

def problem_four(request):
    # Find all students who are taking the Programming class. 
    # Order by their grade. 
    student_courses = StudentCourse.objects.filter(course__name = "Programming").order_by("grade")
    data_visualization = [item for item in student_courses]

    context = {
        'student_courses': student_courses
    }
    return render(request, 'school/four.html', context)

def problem_five(request):
    # Find all students getting an A in the Programming class. 
    # Order by last name.
    student_courses = StudentCourse.objects.filter(course__name = "Programming").filter(grade = "A")

    context = {
        'student_courses': student_courses
    }
    return render(request, 'school/five.html', context)

def problem_six(request):
    # Find all students with a GPA less than 3.0 who are getting an A in Programming class.
    # Order by GPA.
    # student_courses = StudentCourse.objects.filter(grade = "A+").exclude(student__studentcourse__grade = "C+").order_by("student__first_name")

    student_courses = Student.objects.filter(gpa__lt=3.0).filter(studentcourse__course__name = "Programming").filter(studentcourse__grade = "A").order_by("gpa")
    #students = Student.objects.filter(gpa__gt=3.0).order_by("-gpa")

    context = {
        'students': student_courses
    }

    return render(request, 'school/six.html', context)

################## BONUS #################
# These problems will require using Aggregate functions along with annotate()
# https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate

# Create a view function and template for each bonus problem you complete

# BONUS ONE
# Write a query to find any instructors who are only teaching one single course. Display the instructor and the course

def bonus_one(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    students = Student.objects.filter(gpa__gt=3.0).order_by("-gpa")

    context = {
        'students': students
    }
    return render(request, 'school/one.html', context)

# BONUS TWO
# Display all students along with the number of credits they are taking

def bonus_two(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    students = Student.objects.filter(gpa__gt=3.0).order_by("-gpa")

    context = {
        'students': students
    }
    return render(request, 'school/one.html', context)

# BONUS THREE
# Find all students who are getting an A in any course and average their GPAs. Display the number of students and their Average GPA

def bonus_three(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    students = Student.objects.filter(gpa__gt=3.0).order_by("-gpa")

    context = {
        'students': students
    }
    return render(request, 'school/one.html', context)

# BONUS FOUR
# Write a function that will replace student GPAs in the database with an accurate score based only on their current grades
# This may require multiple queries
# See https://www.indeed.com/career-advice/career-development/gpa-scale for a chart of what point value each grade is worth

def bonus_four(request):
    # Find all students who have a GPA greater than 3.0. 
    # Order the data by highest GPAs first.
    students = Student.objects.filter(gpa__gt=3.0).order_by("-gpa")

    context = {
        'students': students
    }
    return render(request, 'school/one.html', context)