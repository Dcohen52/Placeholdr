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
