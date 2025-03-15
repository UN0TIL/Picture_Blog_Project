from uuid import uuid4 # pf 10.5.2
from pytils.translit import slugify

def unique_slugify(instanse, slug, slug_field):
    '''
    Генератор уникальных slug моделей, в случае существования такого SLUG
    '''
    model = instanse.__class__
    unique_slug = slug_field
    if not slug_field:
        unique_slug = slugify(slug)
    elif model.objects.filter(slug=slug_field) and model.objects.filter(slug=slug_field).last().id != instanse.id:
        unique_slug = f'{slugify(slug)}-{uuid4().hex[:8]}'
    return unique_slug