from django.shortcuts import render
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
                <li><a href="/grades/">Viw All Grades</a></li>
                <li><a href="/addgrade/">Add New Grade</a></li>
            </ul>
        </nav>
        <div id="main" style="height:300px;">
            <h1>Welcome to A Grade Book</h1>
            <p> Some paragraph... </p>
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
                <th colspan="2">Tools<th>
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
                    </tr>
                """.format(student.first_name, student.last_name, student.test1,
                           student.test2, student.test3, student.avg, reverse('grade', args=(student.id,)))

    html += "</table>"
    return HttpResponse(html)

def saveGrade(request, student_id=None):
    errors = []
    if request.method == 'POST':
        # handle data posted from the from
        if not request.POST.get('first_name', ''):
            errors.append('Enter first name.')
        if not request.POST.get('last_name'):
            errors.append('Enter last name.')
        if not request.POST.get('grade1', ''):
            errors.append('Enter Grade 1')
        if not request.POST.get('grade2', ''):
            errors.append('Enter Grade 2')
        if not request.POST.get('grade3', ''):
            errors.append('Enter Grade 3')

        data = {'heading': 'Thank You!',
                'content': 'Your data has been saved!',
                'errors': errors,
            }
        if errors:
            data['heading'] = 'Add New Student Grade'
            data['content'] = 'Fill in the following information:'
            return render(request, 'grades/edit_grade.html', data)
        else:
            return render(request, 'grades/index.html', data)
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
            data = {
                'heading': 'Edit Student Grade',
                'content': 'Update the following information',
                'errors': errors,
                'student':student,
            }

        return render(request, 'grades/edit_grade.html', data)