from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm, ShareRecipeForm
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string


class RecipeSelection(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 10


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class ShareRecipe(View):
    form_type = ShareRecipeForm
    template_name = 'recipe_share.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_type(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                'share_recipe_form': form,
                'user': request.user
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_type(request.POST, request.FILES)
        print("we got through")

        if form.is_valid():
            unique_string = get_random_string(length=5)
            form.instance.author = request.user
            form.instance.slug = slugify(form.instance.name)
            checked_form = form.save(commit=False)
            checked_form.save()
            return render(
                request,
                'recipe_share.html',
                {'posted': True}
            )
        else:
            return render(
                request,
                'recipe_share.html',
                {
                    'share_recipe_form': form,
                    'failed': True,
                    'posted': False,
                }
            )
