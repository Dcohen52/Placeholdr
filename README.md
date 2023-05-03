# Placeholdr
The Placeholdr template engine is a robust and versatile Python library, specifically designed to facilitate the seamless integration of placeholders within templates and their subsequent substitution with actual values. Boasting an intuitive syntax and an extensive array of features, tempt empowers developers to craft dynamic, tailor-made templates for a wide variety of web applications.

## Features:
* **Templating:** Placeholdr provides advanced template functionality, including variable substitution, template inheritance, includes, control structures, filters, custom tags, and macros.
* **Simple syntax:** The syntax used by Placeholdr is simple and intuitive, using double curly braces (e.g., {{ variable }}) for placeholders, and special syntax (e.g., {% if condition %} ... {% endif %}) for control structures.
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
  <head>
    <title>{{ title }}</title>
  </head>
  <body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
  </body>
</html>
```

2. Next, write a Python script to use the Placeholdr framework:

``` python
from Placeholdr import Placeholdr

# Create an instance of the Placeholdr class with the path to the template file
template = Placeholdr("full/path/to/template.html")

# Define a dictionary of values to substitute in the template
context = {
  "title": "Example Page",
  "heading": "This is an example page",
  "content": "This is some example content"
}

# Render the template with the context dictionary
output = template.render(context)

# Print the output
print(output)

```


3. When you run the script, the Placeholdr framework will render the template file template.html with the provided context data and produce the following output:

``` html
<!DOCTYPE html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>This is an example page</h1>
    <p>This is some example content</p>
  </body>
</html>
```

### PYPI
https://pypi.org/project/Placeholdr/.

### Contributing:
Placeholdr is an open-source project and contributions are welcome!
