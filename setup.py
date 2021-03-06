import setuptools

from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("digital_thought_commons/version", "r") as fh:
    version_info = fh.read()

setuptools.setup(
    name="digital_thought_commons",
    version=version_info,
    author="Digital Thought",
    author_email="matthew@digital-thought.org",
    description="My standard python libs for doing things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Digital-Thought/commons",
    install_requires=[
        "requests>=2.24.0",
        "PyYaml>=5.3.1",
        "pytz>=2020.1",
        "pytz-convert>=0.2.9",
        "user-agents>=2.2.0",
        "numpy>=1.19.2",
        "pandas>=1.1.3",
        "sklearn",
        "stringcase>=1.2.0",
        "IPy>=1.0",
        "colorlog>=4.4.0",
        "beautifulsoup4>=4.9.3",
        "xlsxwriter>=1.3.7",
        "geoip2>=4.1.0",
        "regex>=2015.10.29",
        "pysocks",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "selenium==3.141.0",
        "elasticsearch"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    packages=find_packages(exclude=('tests', 'docs', 'sampleConfigs')),
    python_requires='>=3.8',
    include_package_data=True
)
