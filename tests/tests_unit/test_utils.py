import pytest

from _nebari.utils import byte_unit_conversion


@pytest.mark.parametrize(
    "value, from_unit, to_unit, expected",
    [
        (1, "", "B", 1),
        (1, "B", "B", 1),
        (1, "KB", "B", 1000),
        (1, "K", "B", 1000),
        (1, "k", "b", 1000),
        (1, "MB", "B", 1000**2),
        (1, "GB", "B", 1000**3),
        (1, "TB", "B", 1000**4),
        (1, "KiB", "B", 1024),
        (1, "MiB", "B", 1024**2),
        (1, "GiB", "B", 1024**3),
        (1, "TiB", "B", 1024**4),
        (1000, "B", "KB", 1),
        (1000, "KB", "K", 1000),
        (1000, "K", "KB", 1000),
        (1000, "MB", "KB", 1000**2),
        (1000, "GB", "KB", 1000**3),
        (1000, "TB", "KB", 1000**4),
        (1000, "KiB", "KB", 1024),
        (1000, "Ki", "KB", 1024),
        (1000, "Ki", "K", 1024),
        (1000, "MiB", "KB", 1024**2),
        (1000, "GiB", "KB", 1024**3),
        (1000, "TiB", "KB", 1024**4),
        (1000**2, "B", "MB", 1),
        (1000**2, "KB", "MB", 1000),
        (1000**2, "MB", "MB", 1000**2),
        (1000**2, "GB", "MB", 1000**3),
        (1000**2, "TB", "MB", 1000**4),
        (1000**2, "MiB", "MB", 1024**2),
        (1000**3, "B", "GB", 1),
        (1000**3, "KB", "GB", 1000),
    ],
)
def test_byte_unit_conversion(value, from_unit, to_unit, expected):
    assert byte_unit_conversion(f"{value} {from_unit}", to_unit) == expected
