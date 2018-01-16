from datetime import datetime
from .models import *
from my_app.registration import *
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import View, ListView
from my_app.forms import RegistrForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.



# Create your views here.


class OrdersView(View):
    def get(self, request):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', locals())


class OrderView(View):
    def get(self, request, id):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', locals())


def main(request):
    return render(request, 'main.html', locals())


def db(request):
    return render(request, 'db.html', locals())


class BookView(ListView):
    model = Book
    template_name = 'books.html'


class WriterView(ListView):
    model = Writer
    template_name = 'writer.html'


def phone_info(request, id):
    name = ['Факультет ИУ', 'iPhone 8', 'iPhone X']
    ip7_info = 'Ведущий факультет по подготовке кадров в области разработки программного обеспечения, электронной и микросистемной техники для предприятий ракетно-космической отрасли, государственных служб и частных компаний.'
    ip8_info = 'Факультет был создан приказом министров высшего и среднего специального образования и радиопромышленности в мае 1956 года как филиал вечернего факультета училища по подготовке инженеров для предприятия радиопромышленности.  '
    ipX_info = ' Факультет включает 10 специализированных кафедр и проводит подготовку высококвалифицированных инженеров исследователей и разработчиков для передовых научно - исследовательских институтов, институтов Российской Академии наук, конструкторских бюро и научно - производственных объединений, занимающихся прогнозированием развития, разработкой, моделированием и созданием новых типов экологически чистых ракетно - космических двигателей и установок, энергетических систем, нетрадиционных источников энергии, поршневых и газотурбинных транспортных двигателей, систем криогеники и кондиционирования, вакуумного оборудования и пневмоавтоматики, физико - энергетических и плазменных энергетических установок, гидромашин, гидроприводов и гидропневмоавтоматики, комбинированных экобиозащитных систем.'
    BMT_info = 'Единственный в стране факультет «Биомедицинская техника» основан в 1998 году и осуществляет подготовку инженеров по двум специальностям: «Биотехнические системы и устройства» (19.05)   «Инженерное дело в медико-биологической практике» (19.06) '
    info = [ip7_info, ip8_info, ipX_info, BMT_info]
    data1 = {'phone': {'id': id}}
    data2 = {'phones': [{'id': '1', 'phone_name': 'Факультет ИУ', 'info': ip7_info},
                        {'id': '2', 'phone_name': 'Факультет РТ', 'info': ip8_info},
                        {'id': '3', 'phone_name': 'Факультет Э', 'info': ipX_info},
                        {'id': '4', 'phone_name': 'Факультет БМТ', 'info': BMT_info}]}
    return render(request, 'phone_info.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success/')
        else:
            error = "Попробуй ещё раз"
    return render(request, 'login.html', locals())


def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


@login_required()
def success(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'success.html', locals())


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            return HttpResponseRedirect('/login/')
    return render(request, 'registration2.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')


class TeacherIUView(ListView):
    model = teacherIU
    template_name = 'IU.html'


class TeacherSMView(ListView):
    model = teacherSM
    template_name = 'SM.html'


class TeacherBMTView(ListView):
    model = teacherBMT
    template_name = 'BMT.html'

class TeacherRTView(ListView):
    model = teacherRT
    template_name = 'RT.html'


class Teachers(ListView):
    model = teachers
    template_name = 'teachers.html'

class Groups(ListView):
    model = groups
    template_name = 'groups.html'


def related_json_nomers(request, hotel_name):
    current_hotel = groups.objects.get(hotell=hotel_name)
    hotell = students.objects.all().filter(hotel_name=current_hotel)
    json_nomers = serializers.serialize("json", hotell)
    return HttpResponse(json_nomers, content_type="application/javascript")


def all_json_registrs(request):
    registr = groups.objects.all()
    json_hotels = serializers.serialize("json", registr, use_natural_foreign_keys=True, use_natural_primary_keys=True)
    return HttpResponse(json_hotels, content_type="application/javascript")


def registr(request, course_id):
    groups.objects.get(id_groups=course_id)
    if request.method == 'POST':
        groups.objects.get(id_groups=course_id)
    model = groups
    return render(request, "ticket.html", {'course': groups.objects.get(id_groups=course_id)},  locals())



class RegistrsList(ListView):
    form_class = RegistrForm
    model = groups
    template_name = "tickets.html"
    paginate_by = 2
    nomera = students.objects.all()
    human = teachers.objects.all()
    context = {"form": form_class, "nomera": nomera, "human": human}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nomera'] = students.objects.all()
        return context


    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('course_url', args=(instance.pk,)))
        return render(request, self.template_name, {'form': form})


def course_add(request):
    nomera = students.objects.all()
    form = RegistrForm(request.POST or None, request.FILES or None)
    context = {"form": form, "nomera": nomera}
    print(form.errors)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('course_url', args=(instance.pk, )))
    return render(request, "ticket_element.html", context)

class hotelsview(View):
    def get(self, request):
        nomera = students.objects.all()
        human = teachers.objects.all()
        form = RegistrForm(request.POST or None, request.FILES or None)
        context = {"form": form, "nomera": nomera, "human": human}
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('course_url', args=(instance.pk,)))
        return render(request, "ticket.html", context)


