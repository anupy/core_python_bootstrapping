from setuptools import setup

setup(name='project',
      version='0.1.0',
      packages=['project'],
      entry_points={
          'console_scripts': [
              'project = project.__main__:main'
          ]
      },
      )
