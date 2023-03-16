import os
from datetime import datetime
from pywebwrap.pywebwrap import Wrap
from tempt import tempt

#############################
#       requirements:       #
#   pip install pywebwrap   #
#############################

# Define the path of the template and output file
template_path = "path/to/template.html"
output_path = "path/to/desired/path/of/output.html"  # full path

# Define a template
post_template = tempt(template_path)

# Define the dynamic content
post_content = {
    "title": "tempt Example",
    "author": "Dekel Cohen",
    "date": datetime.now().strftime("%B %d, %Y %I:%M %p"),
    "content": "<pre>Hello, and welcome to tempt! This is an example.</pre>",  # Add pre-formatted content
    "css_url": "path/to/desired/path/of/style.css"  # CSS file - full path
}

# Render the template with the dynamic content
post_output = post_template.render(post_content)

# Create the directory if it doesn't exist
output_dir = "path/to/desired/path/of"  # The same as {{ output_path }} but without the filename - full path
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Write the rendered output to the output file
with open(output_path, "w") as f:
    f.write(post_output)

# Run it with "pywebwrap" - check it out: https://github.com/Dcohen52/pywebwrap
if os.path.exists(output_path):
    app = Wrap(output_path)
    app.run()
else:
    with open(output_path, "w") as f:
        f.write(post_output)
    app = Wrap(output_path)
    app.run()

# And voilà