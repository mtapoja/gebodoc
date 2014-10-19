
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

def output_and_execution(tc, tr, to=''):
    outputfilename = ''
    try:
        doc = gebodoc.Documenter(tc, testing_active=True)
        doc.parse_configuration()
        doc.process_template()

        # If no test output file name (to) is given, assume that a test case
        # with a config file called 'conf_for_test.cfg' produces an output
        # file called 'conf_for_test'.
        if to == '':
            tcconfigpath, tcconfigfilename = os.path.split(tc)
            outputfilename, fileextension = os.path.splitext(tcconfigfilename)
            output = read_a_file(outputfilename)
        else:
            print('test output file: %s' % to)
            output = read_a_file(to)

        verificationdata = read_a_file(tr)

        # Compare.
        assert output == verificationdata
    finally:
        # Clean up the temporary output files.
        if outputfilename != '':
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

def test_latex_to_pdf():
    test_config = './cases/latex_to_pdf.cfg'
    test_intermediate_result = './cases/latex_to_pdf_result.tex'
    test_output = './latex_to_pdf.tex'
    test_result = './latex_to_pdf.pdf'
    output_and_execution(test_config, test_intermediate_result, test_output)

    assert os.path.exists(test_result)

    # Add teardown function, if similar cases appear later.
    os.unlink(test_output)
    os.unlink(test_result)

