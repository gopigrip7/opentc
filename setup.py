from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

__version__ = ""
exec(open('opentc/version.py').read())

setup(
    name='opentc',
    version=__version__,
    description='A text classification engine using machine learning and designed as client-server architecture',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Filters'
    ],
    keywords='machine learning cnn svm bayesian',
    url='https://github.com/cahya-wirawan/opentc',
    author='Cahya Wirawan',
    author_email='Cahya.Wirawan@gmail.com',
    license='MIT',
    packages=find_packages('.'),
    package_dir={'': '.'},
    install_requires=[
        'numpy',
        'pyparsing',
        'PyYAML',
        'scikit-learn',
        'scipy',
        'tensorflow'
    ],
    scripts=['bin/opentc', 'bin/opentcd'],
    data_files=[('/etc/opentc', ['config/opentc.yml', 'config/logging.yml'])],
    include_package_data=True,
    zip_safe=False)