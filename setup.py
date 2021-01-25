from setuptools import setup

setup(
    name='qais',
    version='1.0',
    description='Query Automation in Incremental Search',
    url='http://github.com/ld258166011/qais',
    license='GPL',
    packages=['qais'],
    package_dir={'qais': 'qais'},
    package_data={'qais': ['models/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['qais = qais.__main__:main']
    },
    install_requires=[
		'numpy>=1.15.1',
        'pandas>=0.23.4',
		'xpinyin>=0.5.7',
        'PyAutoGUI>=0.9.50',
		'scapy>=2.4.3',
        'selenium>=3.141.0'
    ],
    zip_safe=False
)
