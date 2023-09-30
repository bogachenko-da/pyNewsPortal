from django import template

register = template.Library()

words = ['FIA', 'Red Bull', 'AlphaTauri', 'Mercedes-AMG']


@register.filter()
def censor(value):
    for word in words:
        value = value.replace(word, '*' * len(word))
    return value
