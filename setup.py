from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='backend_manager',
    version="1.0",
    description="Manage processes executions and synchronise data between cluster and a local node.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/as641651/BackendManager',
    author='Aravind Sankaran',
    author_email='aravindsankaran22@gmail.com',
    packages= find_packages(), # finds packages inside current directory
    classifiers=[
        "Programming Language :: Python  :: 3",
    ],
    install_requires=[
      "paramiko",
    ],
    python_requires=">3",

)