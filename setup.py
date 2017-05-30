try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='mondrian-art',
      version='0.1.2',
      description='Generate modern art using mondrian processes.',
      license='BSD',
      maintainer='Manoj Kumar',
      maintainer_email="mks542@nyu.edu",
      packages=['mondrian_art'],
      install_requires=["numpy", "matplotlib"]
)
