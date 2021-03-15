from django.contrib import admin
from django.urls import path

from .apps.login.views import login_page, register_page
from .apps.login.api import (
    login_api_rand,
    login_api_verify,
    captcha_api_init,
    captcha_api_verify,
    register_api,
    register_api_id_gen
)

from .apps.chat.views import messages_page, explore_page, post_page, help_page
from .apps.main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('messages', messages_page),
    path('login', login_page),
    path('register', register_page),
    path('explore', explore_page),
    path('faq', help_page),
    path('post', post_page),
    path('api/v1/login/rand', login_api_rand),
    path('api/v1/login/verify', login_api_verify),
    path('api/v1/captcha/init', captcha_api_init),
    path('api/v1/captcha/verify', captcha_api_verify),
    path('api/v1/register/id', register_api_id_gen),
    path('api/v1/register', register_api)
]
