
import os
import sys
import gebodoc

# Read the textual output or verification file.
def read_a_file(filename):
    with open (filename, 'r') as resultfile:
        resultdata = resultfile.read()
    return resultdata

#
# Test cases.

def output_and_execution(tc, tr):
    try:
        doc = gebodoc.Documenter(tc)
        doc.parse_configuration()
        doc.process_template()

        # Assume that a test case that has a config file called 'conf_for_test.cfg'
        # producess output file called 'conf_for_test'.
        tcconfigpath, tcconfigfilename = os.path.split(tc)
        outputfilename, fileextension = os.path.splitext(tcconfigfilename)

        output = read_a_file(outputfilename)
        verificationdata = read_a_file(tr)

        # Compare.
        assert output == verificationdata
    finally:
        # Clean up the temporary output files.
        os.unlink(outputfilename)


def test_test1_simple_string():
    test_config = './cases/test1.cfg'
    test_result = './cases/test1_result.txt'
    output_and_execution(test_config, test_result)


def test_string_and_2_column_list():
    test_config = './cases/string_and_2_column_list.cfg'
    test_result = './cases/string_and_2_column_list_result.txt'
    output_and_execution(test_config, test_result)


def test_string_and_3_column_list():
    test_config = './cases/string_and_3_column_list.cfg'
    test_result = './cases/string_and_3_column_list_result.txt'
    output_and_execution(test_config, test_result)
