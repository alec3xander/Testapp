from setuptools import setup, find_packages

setup(
    name='TestApp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Añade aquí las dependencias, por ejemplo: 'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'testapp=simple_test:main',
        ],
    },
)
