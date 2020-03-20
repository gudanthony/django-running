
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# from apps.events.models.competitor import Competitor
# from apps.events.models.event import Event

User = get_user_model()


class HomePageView(LoginRequiredMixin, TemplateView):
    """."""

    template_name = "base/home.html"

    def get_context_data(self, **kwargs):
        """."""
        context = super().get_context_data(**kwargs)
        return context
