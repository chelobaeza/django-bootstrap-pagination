from django import template

register = template.Library()


@register.inclusion_tag('pagination/pagination.html', takes_context=True)
def paginate(context, page=None, begin_pages=2, end_pages=2, before_current_pages=4, after_current_pages=4):
    '''
    return google like pagination
    Usage::
        {% paginate the_obj_to_paginate %}

    Example::
        {% paginate %}
    At this case 'page_obj' is the default
    object for pages that django provide with generic classes
    extracted from context
    '''
    if not page:
        page = context['page_obj']

    before = max(page.number - before_current_pages - 1, 0)
    after = page.number + after_current_pages

    begin = page.paginator.page_range[:begin_pages]
    middle = page.paginator.page_range[before:after]
    end = page.paginator.page_range[-end_pages:]
    last_page_number = end[-1]

    def collides(firstlist, secondlist):
        return set(firstlist).intersection(set(secondlist))

    # If middle and end has same entries, then end is what we want
    if collides(middle, end):
        end = range(max(last_page_number - before_current_pages - after_current_pages, 1), last_page_number + 1)  # noqa
        middle = []

    # If begin and middle ranges has same entries, then begin is what we want
    if collides(begin, middle):
        begin = range(1, min(before_current_pages + after_current_pages, last_page_number) + 1)  # noqa
        middle = []

    # If begin and end has the same entries then begin is what we want
    if collides(begin, end):
        begin = range(1, last_page_number + 1)
        end = []

    return {
        'request': context.request,
        'page': page,
        'begin': begin,
        'middle': middle,
        'end': end
    }


@register.simple_tag
def url_replace(request, field, value):
    d = request.GET.copy()
    d[field] = value
    return d.urlencode()
