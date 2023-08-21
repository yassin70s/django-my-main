from typing import Dict, Optional
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

class ModelAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        extra_context = {
            'result_list':self.json_result_list(request),
        }
       
        return super().changelist_view(request, extra_context)
    def json_result_list(self,request):
        instance = self.get_changelist_instance(request)
        results = []
        for result_list in instance.result_list:
            
            result = {}
            for li in self.list_display:
                result[li] = getattr(result_list,li)
            results += [result]