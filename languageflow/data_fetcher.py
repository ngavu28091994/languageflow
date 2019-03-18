import shutil

from languageflow.file_utils import cached_path, CACHE_ROOT
from pathlib import Path

REPO = {
    "VNESES": {
        "cache_dir": "datasets/LTA",
        "filepath": "VNESEScorpus.txt"
    },
    "VNTQ_SMALL": {
        "cache_dir": "datasets/LTA",
        "filepath": "VNTQcorpus-small.txt"
    },
    "VNTQ_BIG": {
        "cache_dir": "datasets/LTA",
        "filepath": "VNTQcorpus-big.txt"
    },
}


class DataFetcher:
    @staticmethod
    def download_data(data):
        if data not in REPO:
            print("No matching distribution found for '{data}'")
            return

        filepath = REPO[data]["filepath"]
        cache_dir = REPO[data]["cache_dir"]
        filepath = Path(CACHE_ROOT) / cache_dir / filepath
        if Path(filepath).exists():
            print(f"Data is already existed: '{data}' in {filepath}")
            return

        if data == "VNESES":
            url = "https://www.dropbox.com/s/m4agkrbjuvnq4el/VNESEcorpus.txt?dl=1"
            cached_path(url, cache_dir=cache_dir)
            shutil.move(Path(CACHE_ROOT) / cache_dir / "VNESEcorpus.txt?dl=1",
                        Path(CACHE_ROOT) / cache_dir / filepath)

        if data == "VNTQ_SMALL":
            url = "https://www.dropbox.com/s/b0z17fa8hm6u1rr/VNTQcorpus-small.txt?dl=1"
            cached_path(url, cache_dir=cache_dir)
            shutil.move(Path(CACHE_ROOT) / cache_dir / "VNTQcorpus-small.txt?dl=1",
                        Path(CACHE_ROOT) / cache_dir / filepath)

        if data == "VNTQ_BIG":
            url = "https://www.dropbox.com/s/t4z90vs3qhpq9wg/VNTQcorpus-big.txt?dl=1"
            cached_path(url, cache_dir=cache_dir)
            shutil.move(Path(CACHE_ROOT) / cache_dir / "VNTQcorpus-big.txt?dl=1",
                        Path(CACHE_ROOT) / cache_dir / filepath)
