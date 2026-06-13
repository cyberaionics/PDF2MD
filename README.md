# PDF2MD

A CLI tool that converts PDF documents into Markdown while extracting embedded images into a local folder and automatically linking them inside the generated Markdown.

---

## Features

- Extracts text from PDFs
- Extracts images to a user-defined folder
- Generates clean Markdown output
- Automatically inserts image references
- Preserves reading order
- Detects headings based on font size
- Supports large PDFs with progress bars
- Works on Linux, macOS, and Windows

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/pdf2md.git
cd pdf2md
```

### 2. Create a Virtual Environment (Recommended)

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Package

```bash
pip install -e .
```

Verify installation:

```bash
pdf2md --help
```

---

## Quick Start

Convert a PDF using the default image directory (`assets`):

```bash
pdf2md input.pdf output.md
```

Example:

```bash
pdf2md notes.pdf notes.md
```

Output:

```text
.
├── notes.md
└── assets/
    ├── page_1_img_1.png
    ├── page_2_img_1.png
    └── ...
```

---

## Using a Custom Image Directory

```bash
pdf2md input.pdf output.md --images-dir images
```

Example:

```bash
pdf2md lecture_notes.pdf lecture_notes.md --images-dir images
```

Output:

```text
.
├── lecture_notes.md
└── images/
    ├── page_1_img_1.png
    ├── page_1_img_2.png
    └── ...
```

---

## Example Markdown Output

Generated Markdown:

```md
# Introduction

This is a sample paragraph extracted from the PDF.

![Image](assets/page_1_img_1.png)

## Neural Networks

Neural networks are inspired by biological neurons.

![Image](assets/page_2_img_1.png)
```

This Markdown can be viewed in:

- VS Code
- Obsidian
- GitHub
- MkDocs
- Docusaurus
- Any CommonMark-compatible viewer

---

## CLI Reference

### Basic Usage

```bash
pdf2md INPUT_PDF OUTPUT_MD
```

### Full Syntax

```bash
pdf2md INPUT_PDF OUTPUT_MD --images-dir IMAGE_FOLDER
```

### Arguments

| Argument | Description |
|-----------|-------------|
| `INPUT_PDF` | Source PDF file |
| `OUTPUT_MD` | Output Markdown file |

### Options

| Option | Description | Default |
|----------|-------------|----------|
| `--images-dir` | Folder for extracted images | `assets` |

---

## Typical Workflow

### Convert

```bash
pdf2md textbook.pdf textbook.md
```

### Open Markdown

```bash
code textbook.md
```

### View Structure

```text
project/
├── textbook.md
└── assets/
    ├── page_1_img_1.png
    ├── page_3_img_2.png
    └── ...
```

### Commit to Git

```bash
git add textbook.md assets/
git commit -m "Add converted PDF notes"
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_renderer.py
```

---

## Troubleshooting

### `pdf2md: command not found`

Reinstall the package:

```bash
pip install -e .
```

Verify:

```bash
which pdf2md
```

Linux/macOS

or

```powershell
where pdf2md
```

Windows

---

### Images Not Appearing

Check that:

```text
output.md
assets/
```

exist in the same project structure.

Verify the image link:

```md
![Image](assets/page_1_img_1.png)
```

---

### PDF Opens But Produces Empty Markdown

Possible causes:

- Scanned PDF (image-only)
- Corrupted PDF
- Unsupported encoding

Future OCR support can be added using Tesseract.

---

## Project Structure

```text
pdf2md/
├── pdf2md/
│   ├── cli.py
│   ├── converter.py
│   ├── extractors/
│   ├── processors/
│   ├── renderers/
│   ├── models/
│   └── utils/
│
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Development

Install development dependencies:

```bash
pip install -r requirements.txt
pip install pytest
```

Run tests:

```bash
pytest
```

---

## Example Session

```bash
$ pdf2md research-paper.pdf research-paper.md --images-dir figures

Extracting: 100%|████████████████████| 42/42 [00:03<00:00]

Markdown written to research-paper.md
Images written to figures
```

Generated:

```text
research-paper.md
figures/
├── page_1_img_1.png
├── page_7_img_1.png
├── page_12_img_2.png
└── ...
```

---

## License

MIT License