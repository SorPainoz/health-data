from setuptools import setup, find_packages

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest', ]

setup(
    author="Igor Piroli",
    author_email='piroligor@gmail.com',

    name='gg-dump',
    version='0.1.0',

    description='The goal of the tool is dowload and process data from sources like google fit (and fitbit) so that data packages can be made available to apps such as icig or simply for data science pourposes',

    entry_points={
        'console_scripts': [
            'hdd=health_data_dumper.health_data_dumper_tool:cli',
        ],
    },

    license="GNU General Public License v3",

    # py_module=['health_data_dumper'],
    packages=find_packages(),
    include_package_data=True,
    # packages=find_packages(include=['health_data_dumper']),

    install_requires=requirements,

    setup_requires=setup_requirements,

    test_suite='tests',
    tests_require=test_requirements,

    url='https://github.com/SorPainoz/health-data',
    # zip_safe=False,
)
