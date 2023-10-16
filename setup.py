from setuptools import setup, find_packages, Command
import sys, os

class AppendPaths(Command):
    user_options = [
        ('path=', None, "Path to editable github installs")
    ]

    def finalize_options(self):
        pass

    def initialize_options(self):
        self.path = os.getcwd()

    def run(self):
        sys.path.append(os.path.join(self.path, "src", "taming-transformers"))
        sys.path.append(os.path.join(self.path, "src", "clip"))

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
    cmdclass={"setpath" : AppendPaths}
)
