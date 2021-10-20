from setuptools import setup, find_packages

setup(
    name="tp2", 
    packages=find_packages(where="src"), 
    extras_require=dict(tests=['pytest']),
    package_dir={"": "src"},
)