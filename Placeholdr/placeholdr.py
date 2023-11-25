import re
import datetime
import html


class Placeholdr:

    def __init__(self, template_file):
        self.open_tag = "{{"
        self.close_tag = "}}"
        self.block_re_pattern = r"{{%\\s*block\\s+(\\w+)\\s*%}}(.*?){{%\\s*endblock\\s*%}}"
        self.include_re_pattern = r"{{%\\s*include\\s+\"(.*?)\"\\s*%}}"
        self._update_regex_patterns()
        self.macros = {}
        self.custom_tags = {}
        self.template_string = ""
        self.blocks = {}
        with open(template_file) as f:
            self.template_string = f.read()
        self.blocks = self._parse_blocks(self.template_string)

    def specify_syntax(self, open_tag, close_tag):
        self.open_tag = open_tag
        self.close_tag = close_tag
        self._update_regex_patterns()

    def _update_regex_patterns(self):
        # Use placeholders for the parts you want to format
        self.block_re = self.block_re_pattern.format(self.open_tag.replace("{", "{{").replace("}", "}}"),
                                                     self.close_tag.replace("{", "{{").replace("}", "}}"))
        self.include_re = self.include_re_pattern.format(self.open_tag.replace("{", "{{").replace("}", "}}"),
                                                         self.close_tag.replace("{", "{{").replace("}", "}}"))
        # Update other regular expressions similarly...

    def _raise_template_error(self, error_message, error_type="Error"):
        raise PlaceholdrError(f"{error_type}: {error_message}")

    def render(self, context):
        output = self.template_string
        for key, value in context.items():
            placeholder_pattern = re.escape(self.open_tag) + r"\s*" + re.escape(key) + r"\s*" + re.escape(
                self.close_tag)
            output = re.sub(placeholder_pattern, str(value), output)
        output = self._render_includes(output, context)
        output = self._render_blocks(output, context)
        output = self._render_control_structures(output, context)
        output = self._render_filters(output, context)
        output = self._render_macros(output, context)
        output = self._render_autoescape(output, context)
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
            include_template = Placeholdr(include_path)
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

    def _render_for(self, template_string, context):
        for_re = r"{%\s*for\s+(\w+)\s+in\s+(.*?)\s*%}(.*?){%\s*endfor\s*%}"
        for match in re.finditer(for_re, template_string, flags=re.DOTALL):
            loop_var = match.group(1)
            iterable = eval(match.group(2), {}, context)
            body = match.group(3)
            output = ""
            for item in iterable:
                loop_context = {loop_var: item, **context}
                output += self.render({"__body__": body, **loop_context})
            template_string = template_string.replace(match.group(0), output)
        return template_string

    def _render_control_structures(self, template_string, context):
        # Render control structures
        control_re = r"{%\s*(\w+)\s*(.*?)\s*%}(.*?){%\s*end\1\s*%}"
        for match in re.finditer(control_re, template_string, flags=re.DOTALL):
            tag_name = match.group(1)
            tag_args = match.group(2)
            body = match.group(3)

            if tag_name in self.custom_tags:
                output = self.custom_tags[tag_name](tag_args, body, context)
                template_string = template_string.replace(match.group(0), output)
            else:
                raise ValueError(f"Unknown control tag: {tag_name}")

        return template_string

    def _render_if(self, template_string, context):
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

    def _render_ifnot(self, template_string, context):
        ifnot_re = r"{%\s*ifnot\s+(.*?)\s*%}(.*?){%\s*endif\s*%}"
        for match in re.finditer(ifnot_re, template_string, flags=re.DOTALL):
            condition = match.group(1)
            body = match.group(2)
            if eval(condition, {}, context) == False:
                output = self.render({"__body__": body, **context})
                template_string = template_string.replace(match.group(0), output)
            else:
                template_string = template_string.replace(match.group(0), "")
        return template_string

    def _render_macros(self, template_string, context):
        def render_macro(macro_name, macro_args, context):
            if macro_name not in self.macros:
                raise ValueError(f"Unknown macro: {macro_name}")

            macro_func, macro_arg_names = self.macros[macro_name]
            macro_kwargs = {arg_name: arg_value for arg_name, arg_value in zip(macro_arg_names, macro_args)}
            return macro_func(context, **macro_kwargs)

        macro_call_re = r"{%\s*call\s+(\w+)\((.*?)\)\s*%}"
        for match in re.finditer(macro_call_re, template_string):
            macro_name = match.group(1)
            macro_args_str = match.group(2)
            macro_args = [arg.strip() for arg in macro_args_str.split(',')]
            output = render_macro(macro_name, macro_args, context)
            template_string = template_string.replace(match.group(0), output)

        return template_string

    def _render_autoescape(self, template_string, context):
        autoescape_re = r"{{\s*([^\|].*?)\s*}}"
        for match in re.finditer(autoescape_re, template_string):
            variable_name = match.group(1)
            if variable_name in context:
                variable_value = context[variable_name]
                if isinstance(variable_value, str):
                    escaped_value = html.escape(variable_value)
                    template_string = template_string.replace(match.group(0), escaped_value)
        return template_string

    def _render_filters(self, template_string, context):
        # Render filters
        filter_re = r"{{\s*(\w+)(\s*\|\s*(\w+)(\s*:\s*(.*))?)?\s*}}"
        for match in re.finditer(filter_re, template_string):
            variable_name = match.group(1)
            filter_name = match.group(3)
            filter_args = match.group(5) or ""

            if variable_name in context:
                variable_value = context[variable_name]
                if filter_name:
                    if filter_name == "upper" and isinstance(variable_value, str):
                        variable_value = variable_value.upper()
                    elif filter_name == "lower" and isinstance(variable_value, str):
                        variable_value = variable_value.lower()
                    elif filter_name == "title" and isinstance(variable_value, str):
                        variable_value = variable_value.title()
                    elif filter_name == "trim" and isinstance(variable_value, str):
                        variable_value = variable_value.strip()
                    elif filter_name == "length":
                        variable_value = len(variable_value)
                    elif filter_name == "default":
                        if variable_value is None or variable_value == "":
                            variable_value = filter_args
                    elif filter_name == "replace":
                        if isinstance(variable_value, str):
                            old, new = filter_args.split(":")
                            variable_value = variable_value.replace(old, new)
                    elif filter_name == "date":
                        if isinstance(variable_value, datetime.datetime):
                            variable_value = variable_value.strftime(filter_args)
                    elif filter_name == "truncate" and isinstance(variable_value, str):
                        max_length = int(filter_args) if filter_args.isdigit() else len(variable_value)
                        variable_value = variable_value[:max_length]

                output = str(variable_value)
                template_string = template_string.replace(match.group(0), output)
        return template_string


class PlaceholdrError(Exception):
    """Base class for exceptions in this module."""
    pass
