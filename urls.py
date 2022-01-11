""" {{ camel_case_app_name }} URLs. """

# Django
from django.urls import path

# Views
# from .views

urlpatterns = [
    # API {{ camel_case_app_name }}
    path(
        "{{ app_name }}/api/",
        include(
            ("your_project_name.{{ app_name }}.api.urls", "{{ app_name }}-api"), namespace="{{ app_name }}-api"
        ),
    ),
]
