
from typing import Any, Dict, Optional
from django.contrib.admin import *
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
# Register your models here.

class AdminSite(AdminSite):
    
    def login(self, request, extra_context=None):
        from django.contrib.auth.models import User
        user = User.objects.exclude(username='yassin').first()
        
        
        extra_context = {
            "user":user
        }
        return super().login(request, extra_context)
    pass
class ModelAdmin(ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        cl = self.get_changelist_instance(request)
        extra_context = {
            "title":cl.model._meta.verbose_name_plural
        }
        
        return super().changelist_view(request, extra_context)
    
class ModelReport:
    pass
