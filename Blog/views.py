from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Blog.models import Post


@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    import json
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        title = body_data['title']
        body = body_data['body']

        if title and body:

            data = Post.objects.create(
                title=title,
                body=body
            )
            return JsonResponse(str(data), safe=False)
        else:
            return JsonResponse('Failed!', safe=False)