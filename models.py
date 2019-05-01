from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from multiselectfield import MultiSelectField


class Days(models.Model):
    ALL_DAYS = (
        (1, 'الأحد'),
        (2, 'الاثنين'),
        (3, 'الثلاثاء'),
        (4, 'الأربعاء'),
        (5, 'الخميس'),
        (6, 'الجمعة'),
        (7, 'السبت'),
    )

    day = models.PositiveSmallIntegerField(choices=ALL_DAYS, blank=True, null=True)

    class Meta:
        ordering = ('day',)

    def __str__(self):
        return self.get_day_display()


class Hours(models.Model):
    A_ONE = 1
    A_TWO = 2
    A_THREE = 3
    A_FOUR = 4
    A_FIVE = 5
    A_SIX = 6
    A_SEVEN = 7
    A_EIGHT = 8
    A_NINE = 9
    A_TEN = 10
    A_ELEVEN = 11
    P_TWELVE = 12
    P_ONE = 13
    P_TWO = 14
    P_THREE = 15
    P_FOUR = 16
    P_FIVE = 17
    P_SIX = 18
    P_SEVEN = 19
    P_EIGHT = 20
    P_NINE = 21
    P_TEN = 22
    P_ELEVEN = 23
    A_TWELVE = 24
    HOURS = (
        (A_ONE, '01:00 am'),
        (A_TWO, '02:00 am'),
        (A_THREE, '03:00 am'),
        (A_FOUR,  '04:00 am'),
        (A_FIVE, '05:00 am'),
        (A_SIX, '06:00 am'),
        (A_SEVEN, '07:00 am'),
        (A_EIGHT, '08:00 am'),
        (A_NINE, '09:00 am'),
        (A_TEN, '10:00 am'),
        (A_ELEVEN, '11:00 am'),
        (P_TWELVE, '12:00 pm'),
        (P_ONE, '01:00 pm'),
        (P_TWO, '02:00 pm'),
        (P_THREE, '03:00 pm'),
        (P_FOUR, '04:00 pm'),
        (P_FIVE, '05:00 PM'),
        (P_SIX, '06:00 PM'),
        (P_SEVEN, '07:00 PM'),
        (P_EIGHT, '08:00 PM'),
        (P_NINE, '09:00 PM'),
        (P_TEN, '10:00 PM'),
        (P_ELEVEN, '11:00 PM'),
        (A_TWELVE, '12:00 PM'),
    )
    hour = models.PositiveSmallIntegerField(choices=HOURS, blank=True, null=True)

    class Meta:
        ordering = ('hour',)

    def __str__(self):
        return self.get_hour_display()


class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Salons(models.Model):

    SAB = 1
    SAMBA = 2
    INMA = 3
    RAJIHI = 4
    RIYAD = 5
    AWWAL = 6
    SAFARANSI = 7
    ISTITHMAR = 8
    ARABI = 9
    BILAD = 10
    JAZIRAH = 11
    AHLI = 12
    BANK_NAME = (
        (SAB, 'بنك ساب'),
        (SAMBA, 'مجموعة سامبا المالية'),
        (INMA, 'مصرف الإنماء'),
        (RAJIHI, 'مصرف الراجحي'),
        (RIYAD, 'بنك الرياض'),
        (AWWAL, 'البنك الأول'),
        (SAFARANSI, 'البنك السعودي الفرنسي'),
        (ISTITHMAR, 'البنك السعودي للإستثمار'),
        (ARABI, 'البنك العربي الوطني'),
        (BILAD, 'بنك البلاد'),
        (JAZIRAH, 'بنك الجزيرة'),
        (AHLI, 'البنك الأهلي التجاري'),
    )
    salon_id = models.OneToOneField(User, on_delete=models.CASCADE)
    salon = models.CharField(max_length=45, blank=True)
    mobile = models.CharField(max_length=45, blank=True)
    country = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=45, blank=True)
    district = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=100, blank=True)
    lng = models.DecimalField(max_digits=11, decimal_places=8)
    lat = models.DecimalField(max_digits=10, decimal_places=8)
    iban = models.CharField(max_length=45, blank=True)
    bank = models.PositiveSmallIntegerField(choices=BANK_NAME, blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.salon


class Services(models.Model):
    salon = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    minTime = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.datetime.now(), blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Artists(models.Model):
    ALL_DAY = (
        (1, 'الأحد'),
        (2, 'الاثنين'),
        (3, 'الثلاثاء'),
        (4, 'الأربعاء'),
        (5, 'الخميس'),
        (6, 'الجمعة'),
        (7, 'السبت'),
    )
    salon = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45,)
    nationality = models.CharField(max_length=45, null=True)
    service = models.ManyToManyField(Services, blank=True)
    weekend_days = MultiSelectField(choices=Days.ALL_DAYS, max_choices=7, max_length=7)
    created_date = models.DateTimeField(default=timezone.datetime.now(), blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class WorkDays(models.Model):
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    day = models.ForeignKey(Days, blank=True, on_delete=models.CASCADE)
    is_week_end = models.BooleanField(default=False)

    def __str__(self):
        return self.artist.name


class BreakHours(models.Model):
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    day = models.ForeignKey(WorkDays, on_delete=models.CASCADE)
    hours = models.ManyToManyField(Hours, blank=True,)

    def __str__(self):
        return self.artist.name


# class ArtistServices(models.Model):
#     salon = models.ForeignKey(User, on_delete=models.CASCADE)
#     artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
#     service = models.ManyToManyField(Services)
#
#     def __str__(self):
#         return self.artist.name


class Tasks(models.Model):
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    customer = models.CharField(max_length=45)
    date = models.DateTimeField()

    def __str__(self):
        return self.artist.name + ' - ' + self.customer


class Orders(models.Model):
    A_ONE = 1
    A_TWO = 2
    A_THREE = 3
    A_FOUR = 4
    A_FIVE = 5
    A_SIX = 6
    A_SEVEN = 7
    A_EIGHT = 8
    A_NINE = 9
    A_TEN = 10
    A_ELEVEN = 11
    P_TWELVE = 12
    P_ONE = 13
    P_TWO = 14
    P_THREE = 15
    P_FOUR = 16
    P_FIVE = 17
    P_SIX = 18
    P_SEVEN = 19
    P_EIGHT = 20
    P_NINE = 21
    P_TEN = 22
    P_ELEVEN = 23
    A_TWELVE = 24
    HOURS = (
        (A_ONE, '01:00 am'),
        (A_TWO, '02:00 am'),
        (A_THREE, '03:00 am'),
        (A_FOUR,  '04:00 am'),
        (A_FIVE, '05:00 am'),
        (A_SIX, '06:00 am'),
        (A_SEVEN, '07:00 am'),
        (A_EIGHT, '08:00 am'),
        (A_NINE, '09:00 am'),
        (A_TEN, '10:00 am'),
        (A_ELEVEN, '11:00 am'),
        (P_TWELVE, '12:00 pm'),
        (P_ONE, '01:00 pm'),
        (P_TWO, '02:00 pm'),
        (P_THREE, '03:00 pm'),
        (P_FOUR, '04:00 pm'),
        (P_FIVE, '05:00 PM'),
        (P_SIX, '06:00 PM'),
        (P_SEVEN, '07:00 PM'),
        (P_EIGHT, '08:00 PM'),
        (P_NINE, '09:00 PM'),
        (P_TEN, '10:00 PM'),
        (P_ELEVEN, '11:00 PM'),
        (A_TWELVE, '12:00 PM'),
    )

    salon = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=45)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=50, default='00:00')
    answer = models.BooleanField(default=False)
    approval = models.IntegerField(default=0)
    order_created_date = models.DateTimeField(default=timezone.datetime.now(), blank=True)
    done = models.BooleanField(default=False)
    salon_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return self.customer


class Hotel(models.Model):
    HOTEL = (
        ('الشيرتون', 'هوليدي ان'),
        ('a', 'بنك ساب'),
        ('b', 'مجموعة سامبا المالية'),
        ('c', 'مصرف الإنماء'),
        ('d', 'مصرف الراجحي'),
        ('de', 'بنك الرياض'),
        ('ty', 'البنك الأول'),
        ('uy', 'البنك السعودي الفرنسي'),
        ('f', 'البنك السعودي للإستثمار'),
        ('d', 'البنك العربي الوطني'),
        ('s', 'بنك البلاد'),
        ('h', 'بنك الجزيرة'),
        ('y', 'البنك الأهلي التجاري'),

    )
    title = MultiSelectField(choices=HOTEL)


class Offers(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
