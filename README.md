# PDF2MD

Convert PDF files into Markdown while extracting images.

## Installation

```bash
pip install -e .
```

## Usage

```bash
pdf2md input.pdf output.md --images-dir assets
```

## Output

```text
output.md
assets/
├── image_1.png
├── image_2.png
└── ...
```