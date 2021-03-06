# -*- coding: utf-8 -*-
"""\
This has been created to work in conjunction with mr.anderson, but can be used
for individual use.
"""
import os
import sys
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

name = 'buildout.autoextras'
version = '1.2.rc2'

install_requires = [
    'setuptools',
    'zc.buildout',
    'zc.recipe.egg',
    ]
test_requires = [
    'zope.testing',
    ]
if sys.version_info < (2, 7,):
    test_requires.append('unittest2')
extras_require = {'test': test_requires}

long_description = '\n\n'.join([
        read('README.md'),
        read('docs', 'changes.rst'),
])

DEV_STATES = [
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
]
if version.find('a') >= 0:
    state = 0
elif version.find('b') >= 0:
    state = 1
else:
    state = 2
development_status = DEV_STATES[state]

setup(
    name=name,
    version=version,
    author="Michael Mulich",
    author_email="michael.mulich@gmail.com",
    description="zc.buildout extension to automatically include requirement extras",
    long_description=long_description,
    url="http://bitbucket.org/pumazi/buildout.autoextras",
    classifiers=["Framework :: Plone",
                 "Programming Language :: Python",
                 "Intended Audience :: Developers",
                 development_status,
                 ],
    keywords='plone buildout',
    license='GPL',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    zip_safe=False,
    entry_points="""
[zc.buildout.extension]
default = buildout.autoextras.extension:extension
""",
    )
