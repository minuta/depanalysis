import pytest
from config import Config


def test_read_path_from_config():
    cfg = Config()
    assert cfg.get_path() == "/usr/lib/jvm/java-11-openjdk/bin/jdeps"

