from setuptools import setup, find_packages

import template

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
requirements = []

setup(
      name="template",
      version=template.__version__,
      author="Daniel Gallagher",
      author_email="daniel-gallagher@outlook.com",
      description="Template",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/danielgallagher8/template.git",
      packages=find_packages(),
      install_requires=requirements,
      classifiers=[
              "Programming Language :: Python :: 3.7",
              "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
              ],
      )
