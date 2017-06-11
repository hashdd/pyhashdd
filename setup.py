# coding: utf-8
"""
setup.py
@brad_anton

License:
 
Copyright 2015 hashdd.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



# from __future__ import unicode_literals

from codecs import open   # pylint:disable=redefined-builtin
from os.path import dirname, join, exists, basename, isfile
from os import listdir
import sys
import re
import platform

from setuptools import setup, find_packages
from shutil import copyfile

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Operating System :: OS Independent',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

def get_libs(t):
    """
    t -- type either 'algorithms' or 'features'
    """
    p = join('libs', '{}'.format(platform.system().lower()), 'x86_{}'.format(platform.architecture()[0][:2]), '{}'.format(t))
    if exists(p):
        return [join(p, f) for f in listdir(p) if isfile(join(p, f))]
    return []


def copy_libs():
    package_data = []
    for t in ['algorithms', 'features']:
        libs = get_libs(t)
        for l in libs:
            dst = join('hashdd', '{}'.format(t), basename(l))
            print 'Prep: Copying {} to {}'.format(l, dst)
            copyfile(l, dst)
            package_data.append(join('{}'.format(t), basename(l)))

    print package_data
    return package_data


def main():
    base_dir = dirname(__file__)
    install_requires = open('requirements.txt').read().splitlines()
    with open('hashdd/version', 'r', encoding='utf-8') as config_py:
        version = re.search(r'^\s+__version__\s*=\s*[\'"]([^\'"]*)[\'"]', config_py.read(), re.MULTILINE).group(1)

    setup(
        name='hashdd',
        version=version,
        description='Official hashdd Python SDK',
        long_description=open(join(base_dir, 'README.md'), encoding='utf-8').read(),
        author='hashdd',
        url='https://www.hashdd.com',
        packages=find_packages(exclude=['bin', 'docs', 'libs']),
        package_data={ 'hashdd': copy_libs() },
        #zip_safe=False,
        scripts=['bin/hashdd'],
        install_requires=install_requires,
        classifiers=CLASSIFIERS,
        keywords=['hashdd', 'pyhashdd', 'hash database'],
        license=open('LICENSE').read()
    )


if __name__ == '__main__':
    main()
