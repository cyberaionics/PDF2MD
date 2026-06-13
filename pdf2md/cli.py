import click

from pdf2md.converter import (
    PDFToMarkdownConverter
)


@click.command()
@click.argument(
    "input_pdf",
    type=click.Path(
        exists=True
    )
)
@click.argument(
    "output_md"
)
@click.option(
    "--images-dir",
    default="assets",
    help="Directory for extracted images."
)
def main(
    input_pdf,
    output_md,
    images_dir
):
    """
    Convert PDF to Markdown.
    """

    converter = PDFToMarkdownConverter(
        input_pdf=input_pdf,
        output_md=output_md,
        image_dir=images_dir
    )

    converter.convert()

    click.echo(
        f"Markdown written to {output_md}"
    )

    click.echo(
        f"Images written to {images_dir}"
    )


if __name__ == "__main__":
    main()