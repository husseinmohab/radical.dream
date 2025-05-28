from setuptools import setup, find_packages

with open('requirements.txt', encoding='utf-8') as freq:
    requirements = freq.readlines()

setup_args = {}

setup_args['name']                 = "hydraa"
setup_args['version']              = "1.0.0"
setup_args['scripts']              = ['hydraa/services/caas_manager/kubernetes/bootstrap_kubernetes.sh']
setup_args['packages']             = find_packages()
setup_args['package_data']         = {'': ['*.sh', '*.yaml'],}
setup_args['python_requires']      = '>=3.6'
setup_args['install_requires']     = requirements

setup(**setup_args)
