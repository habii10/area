"""
URL configuration for area project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from shapes.views import SquareView
from shapes.views import RectangleView
from shapes.views import TriangleView
from shapes.views import circleView
from shapes.views import ParellelogramView
from shapes.views import TrapeziumView
from shapes.views import RhombusView
from shapes.views import ElipseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("square/",SquareView.as_view()),
    path("rectangle/",RectangleView.as_view()),
    path("triangle/",TriangleView.as_view()),
    path("circle/",circleView.as_view()),
    path("parallelogram/",ParellelogramView.as_view()),
    path("trapezium/",TrapeziumView.as_view()),
    path("rhombus/",RhombusView.as_view()),
    path("ellipse/",ElipseView.as_view()),
]
