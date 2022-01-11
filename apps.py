"""{{ camel_case_app_name }} app."""

# Django
from django.apps import AppConfig


class {{ camel_case_app_name }}AppConfig(AppConfig):
    """{{ camel_case_app_name }} app config."""

    name = "your_project_name.{{ app_name }}"
    verbose_name = "{{ camel_case_app_name }}"
