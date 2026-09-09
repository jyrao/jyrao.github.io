#!/usr/bin/env python3
"""Export the five archived course syllabi to editable Markdown and linked PDFs.
Requires reportlab. AI1803 already has an original PDF and is preserved.
"""
from pathlib import Path
import re
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'files/teaching'
FONT = Path('/System/Library/Fonts/Supplemental')
for name, filename in [('Body','Arial.ttf'), ('Body-Bold','Arial Bold.ttf'), ('Body-Italic','Arial Italic.ttf'), ('Body-BoldItalic','Arial Bold Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT / filename)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body-Italic', boldItalic='Body-BoldItalic')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Copy', fontName='Body', fontSize=10, leading=15, spaceAfter=7, splitLongWords=True))
styles.add(ParagraphStyle(name='CourseTitle', fontName='Body-Bold', fontSize=19, leading=25, textColor=colors.HexColor('#193c50'), spaceAfter=14))
styles.add(ParagraphStyle(name='SectionTitle', fontName='Body-Bold', fontSize=12, leading=17, spaceBefore=12, spaceAfter=7, keepWithNext=True))
styles.add(ParagraphStyle(name='BulletCopy', parent=styles['Copy'], leftIndent=12, firstLineIndent=-8))

def inline(s):
    # Protect Markdown links, then link bare URLs; retain emphasis.
    saved=[]
    def link(m):
        saved.append('<link href="'+escape(m.group(2), quote=True)+'" color="#226588">'+escape(m.group(1))+'</link>')
        return f'LINKTOKEN{len(saved)-1}END'
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, s)
    s=escape(s)
    s=re.sub(r'https?://[^\s<]+', lambda m:'<link href="'+m[0]+'" color="#226588">'+m[0]+'</link>', s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
    for i,v in enumerate(saved): s=s.replace(f'LINKTOKEN{i}END',v)
    return s

def footer(canvas, doc):
    canvas.setFont('Body',8)
    canvas.setFillColor(colors.HexColor('#657782'))
    canvas.drawString(48,29,doc.title.split(',')[0]+' | Course syllabus')
    canvas.drawRightString(547,29,str(doc.page))

for code in ['MATH2560J','MATH2160J','CUL2610J','STAT4060J','BUS3680J']:
    raw=(ROOT / '_teaching' / (code+'.md')).read_text()
    _,front,body=raw.split('---',2)
    title=re.search(r'title: "(.+)"',front)[1]
    if code=='MATH2560J': title=code+', Honors Linear Algebra & Differential Equation'
    body=body.strip()
    # Restore headings and list markers from the original extracted syllabus.
    body=re.sub(r'(?m)^(\d+(?:\.\d+)? [A-Z][^\n]+)$',r'## \1',body)
    body=re.sub(r'(?m)^\*\*([^*]+)\*\*$',r'## \1',body)
    body=re.sub(r'(?m)^[•+∗] ', '- ', body)
    body=body.replace('–','-').replace('—','-')
    body=re.sub(r'(?m)^(?=- )', '\n', body)
    # Rejoin URL wrapping artifacts present in the archived text.
    body=re.sub(r'(https?://[^\s]+[_?])\s+(?=[a-z])', r'\1', body)
    body=re.sub(r'(https?://[^\s]+) (?=referrer=)', r'\1', body)
    (OUT/(code+'-syllabus.md')).write_text('# '+title+'\n\n'+body+'\n')
    story=[Paragraph(escape(title),styles['CourseTitle'])]
    for block in re.split(r'\n\s*\n',body):
        block=' '.join(block.splitlines())
        if block.startswith('## '): style=styles['SectionTitle']; block=block[3:]
        elif block.startswith('- '): style=styles['BulletCopy']
        else: style=styles['Copy']
        story.append(Paragraph(inline(block),style))
    doc=SimpleDocTemplate(str(OUT/(code+'-syllabus.pdf')),pagesize=(595.28,841.89),rightMargin=48,leftMargin=48,topMargin=45,bottomMargin=48,title=title,author='Shanghai Jiao Tong University')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    print(code)
