# Copyright (C) 2014-2022 Panos Kittenis.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, version 2.1.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from setuptools import setup, find_packages

setup(name='parallel-ssh',
      version="1",
      description='Asynchronous parallel SSH library',
      long_description=open('README.rst').read(),
      author='Panos Kittenis',
      author_email='zuboci@yandex.com',
      url="https://github.com/ParallelSSH/parallel-ssh",
      license='LGPLv2.1',
      packages=find_packages(
          '.', exclude=('embedded_server', 'embedded_server.*',
                        'tests', 'tests.*',
                        '*.tests', '*.tests.*')
      ),
      install_requires=[
          'gevent', 'ssh2-python312', 'ssh-python'],
      )
