from django.urls import path, include
from . import views
from . import class_views
urlpatterns = [
    # path('',views.index, name='index'),
    path('',class_views.IndexPageListView.as_view(), name= 'index'),
    path('blog/', include('blog.urls')),
    
]
