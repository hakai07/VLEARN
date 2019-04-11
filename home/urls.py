from django.conf.urls import url,include
from . import views

app_name = 'home'

urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_login/third/$',views.third_page,name='third_page'),
    url(r'^user_login/fourth/$',views.fourth_page,name='fourth_page'),
    url(r'^user_login/fifth/$',views.fifth_page,name='fifth_page'),
    url(r'^user_login/sixth/$',views.sixth_page,name='sixth_page'),
    url(r'^user_login/seventh/$',views.seventh_page,name='seventh_page'),
    url(r'^user_login/eighth/$',views.eighth_page,name='eighth_page'),
    url(r'^user_login/ninth/$',views.ninth_page,name='ninth_page'),
    url(r'^user_login/tenth/$',views.tenth_page,name='tenth_page'),
    url(r'^user_login/eleventh/$',views.eleventh_page,name='eleventh_page'),
    url(r'^user_login/twelveth/$',views.twelveth_page,name='twelveth_page'),
    url(r'^user_login/thirteenth/$',views.thirteenth_page,name='thirteenth_page'),
    url(r'^user_login/fourteenth/$',views.fourteenth_page,name='fourteenth_page'),
    url(r'^user_login/fifteenth/$',views.fifteenth_page,name='fifteenth_page'),
    url(r'^user_login/leaderboard/$',views.leaderboard,name='leaderboard'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/contactUs/$',views.contactUs,name='contactUs')
    ]
