from setuptools import setup, find_packages, Command

class AppendPaths(Command):
    def run(self):
        import sys, os
        DIR = os.getcwd()
        sys.path.append(os.path.join(DIR, "src", "taming-transformers"))
        sys.path.append(os.path.join(DIR, "src", "clip"))

setup(
    name='latent-diffusion',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
