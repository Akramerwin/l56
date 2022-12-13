from django.contrib import admin
from django.urls import path
from webapp.views import index_views, stufs_view, stuf_create, stuf_update_view, stuf_delete_view, stuf_in_the_bag, stuf_bag_list, delete_stuf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.as_view(), name='index'),
    path('stufs/<int:pk>/', stufs_view.as_view(), name='view'),
    path('create/', stuf_create.as_view(), name='create'),
    path('stufs/<int:pk>/update', stuf_update_view.as_view(), name='update'),
    path('stufs/<int:pk>/delete', stuf_delete_view.as_view(), name='delete'),
    path('stufs/<int:pk>/bag', stuf_in_the_bag.as_view(), name='stufbag'),
    path('stufs/bag', stuf_bag_list.as_view(), name='stuflist' ),
    path('stufs/bag/<int:pk>/delete/', delete_stuf.as_view(), name='deletestuf')
]
