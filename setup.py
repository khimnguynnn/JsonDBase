from setuptools import setup, find_packages

setup(
    name='jsondbase',
    version='1.0.7',
    author='khiemndd',
    description='like database with json file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)