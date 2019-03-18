import shutil

from languageflow.file_utils import cached_path, CACHE_ROOT
from pathlib import Path

REPO = {
    "VNESES": {
        "cache_dir": "datasets/LTA",
        "filepath": "VNESEScorpus.txt"
    }
}
class DataFetcher:
    @staticmethod
    def download_data(data):
        if data == "VNESES":
            filepath = REPO[data]["filepath"]
            cache_dir = REPO[data]["cache_dir"]
            filepath = Path(CACHE_ROOT) / cache_dir / filepath
            if Path(filepath).exists():
                print(f"Data is already existed: '{data}' in {filepath}")
            else:
                url = "https://www.dropbox.com/s/m4agkrbjuvnq4el/VNESEcorpus.txt?dl=1"
                cached_path(url, cache_dir=cache_dir)
                shutil.move(Path(CACHE_ROOT) / cache_dir / "VNESEcorpus.txt?dl=1",
                    Path(CACHE_ROOT) / cache_dir / filepath)

