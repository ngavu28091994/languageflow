class NumberRemover:
    """
    Remove numbers in documents
    """
    def __init__(self):
        numbers = "0123456789"
        self.remover = str.maketrans("", "", numbers)

    def _remove(self, document):
        return document.translate(self.remover)

    def transform(self, raw_documents):
        """
        Remove number in each document

        Parameters
        ----------
        raw_documents : iterable
            An iterable which yields either str, unicode

        Returns
        -------
        X : iterable
            cleaned documents
        """
        return [self._remove(document) for document in raw_documents]
