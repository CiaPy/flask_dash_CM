{% extends "bootstrap/base.html" %}

{% block title %} {{title}} {% endblock %}

{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
             data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/"><img src="https://i.pinimg.com/originals/ba/64/05/ba6405af6bb050ef22b5864a789b652d.png" alt="greta" height="36"></a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
                <li><a href="/Sign">Sign in</a></li>

            </ul>
        </div>
    </div>
</div>
{% endblock %}