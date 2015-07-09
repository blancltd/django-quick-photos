from django.utils.timezone import make_aware, utc

from .models import Photo


def update_photos(photos):
    obj_list = []

    for i in photos:
        image = i.images['standard_resolution']

        obj, created = Photo.objects.update_or_create(photo_id=i.id, defaults={
            'user': i.user.username,
            'image': image.url,
            'image_width': image.width,
            'image_height': image.height,
            'created': make_aware(i.created_time, utc),
            'caption': i.caption or '',
            'link': i.link,
        })

        obj_list.append(obj)

    return obj_list
