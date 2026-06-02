from setuptools import setup

setup(
    name='corral',
    version='0.3.1',
    py_modules=['corral'],
    entry_points={
        'console_scripts': [
            'corral=corral:main',
        ],
    },
    description='Corral every tmux session and Slurm job across your cluster nodes into one live dashboard',
)
