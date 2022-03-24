from django.template.defaulttags import register

@register.filter
def get_value(dictionary, value):
    return dictionary.get(value)