"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    qty = int(value.strip())
    if qty < 0:
        raise ValueError(f"Quantity must be non-negative, got {qty}")
    return qty
