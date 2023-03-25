from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="sunny",
      author_email="sunny.savita@ineuron.ai",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )