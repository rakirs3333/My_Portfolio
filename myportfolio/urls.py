from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet,ContactView,SkillsView
from django.views.generic import TemplateView
router=DefaultRouter()

router.register(r"projects",ProjectViewSet)
router.register(r"skills",SkillsView)

urlpatterns=[
    path("",TemplateView.as_view(template_name="build/index.html")),
    path("api/",include(router.urls)),
    path("api/contact/",ContactView.as_view(),name="contact"),
    # path("api/",include(router.urls))

]