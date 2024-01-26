from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def search_posts(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        search_results= Post.objects.filter(title__icontains=searched).order_by('-created_on')
        if len(search_results)>0:
            context = {'search_results':search_results,'searched':searched}
            return render(request,'searched.html', context)
        else:
            return render(request,'noresult.html')

        
    else:
        context = {}
        return render(request,'searched.html', context)