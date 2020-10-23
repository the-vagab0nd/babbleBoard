from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list_view(request, *args, **kwargs):
    qs = Post.objects.all()
    posts_list = [{"id": x.id, "content": x.content, "likes": x.likes} for x in qs]
    data = {
        "response": posts_list
    }
    return JsonResponse(data)

def home_view(request):
    return render(request, 'pages/home.html', context = {})


def post_detail_view(request, post_id):
    data = {"id":post_id}
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data["content"] = obj.content
    except:
        data["message"] = "The thing you demand, I dont posses"
        status = 404
    return JsonResponse(data, status=status)
