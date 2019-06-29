from setuptools import setup

with open("README.md", 'r') as fh:
    long_description = fh.read()


setup(
    name='wtforms-validators',
    version='1.0.0',
    author='Akhil Harihar',
    author_email="hariharakhil@gmail.com",
    description="Validators for wtforms package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akhilharihar/wtforms-validators",
    packages=['wtforms_validators'],
    python_requires='>=3.0',
    install_requires=[
        'WTForms',
        'dnspython',
        'is_disposable_email'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable"
    ]
)
