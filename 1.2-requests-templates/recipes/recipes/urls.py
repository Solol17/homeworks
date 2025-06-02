"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path

from calculator.views import omlet, pasta, buter

urlpatterns = [
    path('omlet/<int:servings>/', omlet, name='omlet_with_servings'),
    path('omlet/', omlet, name='omlet_default'),
    path('pasta/<int:servings>/', pasta, name='pasta_with_servings'),
    path('pasta/', pasta, name='pasta_default'),
    path('buter/<int:servings>', buter, name='buter_with_servings'),
    path('buter/', buter, name='buter_with_servings'),
    # здесь зарегистрируйте вашу view-функцию
]
