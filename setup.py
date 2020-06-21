from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'terminal_viewer',         # How you named your package folder (MyLib)
  packages = ['terminal_viewer'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Package for printing images in terminal',   # Give a short description about your library
  long_description =long_description,
  long_description_content_type = 'text/markdown',
  author = 'Hardeep SIngh',                   # Type in your name
  author_email = 'hardeep0khalsa122@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Hardeepsingh980/terminal_viewer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Hardeepsingh980/terminal_viewer.git',    # I explain this later on
  keywords = ['terminal','image','terminal_image','terminal_viewer'],   # Keywords that define your package best
  install_requires=[
      'numpy',
      'Pillow',
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)