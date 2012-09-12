"""Simple example of plain text I/O."""

import numpy

def text_table(outfile, csv=False):
    """
    Simple text table.

    Write data below out as plain text. By default::
    
        0000    0.000
        0001    2.000
         ...      ...
        0009   18.000

    If `csv` is `True`, write data as comma-separated values.

    Examples
    --------
    >>> text_table('myfile.txt')
    >>> text_table('myfile.csv', csv=True)
        
    """
    column_1 = numpy.arange(10)
    column_2 = column_1 * 2.0

    if csv:
        str_fmt = '{},{}\n'          # Comma delimited
    else:
        str_fmt = '{:04d} {:8.3f}\n' # Space delimited

    with open(outfile,'w') as fout:
        for c1,c2 in zip(column_1,column_2):
            fout.write(str_fmt.format(c1,c2))

def simple_html(outfile):
    """
    Simple HTML page.

    Display 'Hello World' when you open the output
    HTML file with a browser.

    Examples
    --------
    >>> simple_html('mypage.html')
    
    """
    # This is a literal block, hence the weird indentations.
    html_str = """<html>
<title>My Page</title>
<body>
<h1>Hello World</h1>
</body>
</html>
"""
    
    with open(outfile,'w') as fout:
        fout.write(html_str)
