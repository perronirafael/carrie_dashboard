from django import template
from django.utils.timezone import localtime, now, make_aware, get_current_timezone
from datetime import datetime, time

register = template.Library()

@register.filter
def format_patient_date(value):
    if not value:
        return ""

    if isinstance(value, datetime) is False:
        value = datetime.combine(value, time.min)

    if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
        tz = get_current_timezone()
        value = make_aware(value, timezone=tz)

    value = localtime(value)
    now_time = localtime(now())
    delta = now_time.date() - value.date()

    hour_str = value.strftime("%I:%M %p").lstrip("0") 

    if delta.days == 0:
        return f"Today {hour_str}"
    elif delta.days == 1:
        return f"Yesterday {hour_str}"
    else:
        day_str = value.strftime("%A")
        return f"{day_str} {hour_str}"

@register.filter
def status_color(value):
    if not value:
        return 'gray'
    mapping = {
        'stable': 'green',
        'clinical concern': 'yellow',
        'potential emergency reported': 'red'
    }
    return mapping.get(value.strip().lower(), 'gray')

