import base64
import os

with open('public/logo/deyami-logo-transparent.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254" width="100%" height="100%">
  <image href="data:image/png;base64,{b64}" width="1254" height="1254" />
</svg>'''

with open('public/logo/deyami-logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("SVG created successfully!")
