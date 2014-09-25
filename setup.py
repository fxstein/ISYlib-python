
# python setup.py --dry-run --verbose install

import os.path
from setuptools import setup, find_packages
from distutils.command.install_scripts import install_scripts

from distutils.core import setup

class install_scripts_and_symlinks(install_scripts):
    '''Like install_scripts, but also replicating nonexistent symlinks'''
    def run(self):
	print "=============install_scripts_and_symlinks run"
	install_scripts.run(self)
	# Replicate symlinks if they don't exist
	print self
	print "data_files = ",  dir( self.distribution.data_files)
	print type(self.distribution.data_files)
	print self.distribution.data_files
	for script in self.distribution.scripts:
	    print  "\n---script = ",script
	    if os.path.islink(script):
		target  = os.readlink(script)
		newlink = os.path.join(self.install_dir, os.path.basename(script))
		if not os.path.exists(newlink):
		    print "++++++++++", target, " -> ", newlink
		    # os.symlink(target, newlink)


setup(
    name='ISYlib',
    version='0.1.20140704',
    author='Peter Shipley',
    author_email='Peter.Shipley@gmail.com',
    packages=find_packages(),
    scripts=[ 'bin/isy_find.py', 'bin/isy_log.py', 'bin/isy_nestset.py',
		'bin/isy_net_wol.py', 'bin/isy_progs.py',
		'bin/isy_showevents.py', 'bin/isy_web.py' ],
    data_files=[
#	('examples', ['bin/isy_find.py', 'bin/isy_progs.py',
#		'bin/isy_log.py', 'bin/isy_net_wol.py']),
        ('bin', ['bin/isy_nodes.py', 'bin/isy_var.py']) ],
    url='https://github.com/evilpete/ISYlib-python',
    license='BSD',
    description='Python API for the ISY home automation controller.',
    long_description=open('README.txt').read(),
    cmdclass = { 'install_scripts': install_scripts_and_symlinks }
)




