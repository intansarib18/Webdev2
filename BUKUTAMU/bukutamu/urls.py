from django.contrib import admin
from django.urls import path, include

# from django.http import HttpResponse
# # def buku(coba):
# #     return HttpResponse('Teknik Informatika Unsulbar')

from django.shortcuts import render
def buku(req):
    return render(req, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',buku)
    # path('registrasi',buku)
]