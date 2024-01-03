# YouTube course link:

https://www.youtube.com/watch?v=IrUG07namQ8&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=7

https://github.com/selfedu-rus/django-lessons


Collect static all files to one folder
python manage.py collectstatic

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

STATIC_URL - префикс URL-адреса для статических файлов;
STATIC_ROOT - путь к общей статической папке, используемой в prod;
STATICFILES_DIRS - список дополнительных (нестандартных) путей к статическим файлам, используемых для сбора и для режима отладки

git rm -r -f --cached media
git rm --cached */__pycache__/*