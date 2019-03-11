from django.shortcuts import render

import db.query


# Create your views here.

def db_view(request):
    my_lines = []
    result = db.query.get_user_with_limit()
    my_lines.append("Ready")
    return render(request, 'db_view.html', context={'my_lines': my_lines, 'rec': result})
