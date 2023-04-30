from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='charmr',
    version='1.0.11',
    description='A Magical AI File Converter',
    url='https://github.com/harlev/charmr',
    author='Ron Harlev',
    author_email='harlev@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    license='MIT',
    python_requires='>=3.8',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'charmr=charmr.main:main'
        ]
    }
)
