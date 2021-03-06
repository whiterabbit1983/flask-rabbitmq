from setuptools import setup, find_packages

setup(
    name='flask-rabbitmq',
    version='0.0.1',
    author='Pushy',
    author_email='1437876073@qq.com',
    url='https://github.com/PushyZqin/flask-rabbitmq',
    description=u'Let rabbitmq use flask development more easy! ! !',
    packages=find_packages(
        exclude=[
            "*test*",
            "*build*",
            "*__pycache__*"
        ]
    ),
    include_package_data=True,
    install_requires=['pika']
)