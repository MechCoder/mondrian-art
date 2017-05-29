try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='mondrian-art',
      version='0.1',
      description='Generate modern art using mondrian processes.',
      license='BSD',
      author='Manoj Kumar',
      packages=['mondrian_art'],
      install_requires=["numpy", "matplotlib"]
)
