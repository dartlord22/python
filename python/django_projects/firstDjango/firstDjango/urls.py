from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
# With the above we are saying that we want the urls.py file in the base folder to take care of all of the routing
