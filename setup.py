from setuptools import find_packages, setup

install_requires = [
    "Flask==1.1.2",
    "requests==2.24.0"
]

setup(
    name="walmart_tech_assesment",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    python_requires=">=3.8",
)