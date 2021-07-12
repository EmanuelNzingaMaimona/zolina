from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def str_sub(value):
    # Array of words to be filtered
    a = ['username', 'password1', 'password2']
    b = ['Nome de usuário', 'Senha1', 'Senha2']
    print('BEFORE===>>>',value)
    for i in range(3):
        value = value.replace(a[i], b[i])
        
    print('AFTER===>>>',value)
    return value