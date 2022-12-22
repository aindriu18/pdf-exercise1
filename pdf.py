import PyPDF2
import sys

# will grab all the arguments besides the first one which is our python file.
inputs = sys.argv[1:]

# pdf_lists will be our inputs.
def pdf_combiner(pdf_list):

    # there is a merger object with PyPDF
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)



