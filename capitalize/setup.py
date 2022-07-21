from setuptools import setup
setup(name='capitalize',
      version='1.0',
      # list folders, not files
      packages=['capitalize',
                'capitalize.test'],
      scripts=['bin/cap_script.py'],
      package_data={'capitalize': ['data/*']},
      )