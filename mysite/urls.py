"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def home(request):
    return HttpResponse(
        """
        <html>
        <head><title>My Django Site</title></head>
        <body>
            <h1>Hello from the home page!</h1>
            <p>Welcome to my Django polls application.</p>
            <a href="/polls/" style="
                display: inline-block;
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            ">Go to Polls</a>
        </body>
        </html>
        """
    )


urlpatterns = [
    path("", home),  # Add this
    path("polls/", include("polls.urls", namespace="polls")),  # this is important!
    path("admin/", admin.site.urls),
]
