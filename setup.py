from setuptools import find_packages, setup

setup(
    name='flask_stream',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    'Flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
