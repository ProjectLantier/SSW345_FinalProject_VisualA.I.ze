class TextboxUI(SearchResult):
    def __init__(self, result):
        super().__init__(result)
        self.text = result.get_result()