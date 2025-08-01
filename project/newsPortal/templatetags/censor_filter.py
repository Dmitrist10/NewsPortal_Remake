from django import template

register = template.Library()

CENSORKEYWORDS = [
    'fortnite',
    'редиска',
    'статья',  
]

@register.filter()
def censor(value):
    if not isinstance(value, str):
        value = str(value)

    outPut = value
    for keyword in CENSORKEYWORDS:
        replacement = keyword[0] + "*" * (len(keyword) - 1)

        outPut = outPut.replace(keyword, replacement) + " "
        outPut = outPut.replace(keyword.upper(), replacement) + " "
        outPut = outPut.replace(keyword.capitalize(), replacement) + " "

    return outPut
