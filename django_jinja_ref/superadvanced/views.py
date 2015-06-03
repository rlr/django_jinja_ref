from django.shortcuts import render


def django(request):
    """A view that renders a django template."""
    return render(
        request,
        'superadvanced/django.html',
        {'title': 'This is a Django template #superadvanced'})


def jinja(request):
    """A view that renders a jinja template."""
    return render(
        request,
        'superadvanced/jinja.html',
        {'title': 'This is a Jinja2 template #superadvanced'})
