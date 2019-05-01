from django.urls import path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('new_orders/', views.NewOrders.as_view(), name='new_orders'),
    path('new_orders/update_orders/<int:pk>/', views.Approval.as_view(), name='update_orders'),
    path('today_tasks/', views.TodayTasks.as_view(), name='today_tasks'),
    path('today_tasks/is_done/<int:pk>/', views.IsDone.as_view(), name='is_done'),
    path('completed_orders/', views.CompletedOrders.as_view(), name='completed_orders'),
    path('canceled_orders/', views.CanceledOrders.as_view(), name='canceled_orders'),

    path('orders/add_orders/', views.add_orders, name='add_orders'),

    path('finance/', views.Finance.as_view(), name='finance'),

    path('services/add/', views.serv,  name='serv'),
    path('services/show/', views.show,  name='show'),
    path('services/edit/<int:id>', views.edit),
    path('services/update/<int:id>', views.update, name='update_service'),
    path('services/delete/<int:id>', views.destroy, name='delete'),

    path('o_services/add/', views.o_serv,  name='o_serv'),
    path('o_services/show/', views.o_show,  name='o_show'),
    path('o_services/edit/<int:id>', views.o_edit),
    path('o_services/update/<int:id>', views.o_update, name='o_update_service'),
    path('o_services/delete/<int:id>', views.o_destroy, name='o_delete'),

    path('artists/add/', views.arts,  name='arts'),
    path('artists/show/', views.arts_show,  name='arts_show'),
    path('artists/edit/<int:id>', views.arts_edit),
    path('artists/update/<int:id>', views.arts_update, name='arts_update'),
    path('artists/delete/<int:id>', views.arts_destroy, name='arts_delete'),
    # path('artists/tasks/', views.arts_tasks, name='arts_tasks'),
    # path('artists/tasks/add/', views.add_tasks, name='add_tasks'),
    # path('artists/tasks/update/<int:id>/', views.tasks_update, name='update_tasks'),


    path('calendar/', views.calendar, name='calendar'),
    path('map/', views.map, name='map'),

    path('profile/', views.ViewProfile.as_view(), name='profile'),
    path('profile/add/', views.Profile.as_view(), name='profile_add'),
    # path('profile/add/', views.profile_image_view, name='profile_add'),
    path('profile/<int:pk>/update/', views.UpdateProfile.as_view(), name='profile_update'),


    # path('image_upload', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('hotel_images', views.ViewImage.as_view(), name='hotel_images'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
