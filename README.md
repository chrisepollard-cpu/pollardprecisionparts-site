# pollardprecisionparts.com

Static site for **Pollard's Precision Parts**, Llano, TX. Plain HTML/CSS, no JavaScript, no build step needed to serve.

- Pages: `index.html`, `services.html`, `contact.html` (+ `404.html`)
- Brand: navy `#1c2333`, orange `#e2531b`, tint `#fbe7de`; Montserrat + Libre Baskerville (Google Fonts, same faces as the flyers), gear mark in `img/`
- Contact: pollardprecisionparts@gmail.com (no public phone yet)
- `CNAME` is set for `pollardprecisionparts.com` (GitHub Pages)

Editing: shared header/footer live in `_build/build.py`; run `python3 _build/build.py` to regenerate the pages.
Previews: `node _build/shoot.js` (playwright-core + Chrome) writes `preview-*.png` locally.

## GitHub Pages DNS (at the registrar)

| Type  | Host | Value |
|-------|------|-------|
| A     | @    | 185.199.108.153 |
| A     | @    | 185.199.109.153 |
| A     | @    | 185.199.110.153 |
| A     | @    | 185.199.111.153 |
| CNAME | www  | chrisepollard-cpu.github.io |

Optional IPv6 (AAAA, @): 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153
