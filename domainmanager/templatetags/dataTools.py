from django import template

register = template.Library()

# user in characterboonsummary.html to get the
# triplets in STATUS array for the approvals
@register.filter
def getValue(array, key):
    return array[int(key)]
