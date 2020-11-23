import pytest
import tool


def test_jdeps_availability():
    assert tool.is_jdeps_available()


def test_jdeps_with_params():
    jdeps_version = tool.run_jdeps(["--version"])
    assert jdeps_version == "11.0.8"