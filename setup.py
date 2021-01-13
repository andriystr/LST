import setuptools

with open('requirements.txt') as f:
	requires = list(f)

with open('README.md') as f:
    description = f.read()

setuptools.setup(
    name='lst',
    version='0.3.0',
    author='Andriy Stremeluk',
    author_email='astremeluk@gmail.com',
    description='Declarative Scraping Tools',
    long_description=description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/andriystr/LST',
    packages=setuptools.find_packages(exclude=['test*']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=requires,
    python_requires='>=3.5'
)
