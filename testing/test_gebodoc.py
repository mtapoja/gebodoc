
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

def test_test1_simple_string_variables():
    test_config = './test1.cfg'
    test_result = './test1_result.txt'
    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out

        doc = gebodoc.Documenter(test_config)
        doc.parse_configuration()
        doc.process_template()

        output = out.getvalue()

        verificationdata = read_verification_file(test_result)

        # Compare.
        assert output == verificationdata
    finally:
        sys.stdout = saved_stdout

