from pdf2md.models.document import Document


def extract_metadata(
    pdf_doc,
    document: Document
):
    """
    Populate document metadata.
    """

    metadata = pdf_doc.metadata

    document.title = (
        metadata.get("title") or ""
    )

    document.author = (
        metadata.get("author") or ""
    )

    return document