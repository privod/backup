from setuptools import setup, find_packages
from os.path import join, dirname

import project

setup(
    name='backup',
    version=project.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    install_requires=[
        'PyDrive',
        'config'        # Устанавливается локально (./lib/config-1.0.tar.gz) смотри ./cmd/install.cmd
    ],
    entry_points={
        'console_scripts': [
            'upload = project.backup:upload',
        ]
    },
    # include_package_data=True,
    # test_suite='tests',
)