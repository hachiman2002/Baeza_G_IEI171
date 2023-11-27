from django.urls import path
from .views import Index, SociosListView, SociosCreateView, SociosUpdateView, SociosDeleteView

core_patterns = ([
    path('', Index.as_view(), name='index'),
    path('sociosList', SociosListView.as_view(), name='socios-list'),
    path('sociosCreate', SociosCreateView.as_view(), name="socios-create"),
    path('sociosUpdate/<int:pk>/', SociosUpdateView.as_view(), name="socios-update"),
    path('sociosDelete<int:pk>/', SociosDeleteView.as_view(), name="socios-delete"),
],'socios')