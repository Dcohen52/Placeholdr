# tempt
tempt is a flexible and powerful Python template engine designed to make it easy to substitute placeholders in templates with actual values. With its simple syntax, tempt allows developers to create dynamic and customizable templates for web applications. This document will cover the features of tempt, how to use it, and how to contribute to the project.

### Features:

* Templating: tempt provides basic template functionality, including variable substitution, template inheritance, includes, control structures, and filters.
* Simple syntax: The syntax used by tempt is simple, using double curly braces (e.g. {{ variable }}) for placeholders and special syntax (e.g. {% if condition %} ... {% endif %}) for control structures.
* Inheritance: tempt supports template inheritance, allowing developers to create a base template with common elements and then extend it with more specific templates.
* Customizable: tempt is highly extensible, allowing developers to add their own filters and control structures as needed.

### Get started:

1. First, create an HTML template file, e.g., template.html:

```
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

2. Next, write a Python script to use the tempt framework:

```
from tempt import tempt

# Create an instance of the tempt class with the path to the template file
template = tempt("full/path/to/template.html")

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


3. When you run the script, the tempt framework will render the template file template.html with the provided context data and produce the following output:

```
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
https://pypi.org/project/tempt/.

### Contributing:
tempt is an open-source project and contributions are welcome!
