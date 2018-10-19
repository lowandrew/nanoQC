#!/usr/bin/env python

from nanoqc import nanoQC
import pytest


def test_arg_check_no_input_or_summary_quits():
    nanoqc = nanoQC.NanoQC(input_folder=None,
                           sequencing_summary=None,
                           threads=1,
                           output_folder='asdf')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        nanoqc.check_args()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_exception_when_no_input_fastqs():
    nanoqc = nanoQC.NanoQC(input_folder='tests/no_fastqs_here',
                           sequencing_summary=None,
                           threads=1,
                           output_folder='asdf')
    with pytest.raises(Exception):
        nanoqc.find_fastq_files()
