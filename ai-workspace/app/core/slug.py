import re
import ulid


def base_slug(text: str) -> str:
    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def generate_slug(name: str) -> str:
    base = base_slug(name)
    unique = str(ulid.new())[:16]

    return f"{base}-{unique}"