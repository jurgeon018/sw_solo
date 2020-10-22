# from setuptools import find_packages, setup 
from distutils.core import setup

version      = '0.2'
name         = 'sw_solo'
url          = f'https://github.com/jurgeon018/{name}'
download_url = f'{url}/archive/{version}.tar.gz'

with open('requirements.txt') as f:
  requires = f.read().splitlines()

setup(
  name             = name,
  packages         = ['.'], 
  # packages         = find_packages(),
  version          = version,
  license          = 'MIT',   
  description      = 'Starway singleton django package',   
  author           = 'Andrew Mendela',                   
  author_email     = 'jurgeon018@gmail.com',      
  url              = url,
  download_url     = download_url,    
  install_requires = requires,
  # include_package_data=True,
  keywords         = [
    'singleton', 'solo', 'django',
  ],   
  classifiers      = [
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)


