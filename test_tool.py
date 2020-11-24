import pytest
from tool import Tool


JDEPS_VERSION = "11.0.8"
VERSION_COMMAND = "--version"

tool = Tool()

def test_jdeps_availability():
    assert tool.is_jdeps_available()


def test_jdeps_with_params():
    jdeps_version = tool.run_jdeps([VERSION_COMMAND])
    assert jdeps_version == JDEPS_VERSION