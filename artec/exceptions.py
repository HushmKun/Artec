from . import logger


class NotJsonFile(FileNotFoundError):
    def __init__(self) -> None:
        super().__init__("> Provided Source isn't valid JSON file")
        self.errno = 101
        logger.warning("Provided Source isn't valid JSON file")
        logger.info("Reverting to default structure")

    def __str__(self):
        return "> Provided Source isn't valid JSON file"


class NoSource(ValueError):
    def __init__(self) -> None:
        super().__init__("> No Source Provided")
        self.errno = 102
        logger.warning("No Source Provided")
        logger.info("Using default structure")

    def __str__(self):
        return "> No Source Provided"


class NotValidJson(KeyError):
    def __init__(self) -> None:
        super().__init__("> Provided Json file format is incorrect")
        self.errno = 103
        print(self)
        logger.warning("Provided Json file format is incorrect")
        logger.error("Artec shut down unexpectedly.")

    def __str__(self):
        return "> Provided Json file format is incorrect"


class InValidTemplate(KeyError):
    def __init__(self) -> None:
        super().__init__("> Provided Template argument is invalid")
        self.errno = 104
        logger.warning("Provided Template argument is invalid")
        logger.error("Artec shut down unexpectedly.")

    def __str__(self):
        return "> Provided Template argument is invalid"


class GitError(OSError):
    def __init__(self , e = None) -> None:
        super().__init__("> Git has encountered a problem")
        self.errno = 105
        logger.warning("Git has encountered a problem")
        logger.error(e)
        logger.error("Artec shut down unexpectedly.")

    def __str__(self):
        return "> Git has encountered a problem"
