# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("/Users/sam/Documents/code/smithii/")
# Your mock repo
mock_repo = git.Repo("/Users/sam/Documents/code/work-tracking-repo")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['samuel.dkater@gmail.com', 'samk@singulargenomics.com'])
importer.import_repository()
