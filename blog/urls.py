from django.urls import path


from .views import HomePageView, AboutMeView, BlogListView, BlogDetailView, RecipeListView, RecipeDetailView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('blog/', BlogListView.as_view(), name='blog_home'),
    path('aboutme/', AboutMeView.as_view(), name='aboutme'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail')
]