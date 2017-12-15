import json
from os.path import join
import joblib
from underthesea.util.file_io import write


class TfidfLogger:
    """
    Analyze and save tfidf results
    """

    @staticmethod
    def log(model_folder, binary_file="tfidf.transformer.bin",
            log_folder="analyze"):
        """
        Parameters
        ----------
        model_folder : string
            folder contains binaries file of model
        binary_file : string
            file path to tfidf binary file
        log_folder : string
            log folder
        """
        file = join(model_folder, binary_file)
        tfidf = joblib.load(file)
        output = []

        for token in tfidf.vocabulary_:
            index = tfidf.vocabulary_[token]
            value = tfidf.idf_[index]
            ngram = len(token.split(" "))
            output.append({
                "token": token,
                "ngram": ngram,
                "idf": value
            })
        output = sorted(output, key=lambda item: item["idf"])
        content = json.dumps(output, ensure_ascii=False)
        write(join(log_folder, "tfidf.json"), content)
