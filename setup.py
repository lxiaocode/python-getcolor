from setuptools import setup

setup(
    name = 'getcolor',
    version = '0.0.1',
    packages = ['getcolor'],
    entry_points = {
        'console_scripts': [
            'getcolor = getcolor.core:main'
        ]
    },
    install_requires=[
        'fire>=0.4.0',
        'pynput>=1.7.3',
        'PyScreeze>=0.1.27',
    ]
)