import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='gpa.lu',
    version='1.0.2',
    author='MonkeySkid',
    url='https://github.com/MonkeySkid/Gpa.lu',
    description='Asynchronous api wrapper for the disposable email service gpa.lu',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['gpalu', 'gpalu.models'],
)
