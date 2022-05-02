"""UWE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from UWE import views
from django.conf.urls.static import static
from django.conf import settings

from UWE.views import updateMovieView

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('', include('allAccounts.urls')),
    path('about_us', views.about_us, name='about_us'),
    path('films', views.MoviesView, name='films'),
    path('offers&discounts', views.DiscountView, name='offers&discounts'),
    path('add-movie', views.addMovie, name='add-movie'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catalog'),
    path('add-club', views.addClub, name='add-club'),
    path('add-club-rep', views.addClubRep, name='add-club-rep'),
    path('delete_movie/<int:id>', views.delete_movie, name='delete_movie'),
    path('<int:pk>/update_movie_details/', updateMovieView.as_view(), name='update_movie_details'),
    path('product/<str:name>/<int:id>', views.movie_details, name='movieDetails'),
    path('tickets/<int:id>', views.BuyTicketsView, name='buyTickets')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)