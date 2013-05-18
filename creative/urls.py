from django.conf.urls import url, patterns
from .views import (IdeaDetailView, IdeaListView)

urlpatterns = patterns(
    '',
    url(
        r'(?P<stage>\w+)/(?P<pk>\d+)/$',
        IdeaDetailView.as_view(),
        name='idea_detail',
    ),
    url(
        r'(?P<stage>\w+)/$',
        IdeaListView.as_view(),
        name='Idea_list',
    ),
)
