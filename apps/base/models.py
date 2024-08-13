from django.db.models import * 

# Create your models here.
class Index(Model):
    title = CharField(
        max_length=255,
        verbose_name='Заголовок сайта (на главной странице)'
    )
    description = TextField(
        verbose_name="Описание сайта ()"
    )
    logo = ImageField(
        upload_to='image/',
        verbose_name='Логотип'
    )
    banner = ImageField(
        upload_to='image/'
    )
    twitter = URLField(
        verbose_name='Укжите ссылку на twitter'
    )
    facebook = URLField(
        verbose_name='Укжите ссылку на facebook'
    )
    github = URLField(
        verbose_name='Укжите ссылку на github'
    )
    gmail = URLField(
        verbose_name='Укжите ссылку на почту'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки главной страницы'


class About(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "Название информации"
                )
    description = TextField(
    verbose_name="Описание информации"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Action(Model):
    title = CharField(
    max_length = 255,
    verbose_name = "Название действия"
                )
    description = TextField(
    verbose_name="Описание действия"
                )
    image = ImageField(
        upload_to = "action_image",
        verbose_name="фото"

    )
    desc_image = CharField(
    max_length = 255,
    verbose_name = "Описание фото"
                )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'действие'
        verbose_name_plural = 'действии'


class Image(Model):
    photo = ImageField(
         upload_to = "actional_image",
        verbose_name="фотки"

    )
    photo2 = ImageField(
         upload_to = "actional_image",
        verbose_name="фотки"

    )

    class Meta:
        verbose_name = 'фотографии'
        verbose_name_plural = 'фотографии'
    