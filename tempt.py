import re


class tempt:
    """A template engine that allows you to substitute placeholders in a template file with actual values.

    This class supports basic template functionality, including variable substitution, template inheritance, includes,
    control structures, and filters. It uses a simple syntax for defining templates, with placeholders denoted by double
    curly braces (e.g. {{ variable }}) and control structures denoted by special syntax (e.g. {% if condition %} ... {%
    endif %}).

    To use this class, create an instance with the path to the template file, and then call the `render` method with a
    dictionary of values to substitute in the template.
    """

    def __init__(self, template_file):
        with open(template_file) as f:
            self.template_string = f.read()
        self.blocks = self._parse_blocks(self.template_string)

    def render(self, context):
        output = self.template_string
        for key, value in context.items():
            output = output.replace("{{ " + key + " }}", str(value))
        output = self._render_includes(output, context)
        output = self._render_blocks(output, context)
        output = self._render_control_structures(output, context)
        output = self._render_filters(output, context)
        return output

    def _parse_blocks(self, template_string):
        # Parse template blocks
        block_re = r"{%\s*block\s+(\w+)\s*%}(.*?){%\s*endblock\s*%}"
        blocks = re.findall(block_re, template_string, flags=re.DOTALL)
        return dict(blocks)

    def _render_includes(self, template_string, context):
        # Render included templates
        include_re = r"{%\s*include\s+\"(.*?)\"\s*%}"
        match = re.search(include_re, template_string)
        while match:
            include_path = match.group(1)
            include_template = tempt(include_path)
            include_output = include_template.render(context)
            template_string = template_string.replace(match.group(0), include_output)
            match = re.search(include_re, template_string)
        return template_string

    def _render_blocks(self, template_string, context):
        # Render template blocks
        for block_name, block_content in self.blocks.items():
            block_re = r"{{%\s*block\s+{}\s*%}}(.*?){{%\s*endblock\s*%}}".format(block_name)
            block_output = block_content
            match = re.search(block_re, template_string, flags=re.DOTALL)
            if match:
                block_output = match.group(1)
            template_string = re.sub(block_re, block_output, template_string, flags=re.DOTALL)
        return template_string

    def _render_control_structures(self, template_string, context):
        # Render control structures
        if_re = r"{%\s*if\s+(.*?)\s*%}(.*?){%\s*endif\s*%}"
        for match in re.finditer(if_re, template_string, flags=re.DOTALL):
            condition = match.group(1)
            body = match.group(2)
            if eval(condition, {}, context):
                output = self.render({"__body__": body, **context})
                template_string = template_string.replace(match.group(0), output)
            else:
                template_string = template_string.replace(match.group(0), "")
        return template_string

    def _render_filters(self, template_string, context):
        # Render filters
        filter_re = r"\|\s*(\w+)\s*(:\s*(.*))?"
        for match in re.finditer(filter_re, template_string):
            filter_name = match.group(1)
            filter_args = match.group(3) or ""
            if filter_name in context:
                filter_func = context[filter_name]
                filter_output = filter_func(match.string, filter_args)
                template_string = template_string.replace(match.group(0), filter_output)
        return template_string
