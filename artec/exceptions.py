class NotJsonFile (FileNotFoundError):
    def __init__(self, verbose:bool) -> None:
        super().__init__("> Provided Source isn't valid JSON file")
        self.errno = 101
        if not verbose : return
        print("> Provided Source isn't valid JSON file")
        print("> Reverting to default structure")

def NoSource():
    print("> No Source Provided")
    print("> Using default structure")

class NotValidJson(KeyError):
    def __init__(self, verbose:bool) -> None:
        super().__init__("> Provided Json file format is incorrect")
        self.errno = 102
        if not verbose : return
        print("> Provided Json file format is incorrect")
