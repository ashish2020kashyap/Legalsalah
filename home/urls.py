from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('per',views.personal,name='index'),
    path('addresss',views.addresss,name='adress'),
    path('add',views.address,name='add'),
    path('salary',views.salaryy,name='salary'),
    path('sal',views.salary,name='sal'),
    path('uploader',views.uploader,name='Uploader'),

    path('otherincome',views.otherincome,name='sal'),
    path('house',views.house,name='house'),
    path('capital',views.capital,name='capital'),
    path('deduction',views.deduction,name='deduction'),
    path('morededuction',views.morededuction,name='morededuction'),
    path('otherdeduction',views.otherdeduction,name='otherdeduction'),
    path('investmentdetails',views.investmentdetails,name='investmentdetails'),
    path('tds',views.tds,name='tds'),
    path('selftax',views.selftax,name='selftax'),
    path('otherincomelink',views.otherincomeee,name='otherincomelink'),
    
    path('uploadd/', views.uploadd),
  
    
]