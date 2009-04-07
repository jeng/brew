# Copyright © 2009 Jeremy English <jhe@jeremyenglish.org>

# Permission to use, copy, modify, distribute, and sell this software
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.  No representations are made about the
# suitability of this software for any purpose.  It is provided "as
# is" without express or implied warranty.

# Created: 06-April-2009 

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import re

def cmdFonts(cmd):
    """Returns the font name, font size and ident amount for the command."""
    left_margin = (0.75 * inch)
    header_height = 28
    h2_height = 18
    text_height = 12

    if cmd == '*':
        return ("Times-Bold",header_height,left_margin)
    elif cmd == '+':
        return ("Times-Bold",h2_height,left_margin)
    else:
        return ("Times-Roman",text_height,left_margin + (inch * 0.125))

class Table:
    def __init__(self, c, rows=[]):
        self.rows = [rows]
        self.rowWidths = []
        self.c = c
        self.tablePad = 2
        for i in rows:
            fontName,fontSize,ident = cmdFonts('')
            wd = c.stringWidth(i + (self.tablePad*'W'), fontName, fontSize)
            self.rowWidths.append(wd)

    def addRow(self,row):
        self.rows.append(row)
        for i in range(len(row)):
            fontName,fontSize,ident = cmdFonts('')
            wd = self.c.stringWidth(row[i] + (self.tablePad*'W'), fontName, fontSize)
            self.rowWidths[i] = max(self.rowWidths[i], wd)

def writeTable(c, table, line):

    fontName,fontSize,ident = cmdFonts('')
    c.setFont(fontName, fontSize)
    for row in table.rows:
        x = ident
        line = line - fontSize
        s1 = ""
        for width,cell in zip(table.rowWidths, row):
            s1 = ("%s %d") % (s1, width)
            c.drawString(int(x), line, cell)
            x = x + width
        print "Widths %s" % (s1)
    return line

def getCmd(sl):
    if len(sl) > 0:
        return sl[0]
    else:
        return ''

def procTableCmd(sl, table, c):
    row = sl.split('|')[1:-1]
    if table == None:
        table = Table(c,row)
    else:
        table.addRow(row)
    return table

def writeText(c, text):
    """Parse the text and write it out to the canvas."""
    top_margin = A4[1] - (0.25 * inch)

    line = top_margin
    table = None
    
    for t in text.split('\n'):
        sl = t.strip()
        cmd = getCmd(sl)
        fontName,fontSize,ident = cmdFonts(cmd)

        if cmd == '|':
            table = procTableCmd(sl, table, c)
        else:
            if table:
                line = writeTable(c, table, line)
                table = None
                
            line = line - fontSize
            if cmd in ('*', '+'):
                s = sl.strip(cmd).strip()
            else:
                s = sl
            
            c.setFont(fontName, fontSize)            
            c.drawString(ident, line, s)
        

def createPdf(filename, text):
    """Writes out a pdf file named filename that contains text

    Lines beginning with a * get treated as headers.Lines beginning
    with a + get treated as smaller headers.  Tables can be created by
    starting a line with | and seperating cells with other |.
    """
    c = canvas.Canvas(filename)
    writeText(c, text)
    c.showPage()
    c.save()

def createTxt(text):
    for line in text.split('\n'):
        print line

def runReport(reportType, text="", filename=None):
    if reportType == 'pdf':
        createPdf(filename,
                  text)
    elif reportType == 'txt':
        createTxt(text)

def pdfTest():
    createPdf("test.pdf",
              """*This is a header
              This a line below the header
              This is another line
              +Header number 2
              Yes some more lines
              +insert a table
              |foo1|1|2|3|
              |bar|4|5|6|
              |baz|7|8|9|
              +yow
              |the|second|table|
              |0|1|2|
              |3|4|5|
              |6|7|8|
              """)
