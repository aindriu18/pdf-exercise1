"""
build a tool that watermarks all pages on the super.pdf file
"""

import PyPDF2


def create_watermark(input_pdf, output_pdf, watermark):

    # opens the file we want to add te watermark to
    input_pdf = PyPDF2.PdfFileReader(open('dummy.pdf', 'rb'))

    # creates a pdf writer object for the output file
    output_pdf = PyPDF2.PdfFileWriter()

    # opens the watermark file
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

    # getNumPages will make sure that we iterate over all pages in the input file.
    for i in range(input_pdf.getNumPages()):

        page = input_pdf.getPage(i)

        # will overlay the watermark on top of current page.
        page.mergePage(watermark.getPage(0))

        # add newly merged page to the output object
        output_pdf.addPage(page)

        with open('output2.pdf', 'wb') as file:

            # writes to output pdf
            output_pdf.write(file)


create_watermark('dummy.pdf', 'output2.pdf', 'wtr.pdf')