from django import urls
from polls import views

app_name = "polls"
urlpatterns = [
    urls.path("", views.IndexView.as_view(), name="index"),
    urls.path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    urls.path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    urls.path("<int:question_id>/vote/", views.vote, name="vote"),
]
