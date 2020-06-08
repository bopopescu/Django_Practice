import json

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .form import UserForm, ProfileForm


@method_decorator(csrf_exempt, name='dispatch')
class Signup(View):
    @transaction.atomic
    def post(self,request):
        # getting api data
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        seeker_form = UserForm(body_data)
        profile = ProfileForm(body_data)
        if seeker_form.is_valid():
            seeker_form.instance.save()
            profile.instance.save()
            return JsonResponse({'message': 'Registration Successful!'}, status=201, safe=False)
        else:
            return JsonResponse({'message': seeker_form.errors}, status=422)