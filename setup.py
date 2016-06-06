from setuptools import setup

version = '1.2'

setup(
    name='rtfunicode',
    version=version,
    description="Encoder for unicode to RTF 1.5 command sequences",
    long_description='\n'.join([
        open("README.rst").read(),
        open('CHANGES.rst').read(),
    ]),
    keywords='rtf',
    author='Martijn Pieters',
    author_email='mj@zopatista.com',
    url='http://pypi.python.org/pypi/rtfunicode',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    py_modules=['rtfunicode'],
    test_suite='tests.test_suite',
)
