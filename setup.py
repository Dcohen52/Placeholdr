from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Placeholdr is a flexible and powerful Python template engine for dynamic substitution of values in ' \
              'templates.'
LONG_DESCRIPTION = '''# Placeholdr - Python Template Engine

Placeholdr is a robust and versatile Python library designed to facilitate seamless integration of placeholders within templates and their subsequent substitution with dynamic values. With its intuitive syntax and extensive feature set, Placeholdr empowers developers to craft dynamic and tailor-made templates for a wide range of web applications.

## Key Features

Placeholdr comes packed with a variety of features to enhance your template creation and management:

- **Variable Substitution**: Support for various syntaxes like `{{ variable }}`, `[[ variable ]]`, `< variable >`, etc.
- **Template Inheritance**: Efficiently manage templates with `{% block block_name %}` and `{% endblock %}` tags.
- **Includes**: Easily include external templates using `{% include "path/to/template" %}`.
- **Control Structures**: Intuitive control structures including `{% if condition %}`, `{% endif %}`, `{% for item in iterable %}`, and `{% endfor %}`.
- **Filters**: Apply filters within templates for variable manipulation (e.g., `{{ variable | filter_name }}`).
- **Custom Tags and Macros**: Extend functionality with `{% call macro_name() %}` and `{% endcall %}`.
- **HTML Auto-Escaping**: Automatically escape HTML special characters to enhance security.

## Getting Started

The library is in its early stages of development (version 0.0.4), and we are continuously working to add more features and improve its functionality. We welcome feedback and contributions from the community.

For upcoming documentation, examples, and updates, keep an eye on Placeholdr's GitHub repository: [https://github.com/Dcohen52/Placeholdr](https://github.com/Dcohen52/Placeholdr).'''

# Setting up
setup(
    name="Placeholdr",
    version=VERSION,
    author="Dekel Cohen",
    author_email="<dcohen52@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'template engine', 'templating', 'web development', 'template', 'dynamic templates',
              'template inheritance', 'control structures', 'filters', 'reusability', 'custom tags', 'macros',
              'Placeholdr'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
