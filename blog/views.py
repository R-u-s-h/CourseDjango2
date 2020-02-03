from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category
from .models import Post


# def home(request):
#     if request.method == "POST":
#         return HttpResponse("It's POST request")
#     elif request.method == "GET":
#         return HttpResponse("It's GET request")

class HomeView(View):
        # def get(self, requset):
        #     return HttpResponse("It's GET request")
        #
        # def post(self, request):
        #     return HttpResponse("It's POST request")
        """Home page"""
        # def get(self, request):
        #     category_list = Category.objects.all()
        #     return render(request, "blog/home.html", {"categories": category_list})
        def get(self, request):
                post_list = Post.objects.all()
                return render(request, "blog/home.html", {"posts": post_list})

class CategoryView(View):
        def get(self, request, category_name):
            category = Category.objects.get(slug=category_name)
            return render(request, "blog/post_list.html", {"category": category})