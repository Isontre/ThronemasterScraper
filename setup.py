from setuptools import setup, find_packages, find_namespace_packages 

setup(name='thronescraper',
      version='0.0',
      description='A html scraper for statistical analysis of thronemaster.net',
      url='https://github.com/Isontre/ThronemasterScraper',
      author='Isontre',
      author_email='vlasovequation@gmail.com',
      license='MIT',
      packages=find_packages() + find_namespace_packages(),
      install_requires=[
          'bs4',
          'requests'
      ],
      python_requires='>=3.6.*',
      zip_safe=False,
      scripts=['scripts/update_6pgames.py'])