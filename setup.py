from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Placeholdr is a flexible and powerful Python template engine for dynamic substitution of values in ' \
              'templates.'
LONG_DESCRIPTION = '''The Placeholdr template engine is a robust and versatile Python library, specifically designed 
to facilitate the seamless integration of placeholders within templates and their subsequent substitution with actual 
values. Boasting an intuitive syntax and an extensive array of features, Placeholdr empowers developers to craft dynamic, 
tailor-made templates for a wide variety of web applications.


For more information and examples, check out Placeholdr's documentation ( coming soon) and Github 
repository at https://github.com/Dcohen52/Placeholdr.'''

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
              'template inheritance', 'control structures', 'filters', 'reusability', 'custom tags', 'macros', 'Placeholdr'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
