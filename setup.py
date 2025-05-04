from setuptools import setup, find_packages

setup(
    name='mistral_cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'mistral=mistral_cli.cli:main',
        ],
    },
)
