from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
        name='edrpou',
        version='1.0',
        author='Pavlo Yaremchuk (pablissimo77)',
        author_email='pablissimo77@gmail.com',
        url='https://github.com/pablissimo77/edrpou-iin-validation/',
        description='EDRPOU-IIN validation',
        keywords='edrpou єдрпоу іін iin',
        license='MIT',
        packages=[],
        include_package_data=True,
     )