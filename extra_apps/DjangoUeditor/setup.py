from distutils.core import setup

setup(
    name='MxShop',
    version='',
    packages=['', '', 'goods', 'goods.migrations', 'trade', 'trade.migrations', 'users', 'users.migrations',
              'user_operation', 'user_operation.migrations', 'xadmin', 'xadmin.views', 'xadmin.plugins',
              'xadmin.migrations', 'xadmin.templatetags', 'DjangoUeditor', '', 'views', 'plugins', 'migrations',
              'templatetags'],
    package_dir={'': 'extra_apps/DjangoUeditor'},
    url='',
    license='',
    author='monstar',
    author_email='',
    description=''
)
