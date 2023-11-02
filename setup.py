from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A package to graph vernier graph'
LONG_DESCRIPTION = 'A package to draw graphs from vernier grahical analysis'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="vernier_data_compiler", 
        version=VERSION,
        author="Archie Macdonald",
        author_email="SE6446@Cyber-wizard.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pandas","numpy","scipy","json","time","math","matplotlib","statistics","re"], # add any additional packages that 
        
        keywords=['python', 'matplotlib'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)