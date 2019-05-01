from django import forms
from .models import Services, Artists, Hotel, Salons, Offers, Orders


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['salon', 'name', 'price', 'minTime']


class UpdateServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'price', 'minTime']


class OServicesForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['service', 'offer_price']


class OUpdateServicesForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['service', 'offer_price']


class ArtistsForm(forms.ModelForm):

    class Meta:
        model = Artists
        fields = ['salon', 'name', 'service', 'nationality', 'weekend_days']


class UpdateArtistsForm(forms.ModelForm):

    class Meta:
        model = Artists
        fields = ['name', 'service', 'nationality', 'weekend_days']


class OrdersForm(forms.ModelForm):
    time = forms.ChoiceField(
        choices=(
            ('01:00 am', '01:00 am'),
            ('02:00 am', '02:00 am'),
            ('03:00 am', '03:00 am'),
            ('04:00 am', '04:00 am'),
            ('05:00 am', '05:00 am'),
            ('06:00 am', '06:00 am'),
            ('07:00 am', '07:00 am'),
            ('08:00 am', '08:00 am'),
            ('09:00 am', '09:00 am'),
            ('10:00 am', '10:00 am'),
            ('11:00 am', '11:00 am'),
            ('12:00 pm', '12:00 pm'),
            ('01:00 pm', '01:00 pm'),
            ('02:00 pm', '02:00 pm'),
            ('03:00 pm', '03:00 pm'),
            ('04:00 pm', '04:00 pm'),
            ('05:00 PM', '05:00 PM'),
            ('06:00 PM', '06:00 PM'),
            ('07:00 PM', '07:00 PM'),
            ('08:00 PM', '08:00 PM'),
            ('09:00 PM', '09:00 PM'),
            ('10:00 PM', '10:00 PM'),
            ('11:00 PM', '11:00 PM'),
            ('12:00 PM', '12:00 PM'),
        )
    )

    class Meta:
        model = Orders
        fields = ['salon', 'artist', 'services', 'customer', 'date', 'time', 'approval', 'answer', 'done']


# class TasksForm(forms.ModelForm):
#     class Meta:
#         model = ArtistServices
#         fields = ['salon', 'artist', ]
#
#
# class UpdateTasksForm(forms.ModelForm):
#     class Meta:
#         model = ArtistServices
#         fields = ['artist', 'service']




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Salons
        fields = ["salon", "mobile",  "country", "city", "district", "address", "lat", "lng", "iban", "bank", "logo", "salon_id"]


