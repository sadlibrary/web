from django.template.defaulttags import register


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


@register.filter
def index(indexable, i):
    return indexable[i]


@register.filter
def file(append, i):
    return append+"."+i
