from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


class BaseModelImage(models.Model):
    photo = models.ImageField(
        'фото',
        upload_to='images/',
        blank=True,
    )

    class Meta:
        abstract = True

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '200x200',
            crop='center',
            quality=51,
        )

    def image_tmb(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_img.url}">',
            )
        return 'Нет изображения'

    @property
    def get_img_small(self):
        return get_thumbnail(
            self.photo,
            '50x50',
            crop='center',
            quality=51
        )

    def image_tmb_small(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_img_small.url}">',
            )
        return 'Нет изображения'

    @property
    def get_img_logo(self):
        return get_thumbnail(
            self.photo,
            '30x30',
            crop='center',
            quality=51
        )

    def image_tmb_logo(self):
        if self.photo:
            return mark_safe(
                '<img class="rounded-circle border border-1 border-dark" '
                f'src="{self.get_img_logo.url}">',
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)


class BaseModelSlug(models.Model):
    slug = models.CharField(
        'ссылка',
        max_length=2048,
    )

    class Meta:
        abstract = True


class BaseModelMedia(models.Model):
    name = models.CharField(
        'название',
        max_length=256,
    )
    file = models.FileField(
        'файл',
        upload_to='files/',
    )
    description = models.CharField(
        'описание',
        max_length=1024,
        null=True,
        blank=True,
    )

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BaseModelPost(BaseModelImage):
    text = models.CharField(
        'текст к посту',
        max_length=1024,
    )

    class Meta:
        abstract = True
