from django.contrib import admin
from django.urls import path, include    #コード追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),      #コード追加
]
