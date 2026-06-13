def detect_caption(
    previous_text: str
):
    """
    Simple heuristic.
    """

    previous_text = (
        previous_text.strip()
    )

    if previous_text.lower().startswith(
        "figure"
    ):
        return previous_text

    return None