from setuptools import setup, find_namespace_packages
setup(
    name='docassemble.HarborIntakeDemo',
    version='0.1.0',
    description='Harbor: a branded intake and simulated LegalServer handoff',
    author='Lemma Legal Consulting',
    packages=find_namespace_packages(include=['docassemble.*']),
    package_data={'docassemble.HarborIntakeDemo': ['data/questions/*.yml', 'data/static/*']},
    install_requires=[],
    zip_safe=False,
)
