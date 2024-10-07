from setuptools import setup, find_packages

setup(
    name='lab1',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Тут вкажеш залежності, якщо такі є
    entry_points={
        'console_scripts': [
            'factorial=lab1.lab1:main',  # Вказуєш точку входу: ім'я скрипта і функцію
        ],
    },
)
