from distutils.core import setup

setup(
    name='balanced-dicephrase',
    version='0.0.2',
    packages=[''],
    url='https://github.com/alexiasa/balanced-dicephrase/',
    license='',
    author='alexiasa',
    author_email='type.err0r@protonmail.com',
    description='A Python program to generate easier to type diceware passwords',
    install_requires=['diceware', 'requests'],
    entry_points={
            'console_scripts': [
                'diceware = diceware:main',
            ],
            'diceware_random_sources': [
                'system = diceware.random_sources:SystemRandomSource',
                'realdice = diceware.random_sources:RealDiceRandomSource',
                # add more sources of randomness here...
            ],
    },
)
