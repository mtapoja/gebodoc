
import sys
from StringIO import StringIO
import gebodoc

# Read the correct verification file where the output is compared.
def read_verification_file(filename):
    with open (filename, 'r') as resultfile:
        resultdata = resultfile.read()
    return resultdata

#
# Test cases.

def output_and_execution(tc, tr):
    # This function might not be necessary once writing to a file works.
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out

        doc = gebodoc.Documenter(tc)
        doc.parse_configuration()
        doc.process_template()

        output = out.getvalue()

        verificationdata = read_verification_file(tr)

        # Compare.
        assert output == verificationdata
    finally:
        sys.stdout = saved_stdout



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
