from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('test_requirements.txt','r') as f:
    test_requirements = f.read().splitlines()

setup(
    name = 'aibs_ephys_pink_noise',
    version = '0.1.0',
    description = """Creates the pink noise stimuli used in the noise1, noise2, and ramp to rheo stimulus used in the Allen Institute for Brain Science electrophysiology pipeline.""",
    author = "Corinne Teeter",
    author_email = "corinnet@alleninstitute.org",
    url = 'http://stash.corp.alleninstitute.org/scm/~corinnet/aibs.ephys_pink_noise',
    packages = find_packages(),
    include_package_data=True,
    install_requires = requirements,
    entry_points={
          'console_scripts': [
              'aibs.ephys_pink_noise = aibs.ephys_pink_noise.__main__:main'
        ]
    },
    license="Allen Institute Software License",
    setup_requires=['pytest-runner'],
    tests_require = test_requirements
)
