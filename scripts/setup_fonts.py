import urllib.request
import re
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
req = urllib.request.Request('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Jost:wght@300;400;500;600;700&display=swap', headers=headers)
with urllib.request.urlopen(req) as resp:
    css = resp.read().decode('utf-8')

blocks = css.split('@font-face {')
clean_css = []
seen = set()

for b in blocks:
    if not b.strip():
        continue
    # We want the latin subset
    if 'unicode-range' in b and 'U+0000-00FF' in b:
        m = re.search(r'url\((https://[^)]+\.woff2)\)', b)
        if m:
            url = m.group(1)
            fam = 'Jost' if 'Jost' in b else 'Dancing Script'
            w_m = re.search(r'font-weight:\s*(\d+)', b)
            weight = w_m.group(1) if w_m else '400'
            style_m = re.search(r'font-style:\s*(\w+)', b)
            style = style_m.group(1) if style_m else 'normal'

            key = (fam, weight, style)
            if key in seen:
                continue
            seen.add(key)

            safe_name = f"{fam.lower().replace(' ', '-')}-{weight}.woff2"
            f_path = os.path.join('public/fonts', safe_name)
            req_f = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req_f) as rf:
                with open(f_path, 'wb') as wf:
                    wf.write(rf.read())

            local_rule = f"""@font-face {{
  font-family: '{fam}';
  font-style: {style};
  font-weight: {weight};
  font-display: swap;
  src: url('/fonts/{safe_name}') format('woff2');
}}"""
            clean_css.append(local_rule)

os.makedirs('src/styles', exist_ok=True)
with open('src/styles/fonts.css', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(clean_css))

print(f"Downloaded {len(clean_css)} font files and created src/styles/fonts.css!")
