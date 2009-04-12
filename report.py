# Copyright (c) 2009 Jeremy English <jhe@jeremyenglish.org>

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
            if self.c is None:
                wd = len(i) + self.tablePad
            else:
                wd = c.stringWidth(i + (self.tablePad*'W'), fontName, fontSize)
            self.rowWidths.append(wd)

    def addRow(self,row):
        self.rows.append(row)
        for i,cellinfo in enumerate(zip(self.rowWidths,row)):
            width,cell = cellinfo
            fontName,fontSize,ident = cmdFonts('')
            if self.c is None:
                wd = len(cell) + self.tablePad
            else:
                wd = self.c.stringWidth(cell + (self.tablePad*'W'), fontName, fontSize)
            self.rowWidths[i] = max(width, wd)

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
#        print "Widths %s" % (s1)
    return line

def getCmd(sl):
    if len(sl) > 0:
        return sl[0]
    else:
        return ''

def procTableCmd(sl, table, c=None):
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
    """Parse the text and write it stdout."""
    table = None
    for t in text.split('\n'):
        sl = t.strip()
        cmd = getCmd(sl)
        if cmd == '|':
            table = procTableCmd(sl, table)
        else:
            ident = 4
            if table:
                for row in table.rows:
                    s1 = ' '*ident
                    for width,cell in zip(table.rowWidths, row):
                        s1 = s1 + cell.ljust(width,' ')
                    print s1
                table = None
                
            if cmd == '*':
                s = sl.strip(cmd).strip()
                print s
                print '='*len(s)
            elif cmd == '+':
                s = sl.strip(cmd).strip()
                print s
                print '-'*len(s)
            else:
                print ' '*ident + sl

def createHtml(filename, text):
    f = open(filename,'w')
    f.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">''')

    f.write('<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">')

    f.write('<head>')
    f.write('''<style type="text/css">
    body{
    margin-left: 20%;
    margin-top: 5%;
    }
    p{
    margin-left:2%;
    }
    table{
    margin-left:2%;
    width: 80%
    }
    </style>''')

    f.write('<title>%s</title>' % (filename))
    f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    f.write('</head>')

    f.write('<body>')

    inP = False

    def canP(inP):
        if inP:
            f.write('</p>')
        return False

    table = None
    for t in text.split('\n'):
        sl = t.strip()
        cmd = getCmd(sl)
        if cmd == '|':
            table = procTableCmd(sl, table)
        else:
            ident = 4
            if table:
                inP = canP(inP)
                f.write('<table>')
                for row in table.rows:
                    f.write('<tr>')
                    for cell in row:
                        f.write('<td>%s</td>' % (cell))
                    f.write('</tr>')
                f.write('</table>')
                table = None
                
            if cmd == '*':
                s = sl.strip(cmd).strip()
                inP = canP(inP)
                f.write('<h1>%s</h1>' % (s))
            elif cmd == '+':
                s = sl.strip(cmd).strip()
                inP = canP(inP)
                f.write('<h2>%s</h2>' % (s))
            else:
                if not inP:
                    inP = True
                    f.write('<p>')

                f.write('%s<br/>' % sl)

    inP = canP(inP)
    f.write('</body>')
    f.write('</html>')
    f.close()

def runReport(reportType, text="", filename=None):
    if reportType == 'pdf':
        createPdf(filename,
                  text)
    elif reportType == 'txt':
        createTxt(text)
    elif reportType == 'html':
        createHtml(filename, text)

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

def txtTest():
    createTxt("""*This is a header
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

def htmlTest():
    createHtml("test.html",
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
