from git import Repo
from . import logger
from os import listdir



class repository(Repo):

    def __init__(self, path, name) -> Repo:
        self.name = name
        self.repo_path = path
        self.repo = Repo.init(path)
        logger.info("Creating Git Repository")
    
    def add(self):
        files = listdir(self.repo_path)
        files.remove('.git')
        self.repo.index.add(files)
        logger.info("Adding the skeleton structure")
        self.repo.index.commit(f"{self.name} : initial commit.")
        logger.info("Committing the files")
            
