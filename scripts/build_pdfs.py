"""Build the four static print packs from original, editable translations."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = A4
MARGIN = 42
CONTENT = WIDTH - 2 * MARGIN
INK = HexColor('#202c29')
TEAL = HexColor('#28685f')
GRAY = HexColor('#55615e')
LINE = HexColor('#a7b7b0')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--font', required=True)
    parser.add_argument('--bold-font', required=True)
    parser.add_argument('--cjk-font', required=True)
    parser.add_argument('--cjk-bold-font')
    parser.add_argument('--cjk-index', type=int, default=0)
    args = parser.parse_args()
    pdfmetrics.registerFont(TTFont('Latin', args.font))
    pdfmetrics.registerFont(TTFont('LatinBold', args.bold_font))
    pdfmetrics.registerFont(TTFont('CJK', args.cjk_font, subfontIndex=args.cjk_index))
    pdfmetrics.registerFont(TTFont('CJKBold', args.cjk_bold_font or args.cjk_font, subfontIndex=args.cjk_index))
    data = json.loads((ROOT / 'data/translations.json').read_text())
    output = ROOT / 'output/pdf'
    output.mkdir(parents=True, exist_ok=True)
    for lang, text in data.items():
        regular = 'CJK' if lang == 'zh' else 'Latin'
        bold = 'CJKBold' if lang == 'zh' else 'LatinBold'
        path = output / f'game-night-pack-{lang}.pdf'
        c = canvas.Canvas(str(path), pagesize=A4, pageCompression=1, invariant=1)
        c.setTitle(text['title'])
        c.setAuthor('INEAN PLAY')
        c.setSubject('Original community forms: table agreement, scores, seating and external care')
        c.setCreator('INEAN PLAY community print generator')
        c.setKeywords('INEAN PLAY, OKEY, Mahjong, printable, community, ' + lang)

        def para(value, x, y, width=CONTENT, size=10, color=INK, strong=False):
            style = ParagraphStyle('p', fontName=bold if strong else regular,
                                   fontSize=size, leading=size * 1.42, textColor=color,
                                   wordWrap='CJK' if lang == 'zh' else None)
            p = Paragraph(escape(value).replace('\n', '<br/>'), style)
            _, h = p.wrap(width, HEIGHT)
            p.drawOn(c, x, y - h)
            return y - h

        def field(label, y, height=31):
            end = para(label, MARGIN + 7, y - 5, width=155, size=9.5)
            if y - end > height - 3:
                raise ValueError('Field label too high: ' + label)
            c.setStrokeColor(LINE)
            c.line(MARGIN, y - height, WIDTH - MARGIN, y - height)
            c.line(MARGIN + 165, y - 6, MARGIN + 165, y - height + 4)
            return y - height

        def table(headers, ratios, y, rows, row_height=27):
            widths = [CONTENT * r / sum(ratios) for r in ratios]
            header_height = 35
            c.setFillColor(HexColor('#eef3f0'))
            c.rect(MARGIN, y - header_height, CONTENT, header_height, fill=1, stroke=0)
            x = MARGIN
            for value, w in zip(headers, widths):
                end = para(value, x + 5, y - 7, w - 10, size=9.2, strong=True)
                if end < y - header_height + 3:
                    raise ValueError('Header does not fit: ' + value)
                x += w
            c.setStrokeColor(LINE)
            c.setLineWidth(0.55)
            bottom = y - header_height - rows * row_height
            x = MARGIN
            for w in widths + [0]:
                c.line(x, y, x, bottom)
                x += w
            c.line(MARGIN, y, WIDTH - MARGIN, y)
            for i in range(rows + 1):
                yy = y - header_height - i * row_height
                c.line(MARGIN, yy, WIDTH - MARGIN, yy)
            return bottom, widths, y - header_height

        def footer(page):
            c.setStrokeColor(LINE)
            c.line(MARGIN, 51, WIDTH - MARGIN, 51)
            para(text['version'], MARGIN, 42, width=CONTENT-32, size=7.5, color=GRAY)
            c.setFillColor(GRAY)
            c.setFont(regular, 8)
            c.drawRightString(WIDTH - MARGIN, 31, f'{page}/5')

        for page, title in enumerate(text['titles'], 1):
            c.setFillColor(TEAL)
            c.rect(MARGIN, HEIGHT-42, 32, 4, fill=1, stroke=0)
            y = para(text['title'], MARGIN, HEIGHT-51, size=9, color=TEAL)
            y = para(title, MARGIN, y-13, size=22, strong=True)
            y -= 18
            if page == 1:
                y = para(text['intro'], MARGIN, y, size=10) - 15
                for label in [text['date']+' / '+text['venue'], text['variant'], text['players']] + text['agree']:
                    y = field(label, y, 40)
                y = para(text['additional'], MARGIN, y-20, size=10, strong=True)-10
                c.setStrokeColor(LINE)
                for offset in (30, 65, 100):
                    c.line(MARGIN, y-offset, WIDTH-MARGIN, y-offset)
                y -= 100
            elif page in (2, 3):
                y = para(text['okey'] if page==2 else text['mahjong'], MARGIN, y, size=10)-12
                y=field(text['date']+' / '+text['venue'],y)
                y=field(text['variant'],y)
                y=field(text['players']+' A / B / C / D',y)-13
                if page==2:
                    y=para(text['direction'],MARGIN,y,size=9.5)-12
                headers=[text['round'],'A','B','C','D']+([text['note']] if page==2 else [text['pool'],text['note']])
                ratios=[1.3,1,1,1,1,2.5] if page==2 else [1.3,1,1,1,1,1.4,1.8]
                y,widths,top=table(headers,ratios,y,14,26)
                for i,label in enumerate([text['initial']]+[str(n) for n in range(1,13)]+[text['total']]):
                    para(label,MARGIN+5,top-i*26-7,widths[0]-10,size=9,strong=i in (0,13))
                y=para(text['example'] if page==2 else text['conservation'],MARGIN,y-14,size=9)
            elif page==4:
                y=para(text['rotation'],MARGIN,y,size=10)-12
                y=field(text['date']+' / '+text['venue'],y)
                y=field(text['variant'],y)-15
                y,_,_=table([text['time'],text['venue'],text['seat'],text['dealer'],text['note']],[1.1,1.2,3.1,1.6,2],y,8,55)
            else:
                y=para(text['care'],MARGIN,y,size=10)-14
                y=field(text['date']+' / '+text['venue'],y)-12
                for item in text['checks']:
                    c.setStrokeColor(GRAY);c.rect(MARGIN,y-10,8,8,fill=0,stroke=1)
                    y=para(item,MARGIN+17,y,CONTENT-17,size=9.5)-12
                y,_,_=table([text['date'],text['action'],text['next'],text['person']],[1.2,3.4,1.8,1.2],y-2,7,42)
                y=para(text['stop'],MARGIN,y-16,size=9)
            if y<65:
                raise ValueError(f'{lang} page {page} overlaps footer: {y:.1f}')
            footer(page)
            c.showPage()
        c.save()
        print(path.name)


if __name__ == '__main__':
    main()
