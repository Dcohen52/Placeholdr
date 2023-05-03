# Changelog
## Version 0.0.2 (Current)
* Added the `PlaceholdrError` exception class for raising custom errors in the module.
* Added the `_raise_template_error` method to raise custom exceptions with a custom error message and error type.
* Updated the `_render_control_structures` method.
* Added the `_render_ifnot` method..
* Added the `_render_if` method.
* Added more filters.
* Improved overall code structure and organization for easier future development.
* Added support for macros and autoescape features.

## Version 0.0.1 - Initial release
* Initial implementation of the `Placeholdr` class.
* Supported basic template functionality, including variable substitution, template inheritance, includes, control structures, and filters.
* The class allowed dynamic substitution of values in templates.
* Methods included `_parse_blocks`, `_render_includes`, `_render_blocks`, `_render_control_structures`, and `_render_filters`.
