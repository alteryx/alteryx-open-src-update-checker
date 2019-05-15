from setuptools import find_packages, setup

setup(
    name='featuretools_update_client',
    version='0.0.1',
    packages=find_packages(),
    author='Feature Labs, Inc.',
    author_email='support@featurelabs.com',
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7'
    ],
    install_requires=open('requirements.txt').readlines(),
    setup_requires=open('setup-requirements.txt').readlines(),
    python_requires='>=2.7, <4',
    test_suite='featuretools_update_client/tests',
    tests_require=open('test-requirements.txt').readlines(),
    include_package_data=True,
    long_description_content_type='text/markdown',
    entry_points={
        "featuretools_initialize": [
            "initialize = featuretools_update_client:client"
        ],
    }
)
