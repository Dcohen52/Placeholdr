# tempt
tempt is a flexible and powerful Python template engine designed to make it easy to substitute placeholders in templates with actual values. With its simple syntax, tempt allows developers to create dynamic and customizable templates for web applications. This document will cover the features of tempt, how to use it, and how to contribute to the project.

### Features:

* Templating: tempt provides basic template functionality, including variable substitution, template inheritance, includes, control structures, and filters.
* Simple syntax: The syntax used by tempt is simple, using double curly braces (e.g. {{ variable }}) for placeholders and special syntax (e.g. {% if condition %} ... {% endif %}) for control structures.
* Inheritance: tempt supports template inheritance, allowing developers to create a base template with common elements and then extend it with more specific templates.
* Customizable: tempt is highly extensible, allowing developers to add their own filters and control structures as needed.

### How to use:
Using tempt is simple and straightforward. To get started, follow these steps:

1. Install tempt by running ```pip install tempt```.
2. Import tempt in your project using ```from tempt.tempt import tempt```.
3. Create an instance of tempt by passing the path to the template file as an argument: ```template = tempt('path/to/template.html')```.
4. Call the render method on the template object, passing in a dictionary of values to substitute in the template: ```output = template.render({'variable': 'value'})```.

### PYPI
https://pypi.org/project/tempt/.

### Contributing:
tempt is an open-source project and contributions are welcome. If you'd like to contribute, please contact me.
