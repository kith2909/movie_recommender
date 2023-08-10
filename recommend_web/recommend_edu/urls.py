from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView, ChatView, VotesView, AnswerView

app_name = "recommend_edu"
urlpatterns = [
                  path("", IndexView.as_view(), name="index"),
                  path("results/", AnswerView.as_view(), name="results"),
                  path("chat/", ChatView.as_view(), name="chat"),
                  path('votes/', VotesView.as_view(), name='votes'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
