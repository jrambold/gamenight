from events.forms import LoginForm

def login_form(request):
    return {
         'login_form' : LoginForm()
    }
