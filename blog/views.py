from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
import datetime

from blog.models import Blogpage, Blogger, Comment
# Create your views here.
def index(request):
    """View function for home page of site."""

    blogpages = Blogpage.objects.count()
    authors = Blogger.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    num_blogs = Blogpage.objects.all().count()
    num_bloggers = Blogger.objects.all().count()

    context = {
        'blogpages': blogpages,
        'authors': authors,
        'num_visits': num_visits,
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
    }

    return render(request, 'index.html', context=context)

from django.views import generic
import operator
from django.db.models import Q

class SearchListView(generic.ListView):
    template_name = 'blog/search_results.html'
    model = Blogpage
    paginate_by = 10

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        #print(q)
        context = super().get_context_data(**kwargs)
        context['search'] = q
        context['results_list'] = Blogpage.objects.filter(Q(author__first_name__icontains=q) | Q(author__last_name__icontains=q) | Q(description__icontains=q) | Q(title__icontains=q))
        return context

class BlogListView(generic.ListView):
    model = Blogpage
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("pk")
        context['blogger_item_list'] = Blogpage.objects.filter(author__id=id_)
        # print(self)
        return context

class BlogDetailView(generic.DetailView):
    model = Blogpage
    comment_test = Comment.objects.exclude(blog=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("pk")
        blog_comments = Comment.objects.filter(blog=id_)
        context['blogpage_id'] = id_
        context['comments'] = blog_comments
        print(context)
        return context

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 5
    #Blogpage.author.id is what I need for specific blogger articles

class BloggerDetailView(generic.DetailView):
    model = Blogger

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_ = self.kwargs.get("pk")
        context['blogger_item_list'] = Blogpage.objects.filter(author__id=id_)
        #print(context)
        # print(self)
        return context


class CommentCreate(CreateView):
    model = Comment
    fields = ['description',]

    def get_success_url(self):
        #print(self.kwargs['pk'])
        return reverse_lazy('blog-detail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        """Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blogpage, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['commenter'] = get_object_or_404(Blogpage, pk = self.kwargs['pk'])
        print(context)
        return context
