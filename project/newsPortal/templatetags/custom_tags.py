from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag()
def current_time(format_string: str = "%b %d %Y") -> str:
    return timezone.now().strftime(format_string)


