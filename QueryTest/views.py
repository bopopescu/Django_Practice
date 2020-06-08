# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
#
# from .models import Pizza, Article
# from django.http import JsonResponse
# from django.http import JsonResponse
#
# from .models import Pizza, Topping
#
#
# # Create your views here.
# def Pizzas(request):
#     if request.method == "GET":
#         users = Pizza.objects.all()
#         pizza = {
#             'id': users[0].id,
#             'name': users[0].name,
#             'topping': {
#                 'id': users[0].toppings.id,
#                 'name': users[0].toppings.name
#             }
#         }
#         context = {
#             'pizza': pizza,
#
#         }
#     return JsonResponse(context, safe=False)
#
#
# @csrf_exempt
# @require_http_methods(["POST"])
# def pizza(request):
#     # getting api data
#     import json
#     if request.method == 'POST':
#         body_unicode = request.body.decode('utf-8')
#         body_data = json.loads(body_unicode)
#
#          name= body_data['name']
#          toppings= body_data['toppings']
#     # if data available
#     if name and toppings:
#         # user creation
#         artic = Pizza.objects.create_user(
#             name=name,
#             toppings=toppings,
#
#         )
#
#         # return api response
#         return JsonResponse({'message': 'Employer successfully register done!'}, status=201)
#
#     # if data not available
#     else:
#         return JsonResponse({'message': 'Signup Failed!'}, status=404)
