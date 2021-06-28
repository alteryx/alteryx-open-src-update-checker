from os import path

from setuptools import find_packages, setup

dirname = path.abspath(path.dirname(__file__))
with open(path.join(dirname, 'README.md')) as f:
    long_description = f.read()

setup(
    name='alteryx_open_src_update_checker',
    author='Alteryx, Inc.',
    author_email='support@featurelabs.com',
    license='BSD 3-clause',
    version='2.1.0',
    description='an update checker for alteryx open source libraries',
    url='https://github.com/FeatureLabs/alteryx-open-src-update-checker/',
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
         'Programming Language :: Python :: 3.9'
    ],
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3.7, <4',
    test_suite='alteryx_open_src_update_checker/tests',
    tests_require=open('test-requirements.txt').readlines(),
    keywords='update check data science machine learning alteryx',
    include_package_data=True,
    entry_points={
        "featuretools_initialize": [
            "initialize = alteryx_open_src_update_checker.functions:initialize"
        ],
        "alteryx_open_src_initialize": [
            "initialize = alteryx_open_src_update_checker.functions:initialize"
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
