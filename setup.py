from distutils.core import setup

version = '0.1'

with open('requirements.txt') as f:
  requires = f.read().splitlines()

setup(
  name = 'django-sw-solo', 
  packages = ['.'], 
  version = version,
  license='MIT',   
  description = 'Starway singleton django package',   
  author = 'jurgeon018',                   
  author_email = 'jurgeon018@gmail.com',      
  url = 'https://github.com/jurgeon018/sw_solo',   
  download_url = 'https://github.com/jurgeon018/sw_solo/archive/v_01.tar.gz',    
  keywords = ['singleton', 'solo', 'django'],   
  install_requires=requires,
  classifiers=[
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


