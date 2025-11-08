from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key_tuple):
    """يسمح بالوصول إلى grade_dict[(subject_id, month_id)]"""
    return dictionary.get(key_tuple)