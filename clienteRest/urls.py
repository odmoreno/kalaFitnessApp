from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from clienteRest import views as api


urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^personal/', api.PersonalList.as_view()),

]
urlpatterns= format_suffix_patterns(urlpatterns)
