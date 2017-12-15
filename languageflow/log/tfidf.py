import json
from os.path import join
import joblib
from underthesea.util.file_io import write


class TfidfLogger:
    """
    Analyze and save tfidf results
    """

    @staticmethod
    def log(model_folder, binary_file="tfidf.transformer.bin", log_folder="analyze"):
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
        content = json.dumps(list(tfidf.vocabulary_.keys()), ensure_ascii=False)
        write(join(log_folder, "tfidf.json"), content)
