from django.shortcuts import render

# Create your views here.


def balance(request):
    context = {}
    template = 'website/balance.html'
    return render(request, template, context)
    # return HttpResponse('home')

def bill(request):
    context = {}
    template = 'website/bill.html'
    return render(request, template, context)
    # return HttpResponse('home')

def create_invoice(request):
    context = {}
    template = 'website/create-invoice.html'
    return render(request, template, context)
    # return HttpResponse('home')

def index(request):
    context = {}
    template = 'website/index.html'
    return render(request, template, context)
    # return HttpResponse('home')

def invoice(request):
    context = {}
    template = 'website/invoice.html'
    return render(request, template, context)
    # return HttpResponse('home')

def lock(request):
    context = {}
    template = 'website/lock.html'
    return render(request, template, context)
    # return HttpResponse('home')

def notification(request):
    context = {}
    template = 'website/notification.html'
    return render(request, template, context)
    # return HttpResponse('home')

def otp(request):
    context = {}
    template = 'website/opt.html'
    return render(request, template, context)
    # return HttpResponse('home')

def profile(request):
    context = {}
    template = 'website/profile.html'
    return render(request, template, context)
    # return HttpResponse('home')

def reset(request):
    context = {}
    template = 'website/reset.html'
    return render(request, template, context)
    # return HttpResponse('home')

def settings_activity(request):
    context = {}
    template = 'website/settings-activity.html'
    return render(request, template, context)
    # return HttpResponse('home')

def settings_api(request):
    context = {}
    template = 'website/settings-api.html'
    return render(request, template, context)
    # return HttpResponse('home')

def settings_application(request):
    context = {}
    template = 'website/settings-application.html'
    return render(request, template, context)
    # return HttpResponse('home')

def settings_payment_method(request):
    context = {}
    template = 'website/settings-payment-method.html'
    return render(request, template, context)
    # return HttpResponse('home')

def settings_profile(request):
    context = {}
    template = 'website/settings-profile.html'
    return render(request, template, context)
    # return HttpResponse('home')

def settings_security(request):
    context = {}
    template = 'website/settings-security.html'
    return render(request, template, context)
    # return HttpResponse('home')

def signin(request):
    context = {}
    template = 'website/signin.html'
    return render(request, template, context)
    # return HttpResponse('home')

def signup(request):
    context = {}
    template = 'website/signup.html'
    return render(request, template, context)
    # return HttpResponse('home')

def home(request):
    context = {}
    template = 'website/index.html'
    return render(request, template, context)
    # return HttpResponse('home')

def dashboard(request):
    context = {}
    template = 'website/index-2.html'
    return render(request, template, context)
    # return HttpResponse('home')

