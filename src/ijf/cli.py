from pathlib import Path
import click
from dotenv import load_dotenv

from ijf.tesseract import simple_ocr

from .config import set_config_from_env
from .imagemagick import extract_pages_from_pdf


load_dotenv()
set_config_from_env()


@click.group()
def cli():
    """ Commands for the IJF's tooling """


@cli.command("ocr")
@click.argument("pdffile", type=click.Path(exists=True, dir_okay=False))
@click.option("--output-directory", "-o", default=None, help="Where to dump the OCRs")
def ocr_command(pdffile: str, output_directory: str | None = None):
    pdffile: Path = Path(pdffile)

    if not output_directory:
        output_directory = pdffile.with_suffix(".pdf.ocr")
    else:
        output_directory = Path(output_directory)

    # TODO: Figure out cast
    output_directory: Path = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=False)

    with extract_pages_from_pdf(pdffile) as tmpdir:
        for filename in tmpdir.glob("*.png"):
            simple_ocr(filename, output_directory)


if __name__ == "__main__":
    cli()
