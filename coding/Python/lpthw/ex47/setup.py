try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description':'My Project',
    'author':'Hossein.M',
    'url':'https://github.com/h0ssein2011',
    'download_url':'https://github.com/h0ssein2011/projects',
    'author_email':'h0ssein2011@yahoo.com',
    'version':'0.1',
    'install_requires':['nose'],
    'Packages':['ex47'],
    'scripts':[],
    'name':'ex47'
}

setup(**config)#
