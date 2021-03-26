import setuptools 

setuptools.setup(
name='slack-bot-pydocs-search',
version='0.1',
description='Python implementation of slack bot',
url='https://github.com/menakakarichiyappakumar/slack-bot-pydocs-search.git',
author='Menaka',
author_email='menakakarichiyappakumar@gmail.com',
packages=['code'],
install_requires=['slack',
                'flask',
                'dotenv',
                'bs4']
)
