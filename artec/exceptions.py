class NotJsonFile(FileNotFoundError):
    def __init__(self, verbose: bool) -> None:
        super().__init__("> Provided Source isn't valid JSON file")
        self.errno = 101
        if not verbose:
            return
        print("> Provided Source isn't valid JSON file")
        print("> Reverting to default structure")

    def __str__(self):
        return "> Provided Source isn't valid JSON file"


class NoSource(ValueError):
    def __init__(self, verbose: bool) -> None:
        super().__init__("> No Source Provided")
        self.errno = 102
        if not verbose:
            return
        print("> No Source Provided")
        print("> Using default structure")

    def __str__(self):
        return "> No Source Provided"


class NotValidJson(KeyError):
    def __init__(self, verbose: bool) -> None:
        super().__init__("> Provided Json file format is incorrect")
        self.errno = 103
        if not verbose:
            return
        print("> Provided Json file format is incorrect")

    def __str__(self):
        return "> Provided Json file format is incorrect"


class InValidTemplate(KeyError):
    def __init__(self, verbose: bool) -> None:
        super().__init__("> Provided Template argument is invalid")
        self.errno = 104
        if not verbose:
            return
        print("> Provided Template argument is invalid")

    def __str__(self):
        return "> Provided Template argument is invalid"


if __name__ == "__main__":
    pass
