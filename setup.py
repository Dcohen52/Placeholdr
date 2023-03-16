from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'tempt is a flexible and powerful Python template engine for dynamic substitution of values in templates.'
LONG_DESCRIPTION = '''tempt is a flexible and powerful Python template engine designed to make it 
easy to substitute placeholders in templates with actual values. 

### Supported features:
* template inheritance. 
* control structures. 
* filters

With a simple syntax, tempt makes it easy to create dynamic and customizable templates for web applications. The 
engine is safe to use and undergoes ongoing development to meet our needs as web developers.

For more information and examples, check out tempt's documentation ( coming soon) and Github 
repository at https://github.com/Dcohen52/tempt.'''

# Setting up
setup(
    name="tempt",
    version=VERSION,
    author="Dekel Cohen",
    author_email="<dcohen52@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'template engine', 'templating', 'web development', 'template', 'dynamic templates', 'template inheritance', 'control structures', 'filters', 'reusability'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)