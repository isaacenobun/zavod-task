from django import template
from datetime import datetime
import pytz

register = template.Library()

@register.filter(name='cs_date')
def cs_date(value):
    try:
        dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        
        return dt.strftime('%B %d, %Y')

    except ValueError:
        return value
    
@register.filter
def has_tag(tag_list, tag_name):
    return tag_name in [tag['tag'] for tag in tag_list]

@register.filter
def user_liked(likes, user_email):
    if likes is None:
        return False
    return any(like.email == user_email for like in likes)