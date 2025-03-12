from django.urls import path, include
from .views import UserViewset,NewsViewset, TagsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewset)
router.register('news', NewsViewset)
router.register('tags', TagsViewset)

urlpatterns = [
    path('', include(router.urls)),
]+router.urls
