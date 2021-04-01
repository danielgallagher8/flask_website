from setuptools import setup, find_packages

import website

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
requirements = []

setup(
      name="website",
      version=website.__version__,
      author="Daniel Gallagher",
      author_email="daniel-gallagher@outlook.com",
      description="Website",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/danielgallagher8/website.git",
      packages=find_packages(),
      install_requires=requirements,
      classifiers=[
              "Programming Language :: Python :: 3.7",
              "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
              ],
      )
