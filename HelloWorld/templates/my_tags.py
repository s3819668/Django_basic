from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def mul(v1,v2,v3):
    return v1*v2*v3

@register.simple_tag
def my_input(v1,v2):
    temp_html='''
    <div>
        <span id=%s></span>
        <input type="text" id="%s">
    </div>'''%(v1,v2)
    return mark_safe(temp_html)
@register.filter
def my_filter(v1,v2):
    return v1*v2