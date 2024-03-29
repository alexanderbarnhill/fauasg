from setuptools import setup, find_packages

setup(
    name='fauasg',
    version='0.0.2',
    description='A set of tools developed by the Animal Speech Group at FAU',
    url='https://github.com/alexanderbarnhill/fauasg',
    author='Alexander Barnhill',
    author_email='alexander.barnhill@fau.de',
    license='MIT',
    packages=find_packages(),
    install_requires=['pytorch>=1.11.0',
                      'numpy',
                      'matplotlib',
                      'scikit-learn',
                      'lightning',
                      'scikit-image',
                      'omegaconf',
                      'opencv-python',
                      'wandb',
                      ],

    classifiers=[
    ],
)
