# Episode 1.

- Initial setup for django project

```
mkdir django_tutorial_schafer
cd django_tutorial_schafer
python -m venv env
source env/bin/activate
pip install django python-decouple
pip freeze > requirements.txt
django-admin startproject django_tutorial_schafer .
```

- Remove sensitive data from django_tutorial_schafer and place into .env file

```
python manage.py runserver
```


# Episode 2.
```
python manage.py startapp blog
```
- create home, about functions in blog/views.py that take HTTP requests and return HTTP responses
- create blog/urls.py file and add urlpatterns list
- add "blog/" to urlpatterns list in django_tutorial_schafer/urls.py



# Episode 3.
- create directory blog/templates/blog/ and create home.html, about.html, and base.html files
- add bootstrap to base.html file from [here](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)
- create blog/static/blog/main.css file
- add snippets from [here](https://github.com/CoreyMSchafer/code_snippets/tree/master/Django_Blog/snippets) to relevant files
- add `{% load static %}` to top of base.html to load the css
- add `{% block content %}{% endblock %}` to base.html
- add `{% extends "blog/base.html" %}` to top of non-template html files
- add a content block to the non-template html files, e.g. `{% block content %}<h1>About page</h1>{% endblock content %}`
- use condiitonals / for loops in the html, e.g.
```
    {%if title %}
    <title>Django Blog - {{ title }}</title>
    {% else %}
    <title>Django Blog</title>
    {% endif %}


    {% for post in posts %}
    <article class="media content-section">
        <div class="media-body">
            <div class="article-metadata">
                <a class="mr-2" href="#">{{ post.author }}</a>
                <small class="text-muted">{{ post.date_posted }}</small>
            </div>
            <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
        </div>
    </article>
    {% endfor %}
```
- To use the posts and title variables as in the above, the context must be supplied to the home / about functions in blog/views.py
- Change the links in the html to be dynamic by adding `href="{% url 'blog_home' %}"` to get the link to blog_home. This name is taken from the name argument of the paths inside urls.py

# Episode 4.
Create admin user for login page at http://localhost:8000/admin/login/

```
python manage.py migrate
(optional?) python manage.py makemigrations
python manage.py createsuperuser
```

Fill in required information, log in, and then from there add/edit users and update permissions
