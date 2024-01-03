from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_id': self.pk})

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Women(models.Model):
    """

    python manage.py makemigrations
    python manage.py sqlmigrate app01 0001
    python manage.py migrate
    python manage.py shell
    >> from app01.models import Women
    >> w1 =Women(title="women 1", content="contemt 1")
    >> w1.save()

    >> Women.objects
    >> Women.objects.create(title="women 2", content="contemt 2")
    >> w3 = Women.objects.create(title="women 3", content="contemt 3")
    >> w3.id

    >> Women.objects.all()
    >> w = Women.objects.all()
    >> w[0]
    >> w[0].title

    >> Women.objects.filter(title='women 2')
    >> Women.objects.filter(pk__gte=2)
    >> Women.objects.exclude(pk=2)
    >> Women.objects.get(pk=2)
    >> Women.objects.get(pk=20)
    >> Women.objects.filter(pk__gte=2).order_by('-time_create')

    Update rows:
    >> wu = Women.objects.get(pk=2)
    >> wu.title = "Updated title data"
    >> wu.save()

    Delete rows:
    >> wd = Women.objects.filter(pk__gte=2)
    >> wd.delete()
    >> Women.objects.all()

    from django.db import connection
    connection.queries

    exit()

    """
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']


