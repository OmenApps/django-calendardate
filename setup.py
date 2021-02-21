import os
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as fh:
    readme = fh.read()

setup(
    name="django-calendardate",
    version="0.1.0",
    description="A calendar model with date metadata for querying against.",
    long_description=readme,
    author="Jack Linke",
    author_email="jack@watervize.com",
    url="http://github.com/OmenApps/django-calendardate/",
    packages=find_packages(),
    package_data={
        "django_calendardate": [],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
    ],
)
