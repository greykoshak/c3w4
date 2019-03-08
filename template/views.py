from django.shortcuts import render


def echo(request):
    return render(request, 'echo.html', context={
        'get_letter': request.META['QUERY_STRING'][0],
        'get_value': request.GET.get(request.META['QUERY_STRING'][0]),
        'get_tag': request.META.get('HTTP_X_PRINT_STATEMENT'),
        'request_method': request.META['REQUEST_METHOD'].lower()
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
