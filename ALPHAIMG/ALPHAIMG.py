from pathlib import Path

from .ALPHAJPG import ALPHAJPG

class ALPHAIMG():

    @staticmethod
    def load(filepath, loader_func=None):
        if filepath.suffix == '.jpg':
            return ALPHAJPG.load ( str(filepath), loader_func=loader_func )
        else:
            return None
