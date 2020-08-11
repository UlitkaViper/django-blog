from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from django.forms.models import model_to_dict
from .forms import CreateForm

# Create your views here.


class PostList(View):
    def get(self, request):
        # model = Post
        template_name = 'blog/home.html'
        queryset = Post.objects.all()
        context = {'object_list': queryset}
        return render(request, template_name, context)


class CreatePost(View):
    def get(self, request):
        template_name = 'blog/create.html'
        #obj = Post.objects.get(id=1)
        #form = CreateForm(initial=model_to_dict(obj))
        form = CreateForm()
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request):
        model = Post
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('post-list')


class PostDetails(View):
    def get(self, request, id):
        template_name = 'blog/details.html'
        post = get_object_or_404(Post, id=id)
        context = {
            'post_details': post
        }
        return render(request, template_name, context)


class UpdatePost(View):
    model = Post

    def post(self, request, id):
        if 'CompleteUpdate' in request.POST:
            obj = get_object_or_404(Post, id=id)
            form = CreateForm(request.POST, instance=obj)
            if form.is_valid:
                form.save()
            return redirect(f'/details/{id}')

        if 'Update' in request.POST:
            template_name = 'blog/update.html'
            post = get_object_or_404(Post, id=id)
            form = CreateForm(instance=post)
            context = {'form': form,
                       'id': id}
            return render(request, template_name, context)

        if 'Delete' in request.POST:
            post = get_object_or_404(Post, id=id)
            post.delete()
            print(request.POST)
            return redirect('/')

        return redirect('/')
