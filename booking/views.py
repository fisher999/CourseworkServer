from booking.Classes.UserManager import UserManager
from django.shortcuts import render
from booking.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseForbidden,HttpResponse
import json, base64
from booking.Classes.HotelManager import HotelManager
from booking.Classes.ApartmentsManager import ApartmentsManager
from booking.Classes.FeedbackManager import FeedbackManager




def register(request):
    userManager = UserManager()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            login = form.cleaned_data['login']
            password = form.cleaned_data['password']

            if 'login' in request.POST:
                for user in userManager.allUsers():
                    if user.name == login  and user.password == password:
                        return HttpResponseRedirect('/mainpage/')

            return HttpResponseRedirect('')

    else:
        form = RegisterForm()
        return render(request, 'booking/RegisterPage.html', {'form': form})

def main_page(request):
    return render(request, 'booking/MainPage.html')

def login(request):
    login_failed = False
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        username=body['username']
        password=body['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
            else:
                return HttpResponseForbidden(\
                    content='Your account is not active.')
        else:
            login_failed = True

    if request.user.is_authenticated:
        status = 200
    else:
        status = 401
        login_failed = True

    res = {}

    res['status'] = status
    if login_failed:
        res['Auth-Response'] = 'Login failed'
    else:
        basic_auth = ':'.join([username,password])

        res['token'] = base64.b64encode(basic_auth.encode()).decode()
        res['Auth-Response'] = 'Login success'

    response = json.dumps(res)

    answer = HttpResponse(response)
    print(answer)

    return answer

def getHotels(request):
    if UserManager.didAuth(request)[0]:
        json = HotelManager.getHotelsJson()
        return HttpResponse(json)
    else:
        return HttpResponseForbidden( \
            content='Your account is not active.')

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Not auth'
    return response

def getHotelsAtPage(request):
    if UserManager.didAuth(request)[0]:
        path = request.path
        json = HotelManager.getHotelsJsonAtPage()

def getApartmentsForId(request,hotel_id):
    (didAuth, user) = UserManager.didAuth(request)
    if didAuth:
        id = hotel_id
        json = ApartmentsManager.getApartmentsJsonAtHotelId(id)
        return HttpResponse(json)
    else:
        return HttpResponseForbidden(content='Your account is not active.')

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Not auth'
    return response

def feedbacksForHotelId(request, hotel_id):
    (didAuth, user) = UserManager.didAuth(request)
    if didAuth:
        if request.method == 'GET':
            jsonObject = FeedbackManager.getFeedbacks(hotel_id, user)
            return HttpResponse(jsonObject)
        elif request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            json_object = FeedbackManager.postFeedback(user, hotel_id, body)
            return  HttpResponse(json_object)
    else:
        return HttpResponseForbidden(content='Your account is not active.')

    response = HttpResponse()
    response.status_code = 401
    response['WWW-Authenticate'] = 'Not auth'

    return response


