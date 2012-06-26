from fabric.api import cd
from fabric.api import run
from fabric.operations import sudo

SITE_CHECKOUT = '/srv/www/david-huie.com/personal_site/'

def deploy():
	"""Deploys my website! Yay! ^.^"""

	# My checkout has root permissions, motherfucker.
	with cd(SITE_CHECKOUT):
		sudo('git fetch origin')
		sudo('git checkout origin/master')
		sudo('git reset --hard HEAD')

	sudo('apache2ctl restart')
