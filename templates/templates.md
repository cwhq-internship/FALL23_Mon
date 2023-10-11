# Getting Started with templates

## What are Jinja templates?
Flask uses the jinja template library to render templates of html. Jinja templates are smart html files that allow us to tell flask what content we want to render to the web browser. In this application we have a base template known as layout.html which is the primary parent template in this flask application. If you look inside that file you will notice blocks of code that look something like the following.
```
  {% block content %}
  {% endblock %}
``` 
Each of of the blocks in this template is a place you can yield/add html code through a child template.

## Creating your first template
To create your first template simple create an html file in the templates folder first. Next you can copy in paste the following code snippet as a boiler plate to get started.
```
{% extends 'layout.html' %}

{% block styles %}
{% endblock %}

{% block content %}
{% endblock %}

{% block scripts %}
{% endblock %}
```
The `extends` keyword tells flask which parent template to use. If you do want to use another parent template simple change the file name to the layout template of your choice. The `block styles` allows you to import or add any styles directly to the parent template of layout.html. It is recommended to create a new stylesheet inside of the static/stylesheets folder for each new screen and import that stylesheet instead of writing your styles directly in your template. The `block content` is meant to render the content of your screen. This is the primary place you should add your content. Lastly you have `block scripts` which is used to import scripts or write javascript code. It is recommended to write your javascript in separate files in the static/javascript folder and import the scripts when needed.

