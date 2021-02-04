from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:      # user is already login ==> authenticated user 
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs) # user is without login ==> unauthenticated user   

    return wrapper_func 

def allowed_users(allowed_roles=[]):
    def decorator(view_func):  
        def wrapper_func(request, *args, **kwargs):
            group = None 
            users = request.user.groups     # it will return queryset of all users
            if users.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs) 
            else:
                return HttpResponse('You are Not an authorized to see this page')     
        return wrapper_func
    return decorator                   


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func

        