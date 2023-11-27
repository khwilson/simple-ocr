from contextlib import contextmanager, nullcontext
from pathlib import Path
import subprocess
import tempfile
from typing import Iterator

from .config import get_config


@contextmanager
def extract_pages_from_pdf(
    pdf_path: Path | str,
    extract_path: Path | str | None = None,
    imagemagick_path: Path | str | None = None,
) -> Iterator[Path]:
    """
    Given a PDF, extract its pages as PNG files into `extract_path`,
    or if `extract_path` is None, a temporary directory.

    If to a temporary directory, note that these files will be deleted
    immediately after leaving the context.
    """
    imagemagick_path = Path(imagemagick_path or get_config().imagemagick_path)
    pdf_path = Path(pdf_path)
    extract_path_cm = nullcontext(extract_path) if extract_path else tempfile.TemporaryDirectory()
    with extract_path_cm as tmpdir:
        tmpdir = Path(tmpdir)
        subprocess.run(
            [
                str(imagemagick_path),
                str(pdf_path),
                str(tmpdir / pdf_path.with_suffix(".png").name)
            ],
            check=True,
        )
        yield tmpdir
