import setuptools
import celeste as i

with open(i.__file__, encoding='utf8') as f:
    for line in f:
        if line.startswith('"""  # '):
            break

setuptools.setup(
    name=i.__name__,
    version=line[7:-1],
    author='竹永康',
    author_email='<gqylpy@outlook.com>',
    license='MIT',
    url='http://gqylpy.com',
    project_urls={'Source': 'https://github.com/gqylpy/celeste'},
    description='The celeste.',
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    py_modules=[i.__name__],
    python_requires='>=3.8, <4',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Object Brokering',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ]
)
