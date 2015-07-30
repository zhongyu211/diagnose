from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diagnose.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^index.html', 'diagnose_app.views.index'),
    url(r'^setting.html', 'diagnose_app.views.setting'),

   #tables
    url(r'^tables.html', 'diagnose_app.views.tables'),
   #diagnose
    url(r'^diagnose.html', 'diagnose_app.views.diagnose'),
    url(r'^counts.html', 'diagnose_app.views.counts'),
    url(r'^troubleshooting.html', 'diagnose_app.views.troubleshooting'),
    url(r'^trafficload.html', 'diagnose_app.views.trafficload'),
    url(r'^abnormal.html', 'diagnose_app.views.abnormal'),
    #get the table info
    url(r'^gettableinfo/(?P<tablename>)$','diagnose_app.views.gettableinfo'),
    #get the chart info
    url(r'^counts/submit/$','diagnose_app.views.getchartinfo'),
    #get logid
    url(r'^diagnose/logsubmit/$','diagnose_app.views.getdiagnoseinfo'),
    #get the setting log path
    url(r'^path/setting/$','diagnose_app.views.prepdata'),
    #get the  logid
    url(r'^diagnose/getlogid/$','diagnose_app.views.getlogid'),


    url(r'^admin/', include(admin.site.urls)),

)
urlpatterns +=staticfiles_urlpatterns()
