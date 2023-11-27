from contextlib import contextmanager, nullcontext
from pathlib import Path
import subprocess
import tempfile
from typing import Iterator

from .config import get_config


def simple_ocr(
    png_path: Path | str,
    output_directory: Path | str,
    tesseract_path: Path | str | None = None,
) -> Iterator[Path]:
    """
    Given a PDF, extract its pages as PNG files into `extract_path`,
    or if `extract_path` is None, a temporary directory.

    If to a temporary directory, note that these files will be deleted
    immediately after leaving the context.
    """
    tesseract_path = Path(tesseract_path or get_config().tesseract_path)
    png_path = Path(png_path)
    output_directory = Path(output_directory)

    subprocess.run(
        [
            str(tesseract_path),
            str(png_path),
            str(output_directory / png_path.with_suffix("").name)
        ],
        check=True,
    )

