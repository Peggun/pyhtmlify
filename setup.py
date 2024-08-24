from setuptools import setup, find_packages

setup(
    name="pyhtmlify",
    version="0.1.5",
    long_description=open("README.md").read(),
    description="HTML in Pure Python",
    long_description_content_type='text/markdown',
    author="Peggun",
    author_email="peggundev@gmail.com",
    url="https://github.com/Peggun/pyhtml",
    packages=find_packages(where="src"),  # Find packages inside 'src'
    package_dir={"": "src"},  # Tell setuptools that packages are under 'src'
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "certifi==2024.7.4",
        "charset-normalizer==3.3.2",
        "docutils==0.21.2",
        "idna==3.7",
        "importlib_metadata==8.4.0",
        "jaraco.classes==3.4.0",
        "jaraco.context==6.0.1",
        "jaraco.functools==4.0.2",
        "keyring==25.3.0",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "more-itertools==10.4.0",
        "nh3==0.2.18",
        "pkginfo==1.10.0",
        "Pygments==2.18.0",
        "readme_renderer==44.0",
        "requests==2.32.3",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==13.7.1",
        "setuptools>=64",
        "urllib3==2.2.2",
        "zipp==3.20.0",
        "beautifulsoup4==4.12.3"
    ],
    entry_points={
        "console_scripts": [
            "pyhtmlify=pyhtmlify.cli.cli:main",  # Command 'pyhtmlify'
        ],
    },
)
