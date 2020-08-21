from setuptools import setup

import pip_autoremove


setup(
    name="python3-pip-autoremove",
    version=pip_autoremove.__version__,
    description="Remove a package and its unused dependencies(Supports Python3)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    py_modules=["pip_autoremove"],
    license='Apache License 2.0',
    url='https://github.com/enjoysoftware/pip3-autoremove',
    entry_points="""
    [console_scripts]
    pip3-autoremove = pip_autoremove:main
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
