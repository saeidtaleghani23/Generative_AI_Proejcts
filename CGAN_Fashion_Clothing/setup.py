from setuptools import setup, find_packages

setup(
    name='cgan_fashion_clothing_data',  
    version='0.1.0',
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[
        'tensorflow==2.17.0',
        'numpy==1.26.4',
        'matplotlib==3.9.0',
        'keras==3.4.1'
    ],
    description='Implementing Conditional GAN (CGAN) using Fashion Clothing Dataset',
    author='Saeid Taleghani',  
    author_email='stalegha@uwaterloo.ca', 
    url='https://github.com/saeidtaleghani23/CGAN_Fashion_Clothing_Data',  
)
