from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name='RPI-ST7789',
      version='0.0.4a',
      description='Library to control an ST7789 240*240 TFT LCD display.',
      long_description=open('README.md').read() + '\n' + open('CHANGELOG.txt').read(),
      long_description_content_type='text/markdown',
      license='MIT',
      author='Russell bayley',
      author_email='russell.bayley@gmail.com',
      classifiers=classifiers,
      url='https://github.com/rusconi/Rpi-ST7789',
      packages=find_packages())
