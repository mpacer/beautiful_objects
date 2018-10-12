from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
name = 'hearts_full_of_pride'

version_ns = {}
with open(os.path.join(here, name, '_version.py')) as f:
    exec(f.read(), {}, version_ns)

extras_require = {
    'test': ['pytest']
}
extras_require['dev'] = ['check_manifest'] + extras_require['test']

setup(
    name=name,
    packages=[name],
    version=version_ns['__version__'],
    author='M Pacer',
    author_email='mpacer@berkeley.edu',
    url='https://github.com/mpacer/beautiful_objects/'
    python_requires = '>=3.6',
    install_requires=[
        "vdom",
        "sympy",
        "cairosvg",
        "numpy"
        ],
    extras_require=extras_require,
)
