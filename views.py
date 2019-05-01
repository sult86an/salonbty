from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import ServicesForm, UpdateServicesForm, ArtistsForm, UpdateArtistsForm,  ProfileForm, OServicesForm,\
    OUpdateServicesForm, OrdersForm

from .models import Orders, Artists, Services, Member, Salons, Hotel, Offers
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse


def home(request):
    a = []
    salon_name = Salons.objects.filter(salon_id=request.user.id)
    new_order = Orders.objects.filter(salon=request.user.id, answer=False,  done=False)
    tasks = Orders.objects.filter(salon=request.user.id, done=False)
    revenue = Orders.objects.filter(salon=request.user.id, done=True)
    ssr = Orders.objects.all().annotate(total=Sum('services__price'))

    context= {
        'salon_name': salon_name,
        'new_order': new_order,
        'tasks': tasks,
        'sr': revenue,
        }
    return render(request, 'home.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class NewOrders(generic.ListView):
    template_name = 'salonbty/new-orders.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Orders.objects.filter(salon=self.request.user.id, answer=False)


class Approval(generic.UpdateView):
    model = Orders
    fields = ['approval', 'answer']
    success_url = reverse_lazy('new_orders')
    template_name = 'salonbty/new-orders.html'


class TodayTasks(generic.ListView):
    template_name = 'salonbty/today_tasks.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Orders.objects.filter(salon=self.request.user.id, done=False)


class IsDone(generic.UpdateView):
    model = Orders
    fields = ['done', 'salon_charge', 'final_price', 'approval', 'answer']
    success_url = reverse_lazy('today_tasks')
    template_name = 'salonbty/today_tasks.html'


class CompletedOrders(generic.ListView):
    template_name = 'salonbty/completed_order.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Orders.objects.filter(salon=self.request.user.id, done=True)


class CanceledOrders(generic.ListView):
    template_name = 'salonbty/canceled.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Orders.objects.filter(salon=self.request.user.id, answer=True, approval=2)


class Finance(generic.ListView):
    template_name = 'salonbty/finance.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Orders.objects.filter(salon=self.request.user.id, done=True)


def serv(request):
    if request.method == "POST":
        form = ServicesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/services/show/')
            except:
                pass
    else:
        form = ServicesForm()
    return render(request, 'salonbty/services/services_index.html', {'form': form})


def show(request):
    services = Services.objects.filter(salon=request.user.id)
    return render(request, "salonbty/services/show.html", {'services': services})


def edit(request, id):
    services = Services.objects.get(id=id)
    return render(request, 'salonbty/services/edit.html', {'services': services})


def update(request, id):
    service = Services.objects.get(id=id)
    form = UpdateServicesForm(request.POST, instance=service)
    if form.is_valid():
        form.save()
        return redirect('/services/show/')
    return render(request, 'salonbty/services/edit.html', {'service': service})


def destroy(request, id):
    services = Services.objects.get(id=id)
    services.delete()
    return redirect('/services/show/')


#offers


def o_serv(request):
    if request.method == "POST":
        form = OServicesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/services/show/')
            except:
                pass
    else:
        form = OServicesForm()
    return render(request, 'salonbty/o_services/services_index.html', {'form': form})


def o_show(request):
    services = Offers.objects.filter(service__artists__salon=request.user.id)
    return render(request, "salonbty/o_services/show.html", {'services': services})


def o_edit(request, id):
    services = Offers.objects.get(id=id)
    return render(request, 'salonbty/o_services/edit.html', {'services': services})


def o_update(request, id):
    service = Offers.objects.get(id=id)
    form = OUpdateServicesForm(request.POST, instance=service)
    if form.is_valid():
        form.save()
        return redirect('/o_services/show/')
    return render(request, 'salonbty/o_services/edit.html', {'service': service})


def o_destroy(request, id):
    services = Offers.objects.get(id=id)
    services.delete()
    return redirect('/o_services/show/')



# Artists Sections

def arts(request):
    services = Services.objects.filter(salon=request.user.id)
    if request.method == "POST":
        form = ArtistsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/artists/show/')
            except:
                pass
    else:
        form = ArtistsForm()
    return render(request, 'salonbty/artists/artists_index.html', {'form': form, 'services': services})


def arts_show(request):
    form = ArtistsForm
    artists = Artists.objects.filter(salon=request.user.id)
    return render(request, "salonbty/artists/show.html", {'artists': artists, 'form': form})


def arts_edit(request, id):
    artists = Artists.objects.get(id=id)
    return render(request, 'salonbty/artists/edit.html', {'artists': artists})


def arts_update(request, id):
    services = Services.objects.filter(salon=request.user.id)
    artist = Artists.objects.get(id=id)
    form = UpdateArtistsForm(request.POST, instance=artist)
    if form.is_valid():
        form.save()
        return redirect('/artists/show/')
    return render(request, 'salonbty/artists/edit.html', {'artist': artist, 'services': services, 'form': form})


def add_orders(request):
    services = Services.objects.filter(salon=request.user.id)
    artists = Artists.objects.filter(salon=request.user.id)
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/today_tasks/')
            except:
                pass
    else:
        form = OrdersForm()
    return render(request, 'salonbty/orders/add.html', {'form': form, 'services': services, 'artists': artists})


# class ArtistUpdate(generic.UpdateView):
#     model = Artists
#     form_class = UpdateArtistsForm
#     template_name = 'salonbty/artists/edit.html'
#     success_url = reverse_lazy('arts_show')


def arts_destroy(request, id):
    artist = Artists.objects.get(id=id)
    artist.delete()
    return redirect('/artists/show/')


# Artist Tasks
# def arts_tasks(request):
#     artists = ArtistServices.objects.filter(salon=request.user.id, )
#     return render(request, "salonbty/artists/tasks.html", {'artists': artists})
#
#
# def add_tasks(request):
#     services = Services.objects.filter(salon=request.user.id)
#     artists = Artists.objects.filter(salon=request.user.id)
#
#     if request.method == "POST":
#         form = TasksForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/artists/tasks/')
#             except:
#                 pass
#     else:
#         form = TasksForm()
#     return render(request, 'salonbty/artists/add_tasks.html', {'form': form, 'services': services, 'artists': artists})
#
#
# def tasks_update(request, id):
#     tasks = ArtistServices.objects.get(id=id)
#     form = UpdateTasksForm(request.POST, instance=tasks)
#     if form.is_valid():
#         form.save()
#         return redirect('/tasks/show/')
#     return render(request, 'salonbty/artists/tasks_edit.html', {'tasks': tasks})


# Calendar
def calendar(request):
    orders = Orders.objects.filter(salon=request.user.id)
    return render(request, "salonbty/calendar/calendar.html", {'orders': orders})


# # salons profile
# def salons_profile(request):
#     return render(request, 'salonbty/salons_info/salons_info.html')


class ViewProfile(generic.ListView):
    model = Salons
    template_name = 'salonbty/salons_info/salons_info.html'
    context_object_name = 'salons'

    def get_queryset(self):
        user = self.request.user.id
        return Salons.objects.filter(salon_id=user)


class Profile(generic.CreateView):
    model = Salons
    fields = ["salon_id", "salon", "mobile", "country", "city", "district", "address", "lat", "lng", "iban", "bank", "logo"]
    success_url = reverse_lazy('profile')
    template_name = 'salonbty/salons_info/salons_info.html'


class UpdateProfile(generic.UpdateView):
    model = Salons
    fields = ["salon", "mobile",  "country", "city", "district", "address", "lat", "lng", "iban", "bank", "logo"]
    template_name = 'salonbty/salons_info/salons_info.html'
    success_url = reverse_lazy('profile')


# -----------------------


# # Create your views here.
# def hotel_image_view(request):
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = HotelForm()
#     return render(request, 'salonbty/img_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')


class ViewImage(generic.ListView):
    model = Hotel
    template_name = 'salonbty/display_hotel_images.html'
    context_object_name = 'hotel_images'

    def get_queryset(self):
        return Hotel.objects.all()


# Calendar
def map(request):
    return render(request, 'salonbty/map.html')
