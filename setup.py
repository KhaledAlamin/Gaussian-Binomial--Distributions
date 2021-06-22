from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["matplotlib", "numpy", "math"]


setup(name='gaus_binom_dist',
      version='0.1',
      description='Gaussian & Binomial distributions',
      long_description = readme,
      install_requires = requirements,
      packages=['gaus_binom_dist'],
      zip_safe=False)
