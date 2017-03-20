from blog.views import index,view_post,view_category,post_new
from django.conf.urls import url
from django.contrib.auth.views import login
from blog.forms import LoginForm

urlpatterns = [

    url('blog/$',index),
    url('blog/category/(?P<id>[0-9]+)',view_category),
    url('blog/post/(?P<id>[0-9]+)',view_post),
    url('blog/login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url('blog/new$', post_new, name='post_new'),
]