import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-markdownfield", # Replace with your own username
    version="0.0.1",
    author="Luke Rogers",
    author_email="luke@dmptr.com",
    description="Markdown Field for Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmptrluke/django-markdownfield",
    project_urls={
        "Bug Tracker": "https://github.com/dmptrluke/django-markdownfield/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    requires=[
          'django>=2.2',
          'bleach',
          'markdown',
          'shortuuid',
          'dataclasses; python_version == "3.6"',
    ]
)
