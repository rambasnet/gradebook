from django.shortcuts import render
from django.http import HttpResponse

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
                <li><a href="/view_grades/">Viw All Grades</a></li>
                <li><a href="/add_new/">Add New Grade</a></li>
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

def save_grade(request):
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
        # must be a get method so render the form so user can enter
        # data
        data = {
            'heading': 'Add New Student Grade',
            'content': 'Fill in the following information',
            'errors': errors,
        }
        return render(request, 'grades/edit_grade.html', data)