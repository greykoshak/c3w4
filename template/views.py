from django.shortcuts import render


# from django.utils.http import urlencode


def echo(request):
    get_letter, get_value = list(), list()

    if request.method == 'GET':
        get_letter = [key for key in request.GET]
        get_value = [request.GET[key] for key in request.GET]
    elif request.method == 'POST':
        get_letter = [key for key in request.POST]
        get_value = [request.POST[key] for key in request.POST]

    return render(request, 'echo.html', context={
        'get_letter': get_letter[0] if len(get_letter) > 0 else "",
        'get_value': get_value[0] if len(get_value) > 0 else "",
        'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
        'request_method': request.method.lower() if len(get_letter) > 0 else "",
        'colon': ':' if len(get_letter) > 0 else ""
    }, status=200)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
