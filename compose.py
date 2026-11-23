from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 1600
PAPER, INK, RED, NAVY, TEAL, SAND = '#f6f1e5', '#14181f', '#b3202c', '#1d3557', '#14666b', '#ece4d3'
im = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(im)

def font(size, face='sans', bold=False):
    paths = {
        ('serif', True): ['/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'],
        ('sans', True): ['/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'],
        ('sans', False): ['/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'],
    }
    for p in paths[(face, bold)]:
        try: return ImageFont.truetype(p, size)
        except OSError: pass
    return ImageFont.load_default()

def width(s, f):
    b = d.textbbox((0, 0), s, font=f)
    return b[2] - b[0]

def wrap(text, f, maxw):
    result = []
    for para in text.split('\n'):
        line = ''
        for word in para.split():
            trial = word if not line else line + ' ' + word
            if width(trial, f) <= maxw: line = trial
            else:
                if line: result.append(line)
                line = word
        if line: result.append(line)
    return result

def paragraph(text, x, y, f, fill, maxw, leading=3):
    for line in wrap(text, f, maxw):
        d.text((x, y), line, font=f, fill=fill)
        y += f.size + leading
    return y

def centered(text, y, f, fill, x0=0, x1=W):
    d.text((x0 + (x1-x0-width(text, f))/2, y), text, font=f, fill=fill)

def rule(x0, y, x1, fill=INK, thick=1): d.line((x0, y, x1, y), fill=fill, width=thick)

# Masthead
d.rectangle((32, 22, 1168, 30), fill=RED)
centered('THE DAILY WORLD', 38, font(70, 'serif', True), INK)
rule(32, 132, 1168, thick=2)
d.text((38, 143), 'VOL. XXII — NO. 327', font=font(15,'sans',True), fill=INK)
centered('MONDAY, NOVEMBER 23, 2026', 143, font(15,'sans',True), INK)
d.text((1003, 143), 'ONE IMAGE EDITION', font=font(15,'sans',True), fill=INK)
rule(32, 174, 1168)

# Lead report and hand-drawn Baltic night scene
d.text((42, 189), 'BALTIC SEA / KYIV', font=font(17,'sans',True), fill=RED)
lead_f = font(43, 'serif', True)
yy = paragraph("UKRAINE TAKES THE WAR TO RUSSIA'S FLEET — AND RUSSIA ANSWERS OVER KYIV", 40, 218, lead_f, INK, 694, leading=0)
body = ('Ukrainian sea drones set the Russian cargo ship Sparta II ablaze in the Baltic, leaving it drifting into Finnish waters, a day after the corvette Merkury sank at Benghazi; Kyiv also hit the dry cargo vessel MV Angara. Over Ukraine, a Russian strike on a Kyiv-region supermarket killed 2 and wounded at least 8 during working hours. Another strike on a residential complex near the capital killed 3 and trapped more under rubble. Ukraine’s General Staff says Russia lost over 1,700 troops in 24 hours. President Zelenskyy renewed his appeal to Washington for Patriot missiles.')
paragraph(body, 42, yy+12, font(18), INK, 690, leading=4)

# Illustration panel: dark Baltic, cargo ship, smoke, searchlights and distant skyline
ix0, iy0, ix1, iy1 = 775, 225, 1158, 536
d.rectangle((ix0, iy0, ix1, iy1), fill='#17283b', outline=INK, width=2)
d.ellipse((1063, 248, 1115, 300), fill='#e8d7a8', outline='#e8d7a8')
d.rectangle((786, 388, 1147, 469), fill='#26394c')
for x, h in [(797,37),(827,55),(860,42),(890,72),(923,47),(953,61),(986,39),(1015,66),(1047,48),(1080,72),(1118,51)]:
    d.rectangle((x, 388-h, x+24, 470), fill='#24364a')
    for wx in (x+5, x+14):
        for wy in range(397-h, 461, 17):
            if (wx+wy) % 3: d.rectangle((wx, wy, wx+4, wy+6), fill='#e1b76e')
d.polygon([(862,382),(803,263),(900,378)], fill='#d9d3a0')
d.polygon([(1094,385),(1135,273),(1072,383)], fill='#d9d3a0')
d.rectangle((786, 466, 1147, 526), fill='#102b42')
for x in range(799, 1140, 42): d.line((x, 488+(x%19), x+25, 488+(x%19)), fill='#66828b', width=2)
d.polygon([(848,444),(1091,444),(1066,478),(876,478)], fill='#202a31', outline='#111820')
d.rectangle((903,420,1046,444), fill='#78818a', outline=INK)
d.rectangle((928,405,1018,420), fill='#89929a', outline=INK)
d.rectangle((1030,419,1040,438), fill=RED)
d.ellipse((967,371,1020,423), fill='#8f2524')
d.ellipse((979,357,1006,407), fill='#e36b27')
d.polygon([(975,411),(978,382),(990,394),(995,362),(1005,394),(1015,376),(1012,414)], fill='#f5b43d')
d.ellipse((976,332,1011,373), fill='#46505a')
d.ellipse((990,309,1034,360), fill='#424b54')
d.ellipse((1004,286,1041,336), fill='#353f49')
d.text((797, 502), 'BALTIC SEA • NIGHT', font=font(13,'sans',True), fill='#f6f1e5')
centered('DRONE STRIKE SETS SPARTA II ABLAZE', 545, font(13,'sans',True), NAVY, 766, 1168)
rule(32, 574, 1168, RED, 3)

# Second lead
d.text((42, 590), 'THANKSGIVING TRAVEL', font=font(15,'sans',True), fill=RED)
paragraph('OUTAGE GROUNDS THANKSGIVING GETAWAY: 1,600 DELTA FLIGHTS DELAYED', 40, 616, font(33,'serif',True), NAVY, 1118, leading=0)
second = ('A failure in Delta Air Lines’ weight-and-balance systems delayed more than 1,600 flights across the United States, snarling Atlanta, the world’s busiest hub, just as Thanksgiving travel began. The airline said the outage was resolved by Monday. In Washington, President Trump signed the Common Cents Act, ending production of the penny after 232 years.')
paragraph(second, 42, 694, font(17), INK, 1110, leading=3)
rule(32, 777, 1168)

# Three-column briefs
columns = [42, 426, 810]
colw = 348
for x in (408, 792): d.line((x, 791, x, 1279), fill='#9a9487', width=1)
briefs = [
    [('HORMUZ', 'Iran says it shot down a U.S. MQ-9 Reaper over the Strait of Hormuz — the 58th drone it claims — as attacks on shipping there reach their highest level since the war began.'),
     ('INDONESIA', 'The navy seized a ship bound from China to Bangladesh carrying 405 tonnes of sodium perchlorate, a rocket-propellant chemical.'),
     ('LAHORE', 'Pakistan’s Lahore again topped the world’s pollution ranking with air quality above 500, deep in the hazardous band.')],
    [('BELGIUM', 'Airports faced a complete shutdown as a nationwide protest against austerity halted flights.'),
     ('DENMARK', 'Copenhagen accused Russia of plotting to kill a Ukrainian-American rapper on Danish soil.'),
     ('SYRIA', 'Authorities destroyed 400 million Captagon pills in one of the largest drug seizures on record.')],
    [('NEPAL', 'Prime Minister Balen Shah received a ceremonial welcome in New Delhi and was received by Prime Minister Modi.'),
     ('THANKSGIVING', 'A coastal storm is forecast to bring heavy rain and strong winds to New York City on Thanksgiving Day, Thursday.'),
     ('AT SEA', 'The cargo ship MV Angara was also struck as Kyiv widened its campaign against Russian vessels.')]
]
labels = ['WAR & SHIPPING', 'EUROPE & MIDDLE EAST', 'ASIA & DIPLOMACY']
for ci, x in enumerate(columns):
    d.text((x, 792), labels[ci], font=font(14,'sans',True), fill=RED)
    y = 819
    for head, copy in briefs[ci]:
        d.text((x, y), head, font=font(21,'sans',True), fill=NAVY)
        y += 29
        y = paragraph(copy, x, y, font(16), INK, colw, leading=3) + 12
        rule(x, y, x+colw, '#aaa394')
        y += 12

# Markets and sport boxes
d.rectangle((32, 1300, 1168, 1532), fill=SAND, outline=INK, width=1)
d.line((600, 1300, 600, 1532), fill='#9a9487', width=1)
d.text((48, 1315), 'MARKETS', font=font(16,'sans',True), fill=RED)
d.text((48, 1340), 'AI FEARS SPREAD WEST', font=font(25,'sans',True), fill=NAVY)
paragraph('Wall Street braced for up to $80.6 billion in further sell-offs as the AI sell-off that hit Asia on Monday spread west; the Nikkei’s 5% slide set the tone.', 48, 1380, font(18), INK, 505, leading=5)
for i, (x, h) in enumerate([(510,67),(530,83),(550,111),(570,137)]):
    d.rectangle((x, 1512-h, x+12, 1512), fill=RED if i == 3 else NAVY)
d.text((620, 1315), 'SPORT', font=font(16,'sans',True), fill=RED)
d.text((620, 1340), 'FINALS, FOOTBALL & A HOST BID', font=font(23,'sans',True), fill=NAVY)
paragraph('Alcaraz beat Zverev to win his first ATP Finals title; FIFA is set to confirm the United Kingdom as host of the 2035 Women’s World Cup; Liverpool beat ten-man Manchester United.', 620, 1380, font(18), INK, 520, leading=5)
d.ellipse((1072, 1460, 1134, 1522), fill='#d8bc56', outline=NAVY, width=2)
d.arc((1078,1462,1110,1520), 275, 85, fill=PAPER, width=3)
d.arc((1097,1462,1129,1520), 95, 265, fill=PAPER, width=3)

rule(32, 1543, 1168)
centered('Compiled from wire reports around the world — Monday 23 November 2026 · The day, in one image', 1552, font(12), INK, 32, 1168)
im.save(Path(__file__).with_name('entry.png'), format='PNG', optimize=True)
