# Simple OCR Demo

A simple CLI to tesseract and imagemagick that:
  * Take a PDF
  * Performs a simple OCR on each page
  * Dumps the results to a series of text files, one per page

## Requirements

You must have tesseract and imagemagick installed. If they are not on your path, then add `IJF_TESSERACT_PATH` and `IJF_IMAGEMAGICK_PATH` as environment variales with the absolute path to the relevant binaries.

## Example

```bash
ijf ocr data/Trans-Legislation-Summary-Oct-2023.pdf
```

You should now see a folder of text files at `data/Trans-Legislation-Summary-Oct-2023.pdf.ocr`, one per page.

## License

MIT
