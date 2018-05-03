# import codecs
# try:
#     codecs.lookup('mbcs')
# except LookupError:
#     ascii = codecs.lookup('ascii')
#     func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
#     codecs.register(func)

from setuptools import setup, find_packages


requirements = [
	'scipy', 'numpy', 'scikit-learn', 'Click'
]

test_requirements=[
	'behave'
]

setup(
	name='irisvmpy',
	version='0.0.1',
	description='SVM classifier for iris data-set',
	author='Michal Dyzma',
	author_email='mdyzma@gmail.com',
    url ='https://github.com/mdyzma/jenkins-python-test',
    download_url='https://github.com/mdyzma/jenkins-python-test/archive/0.0.1.tar.gz',
	license='MIT',
	packages=find_packages(),
	install_requires=requirements,
	entry_points={
    	'console_scripts': [
        		'irisvmpy = irisvmpy.iris:cli',
        	],
        },
	classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
      ],
	zip_safe=False
)