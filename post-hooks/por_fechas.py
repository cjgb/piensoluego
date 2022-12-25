import os
import yaml
import datetime

post_dir = "../content/post"
target_file = "../content/paginas/por_fecha.md"

md_header = f"""
---
title: Por fecha
date: {datetime.date.today().strftime('%Y-%m-%d')}
type: page
url: /por_fecha/
menu:
    main:
        weight: 20
---
"""

all_posts = os.listdir(post_dir)
all_posts = [os.path.join(post_dir, f) for f in all_posts if f[-2:] == "md"]

def get_header(fname):
    with open(fname) as f:
        tmp = next(yaml.load_all(f, Loader=yaml.FullLoader))
    if isinstance(tmp['date'], datetime.datetime):
        tmp['date'] = tmp['date'].date()
    return tmp

mes = ['', 'Enero', 'Febrero', 'Marzo',
        'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre',
        'Octubre', 'Noviembre', 'Diciembre']

headers = [get_header(f) for f in all_posts]
headers = [h for h in headers if h['date'] < datetime.date.today()]
headers.sort(key = lambda x: x['date'], reverse = True)

year = headers[0]['date'].year
month = headers[0]['date'].month

out = [f"* {year}", f"  * {mes[month]} {year}"]

for h in headers:
    if h['date'].year < year:
        year = h['date'].year
        month = h['date'].month
        out.extend([f"* {year}", f"  * {mes[month]} {year}"])
    elif h['date'].month < month:
        month = h['date'].month
        out.extend([f"  * {mes[month]} {year}"])
    out.append(f"    * [{h['title']}]({h['url']})")

with open(target_file, "w") as f:
    print(md_header, file = f)
    for l in out:
        print(l, file = f)



