from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from .models import Student

# Create your views here.
def index(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Grade Book</title></head>
        <link rel="stylesheet" href="/static/grades/css/style.css" />
    </head>
    <body>
        <header>
            A Grade Book
        </header>
        <nav>
            <ul>
                <li><a href="/index/">Home</a></li>
                <li><a href="/grades/">View All Grades</a></li>
                <li><a href="/addgrade/">Add New Grade</a></li>
            </ul>
        </nav>
        <div id="main" style="height:300px;">
            <h1>Welcome to A Grade Book</h1>
            <p> Some paragraphs... </p>
        </div>
       	<footer>
			<a href="/index/">Home</a> | <a href="/about/">About</a> | <a href="/contact/">Contact </a>|
			<div id="copy">
			&copy; 2016 Ram Basnet
			</div>
		</footer>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    #print(request)
    data = {'heading': 'About',
            'content': 'Demo program developed using django framework.'
            }
    return render(request, 'grades/index.html', data)

def showGrades(request):
    html = """
        <table>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Test 1</th>
                <th>Test 2</th>
                <th>Test 3</th>
                <th>Average </th>
                <th colspan="2">Tools</th>
            </tr>
        """
    for student in Student.objects.all():
        student.findAverage()
        student.save()
        html += """<tr>
                    <td>{0}</td>
                    <td>{1}</td>
                    <td>{2}</td>
                    <td>{3}</td>
                    <td>{4}</td>
                    <td>{5:.2f}</td>
                    <td><a href="{6}">Edit</a></td>
                    <td><a href="{7}">Delete</a></td>
                    </tr>
                """.format(student.first_name, student.last_name, student.test1,
                           student.test2, student.test3, student.avg,
                           reverse('grade', args=(student.id,)),
                           reverse('delete', args=(student.id,)))

    html += "</table>"
    return HttpResponse(html)

def allGrades(request):
    students = Student.objects.order_by("-avg")
    data = ""
    for student in students:
        data += str(student.id) + "  " + student.first_name + "  " + str(student.avg) + "<br>"

    return HttpResponse(data)

def showGradesUsingTemplate(request):
    students = Student.objects.all()
    for student in students:
        student.findAverage()
        student.save()

    context = {'heading': "All Students' Grades",
               'students_list': students,
               }
    return render(request, 'grades/grades.html', context)

def saveGrade(request, student_id=None):
    errors = []
    if request.method == 'POST':
        # handle data posted from the from
        if not request.POST.get('first_name', ''):
            errors.append('Enter first name.')
        if not request.POST.get('last_name'):
            errors.append('Enter last name.')
        if not request.POST.get('test1', ''):
            errors.append('Enter Test 1')
        if not request.POST.get('test2', ''):
            errors.append('Enter Test 2')
        if not request.POST.get('test3', ''):
            errors.append('Enter Test 3')

        data = {'heading': 'Thank You!',
                'content': 'Your data has been saved!',
                'errors': errors,
            }
        if errors:
            data['heading'] = 'Add New Student Grade'
            data['content'] = 'Fill in the following information:'
            return render(request, 'grades/edit_grade.html', data)
        else:
            if student_id:
                student = Student.objects.get(pk=student_id)
            else:
                student = Student()
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.test1 = float(request.POST.get('test1'))
            student.test2 = float(request.POST.get('test2'))
            student.test3 = float(request.POST.get('test3'))
            student.findAverage()
            student.save()
            data['heading'] = 'Success'
            data['content'] = 'Student Grade updated successfully!'
            data['student'] = student
            return render(request, 'grades/edit_grade.html', data)
    else:
        if not student_id:
            # must be a get method to enter new grade info so render the form for user to enter
            # data
            data = {
                'heading': 'Add New Student Grade',
                'content': 'Fill in the following information',
                'errors': errors,
            }
        else:
            # edit existing student
            student = Student.objects.get(pk=student_id)
            #student = get_object_or_404(Student, pk=student_id)
            data = {
                'heading': 'Edit Student Grade',
                'content': 'Update the following information',
                'errors': errors,
                'student':student,
            }

        return render(request, 'grades/edit_grade.html', data)

def deleteGrade(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return showGrades(request)

