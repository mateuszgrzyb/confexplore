from django.urls import path

from misc.views import KontaktView, RegulaminView, FAQView

urlpatterns = [
    path('faq/', FAQView.as_view(), name='faq'),
    path('regulamin/', RegulaminView.as_view(), name='regulamin'),
    path('kontakt/', KontaktView.as_view(), name='kontakt'),
]