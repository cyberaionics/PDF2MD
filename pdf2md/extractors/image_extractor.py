from pathlib import Path

import fitz

from pdf2md.models.image import ImageBlock


def extract_images(
    page,
    pdf_doc,
    page_number: int,
    image_dir: Path
):
    """
    Extract page images.

    Returns:
        list[ImageBlock]
    """

    images = []

    image_list = page.get_images(
        full=True
    )

    for idx, image in enumerate(
        image_list,
        start=1
    ):

        xref = image[0]

        try:

            pix = fitz.Pixmap(
                pdf_doc,
                xref
            )

            image_name = (
                f"page_{page_number}_img_{idx}.png"
            )

            image_path = (
                image_dir /
                image_name
            )

            if pix.n < 5:
                pix.save(
                    image_path
                )
            else:
                rgb = fitz.Pixmap(
                    fitz.csRGB,
                    pix
                )

                rgb.save(
                    image_path
                )

                rgb = None

            pix = None

            rects = page.get_image_rects(
                xref
            )

            if rects:
                rect = rects[0]

                images.append(
                    ImageBlock(
                        path=str(image_path),
                        x0=rect.x0,
                        y0=rect.y0,
                        x1=rect.x1,
                        y1=rect.y1,
                        width=rect.width,
                        height=rect.height
                    )
                )

        except Exception:
            continue

    return images