from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in product_wizard/__init__.py
from product_wizard import __version__ as version

setup(
	name="product_wizard",
	version=version,
	description="New Development",
	author="Thirvusoft",
	author_email="thirvusoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
