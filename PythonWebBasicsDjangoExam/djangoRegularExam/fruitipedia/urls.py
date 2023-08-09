from django.urls import path, include
from djangoRegularExam.fruitipedia.views import index_page, dashboard_page, fruit_create_page, fruit_details_page, \
    fruit_edit_page, fruit_delete_page, profile_create_page, profile_details_page, profile_edit_page, \
    profile_delete_page

urlpatterns = (
    path('', index_page, name='index page'),
    path('dashboard/', dashboard_page, name='dashboard page'),
    path('create/', fruit_create_page, name='fruit create page'),
    path('<int:pk>/details', fruit_details_page, name='fruit details page'),
    path('<int:pk>/edit', fruit_edit_page, name='fruit edit page'),
    path('<int:pk>/delete', fruit_delete_page, name='fruit delete page'),
    path('profile/', include([
        path('create/', profile_create_page, name='profile create page'),
        path('details/', profile_details_page, name='profile details page'),
        path('edit/', profile_edit_page, name='profile edit page'),
        path('delete/', profile_delete_page, name='profile delete page'),
    ])),
)
