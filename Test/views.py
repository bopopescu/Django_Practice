from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.db import transaction

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Test.models import CompanyInfo, IndustryTypeSubordinate, IndustryTypeMain, Division


@csrf_exempt
@require_http_methods(["POST"])
@transaction.atomic
def Registration(request):
    import json
    if request.method == 'POST':
        # body_unicode = request.body.decode('utf-8')
        # body_data = json.loads(body_unicode)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        name = request.POST.get('name')
        division = Division.objects.create(
            name=name
        )

        company_name = request.POST.get('company_name')
        country = request.POST.get('country')
        # division = request.POST.get('division')
        industrytypesubordinate = request.POST.get('industrytypesubordinate')

        # company info creation
        company_info = CompanyInfo.objects.create(
            company_name=company_name,
            country=country,
            division=division,
            industrytypesubordinate=industrytypesubordinate,
            user=user
        )
        return JsonResponse(user_data, safe=False)
    else:
        return JsonResponse('Failed!', safe=False)
