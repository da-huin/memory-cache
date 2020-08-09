
# Use this command for deploy.
#   python3 setup.py sdist bdist_wheel && python3 -m twine upload --skip-existing dist/*

import io
from setuptools import find_packages, setup

setup(name='memory_cache',
      version='1.0.0',
      description='It is a package that simply stores and uses a cache in memory.',
      long_description="Please refer to the https://github.com/da-huin/memory_cache",
      long_description_content_type="text/markdown",
      url='https://github.com/da-huin/memory_cache',
      download_url= 'https://github.com/da-huin/memory_cache/archive/master.zip',
      author='JunYeong Park',
      author_email='dahuin000@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      classifiers=[
          'Programming Language :: Python :: 3',
    ]
)


