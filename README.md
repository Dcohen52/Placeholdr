# Placeholdr
The Placeholdr template engine is a robust and versatile Python library, specifically designed to facilitate the seamless integration of placeholders within templates and their subsequent substitution with actual values. Boasting an intuitive syntax and an extensive array of features, tempt empowers developers to craft dynamic, tailor-made templates for a wide variety of web applications.

## Features:
* **Templating:** Placeholdr provides advanced template functionality, including variable substitution, template inheritance, includes, control structures, filters, custom tags, and macros.
* **Simple syntax:** The syntax used by Placeholdr is simple and intuitive, using double curly braces (e.g., {{ variable }}) for placeholders, and special syntax (e.g., {% if condition %} ... {% endif %}) for control structures.
* **Custom Syntax:** Placeholdr allows developers to customize the syntax used for placeholders and control structures, enabling them to use any syntax they want.
* **Inheritance:** Placeholdr supports template inheritance, allowing developers to create a base template with common elements and then extend it with more specific templates.
* **Includes:** Placeholdr allows for including other template files within a template using the {% include "path/to/template" %} syntax, promoting modularity and reusability.
* **Control Structures:** Placeholdr offers a variety of control structures like {% if condition %}, {% endif %}, {% for item in iterable %}, and {% endfor %} to enable dynamic content generation.
* **Filters:** Placeholdr supports filters for manipulating variables within the template (e.g., {{ variable | filter_name }}), providing a powerful way to format and process data.
* **Custom Tags and Macros:** Placeholdr allows developers to create custom tags and macros using {% call macro_name() %} and {% endcall %}, enhancing the flexibility and functionality of the engine.
* **Automatic HTML Escaping:** Placeholdr automatically escapes HTML special characters to prevent security vulnerabilities such as XSS attacks.
* **Customizable:** Placeholdr is highly extensible, allowing developers to add their own filters, control structures, tags, and macros as needed, tailoring the engine to fit their specific requirements.

### Get started:

1. First, create an HTML template file, e.g., template.html:

``` html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ css_url }}">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>

    {% if author %}
    <p><strong>Author:</strong> {{ author }}</p>
    {% endif %}

    {% if date %}
    <p><strong>Date:</strong> {{ date }}</p>
    {% endif %}

    {% if items %}
    <ul>
        {% for item in items %}
        <li>{{ item }}</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No items available.</p>
    {% endif %}

    {% if content %}
    <p>{{ content }}</p>
    {% else %}
    <p>No content available.</p>
    {% endif %}
</body>
</html>

```

2. Next, write a Python script to use the Placeholdr framework:

``` python
from Placeholdr.placeholder import Placeholdr

template = Placeholdr("full/path/to/template.html")

context = {
    "title": "Placeholdr Example",
    "author": "Author",
    "date": datetime.now().strftime("%B %d, %Y %I:%M %p"),
    "content": "<pre>Hello, and welcome to Placeholdr! This is an example.</pre>",
    "items": ['Item 1', 'Item 2', 'Item 3'],
    "css_url": "../styles/style.css"
}

output = template.render(context)

print(output)

```


3. When you run the script, the Placeholdr framework will render the template file template.html with the provided context data and produce the following output:

``` html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/Users/dekelcohen/Library/CloudStorage/GoogleDrive-dcohen52@gmail.com/My Drive/Development/Python/jsonLang/tempt/templates/styles/style.css">
    <title>Placeholdr Example</title>
</head>
<body>
    <h1>Placeholdr Example</h1>
    <p><strong>Author:</strong>Author</p>
    <p><strong>Date:</strong> November 26, 2023 11:19 AM</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    <p><pre>Hello, and welcome to Placeholdr! This is an example.</pre></p>
</body>
</html>

```

### PYPI
https://pypi.org/project/Placeholdr/.

### Contributing:
Placeholdr is an open-source project and contributions are welcome!
