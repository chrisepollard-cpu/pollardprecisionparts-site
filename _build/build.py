"""Builds the static pages from one shared header/footer (python3 _build/build.py)."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://pollardprecisionparts.com"
NAME = "Pollard’s Precision Parts"
EMAIL = "pollardprecisionparts@gmail.com"
MAILTO = f"mailto:{EMAIL}?subject=Parts%20request"
EMAIL_W = EMAIL.replace("@", "@<wbr>")

LD = json.dumps({
  "@context": "https://schema.org", "@type": "LocalBusiness", "@id": SITE + "/#business",
  "name": "Pollard's Precision Parts", "url": SITE + "/", "email": EMAIL,
  "description": "Custom 3D-printed replacement, discontinued, and hard-to-find parts made in a Llano, Texas workshop.",
  "address": {"@type": "PostalAddress", "addressLocality": "Llano", "addressRegion": "TX", "addressCountry": "US"},
  "areaServed": "United States", "logo": SITE + "/img/gear.svg"}, indent=2)

def nav(cur):
    def a(href, label, key, cls=""):
        c = f' class="{cls}"' if cls else ""
        cur_attr = ' aria-current="page"' if key == cur else ""
        return f'<a href="{href}"{c}{cur_attr}>{label}</a>'
    return a("services.html", "Services", "services") + "\n        " + a("contact.html", "Contact", "contact", "nav-cta")

def page(fname, key, title, desc, body):
    canon = SITE + "/" if fname == "index.html" else f"{SITE}/{fname}"
    ld = f'\n  <script type="application/ld+json">\n{LD}\n  </script>' if fname == "index.html" else ""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canon}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#1c2333">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,700;1,400&amp;family=Montserrat:wght@400;600;800&amp;display=swap">
  <link rel="stylesheet" href="css/site.css">{ld}
</head>
<body>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="./" aria-label="{NAME} home"><img src="img/gear.svg" alt="" width="30" height="30"><span>{NAME}</span></a>
      <nav class="nav" aria-label="Main">
        {nav(key)}
      </nav>
    </div>
  </header>
  <main>
{body}
  </main>
  <footer class="site-footer">
    <div class="wrap footer-inner">
      <a class="brand" href="./"><img src="img/gear.svg" alt="" width="24" height="24"><span>{NAME}</span></a>
      <div>Custom 3D-printed parts · Llano, Texas</div>
    </div>
  </footer>
</body>
</html>
'''
    (ROOT / fname).write_text(html)

HOME = f'''    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <p class="kicker">Llano · Texas Hill Country</p>
          <h1><span>Broken.</span> <span>Discontinued.</span> <span>Impossible</span> <span>to find.</span> <em>We’ll make it.</em></h1>
          <p class="lead">Custom 3D-printed parts in PLA, PETG, ASA &amp; TPU, made in a Hill Country workshop.</p>
          <div class="actions">
            <a class="btn btn-primary" href="{MAILTO}">Email Chris</a>
            <a class="btn btn-ghost" href="services.html">How it works</a>
          </div>
        </div>
        <img class="hero-art" src="img/gear-hero.svg" alt="" width="360" height="360">
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>What I make</h2>
          <p>One part or a small batch.</p>
        </div>
        <ul class="checks">
          <li><h3>Replacement parts</h3><p>Custom-made to fit</p></li>
          <li><h3>Discontinued parts</h3><p>Sourced or recreated</p></li>
          <li><h3>Appliance &amp; blender parts</h3><p>Lids, plugs, knobs</p></li>
          <li><h3>Vintage typewriter parts</h3><p>Knobs, feet, spool caps, keytops</p></li>
          <li><h3>Wall plates</h3><p>Custom &amp; odd layouts</p></li>
          <li><h3>Brackets &amp; prototypes</h3><p>Small hardware, first versions</p></li>
        </ul>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="quote">
          <h2>Bring me your broken part.</h2>
          <p>I’ll measure it and make it new.&nbsp;— Chris</p>
          <a class="quote-mail" href="{MAILTO}">{EMAIL_W}</a>
        </div>
      </div>
    </section>'''

SERVICES = f'''    <section class="page-hero">
      <div class="wrap">
        <p class="kicker accent">Services</p>
        <h1>From broken to good as new.</h1>
        <p class="lead">A simple process, the right material, and a part that fits.</p>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="section-head"><h2>How it works</h2><p>Fit first, then the finished part.</p></div>
        <div class="grid-3">
          <div class="card"><span class="num">1</span><h3>Send it</h3><p>Email a photo and rough measurements, or bring the broken part by. Tell me what it goes on.</p></div>
          <div class="card"><span class="num">2</span><h3>I measure &amp; model</h3><p>I recreate the part, print a fit sample, and adjust until it’s right.</p></div>
          <div class="card"><span class="num">3</span><h3>You get a part that fits</h3><p>Pick it up in Llano or have it shipped anywhere in the US.</p></div>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head"><h2>Materials</h2><p>Matched to the job.</p></div>
        <div class="grid-4">
          <div class="card"><span class="tag">PLA</span><p>Crisp detail for knobs, keytops, covers and indoor parts.</p></div>
          <div class="card"><span class="tag">PETG</span><p>Tough and heat-tolerant for kitchen and everyday wear.</p></div>
          <div class="card"><span class="tag">ASA</span><p>UV- and weather-resistant for outdoor and garage use.</p></div>
          <div class="card"><span class="tag">TPU</span><p>Flexible and grippy for feet, bumpers, seals and plugs.</p></div>
        </div>
        <p class="note">Not for load-bearing, electrical, stove, or child-safety parts.</p>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="quote">
          <h2>Have a part in mind?</h2>
          <p>Send a photo and I’ll tell you what’s possible.</p>
          <div class="actions"><a class="btn btn-primary" href="{MAILTO}">Email Chris</a></div>
        </div>
      </div>
    </section>'''

CONTACT = f'''    <section class="page-hero">
      <div class="wrap">
        <p class="kicker accent">Contact</p>
        <h1>Let’s make your part.</h1>
        <p class="lead">Email is the fastest way to reach me. I reply personally.</p>
      </div>
    </section>

    <section>
      <div class="wrap contact-grid">
        <div class="email-card">
          <div>
            <p class="kicker">Email</p>
            <a class="addr" href="{MAILTO}">{EMAIL_W}</a>
          </div>
          <div>
            <p class="kicker">Workshop</p>
            <p class="flush">Llano, Texas · Hill Country<br>Parts ship anywhere in the US</p>
          </div>
        </div>
        <div>
          <div class="section-head tight"><h2>What to include</h2></div>
          <ul class="include">
            <li><b>1</b><span>A photo of the part, or of the spot where it goes</span></li>
            <li><b>2</b><span>The make and model it fits, if it has one</span></li>
            <li><b>3</b><span>Rough measurements (a ruler in the photo works)</span></li>
            <li><b>4</b><span>How many you need</span></li>
          </ul>
        </div>
      </div>
    </section>'''

NF = '''    <section class="page-hero solo">
      <div class="wrap">
        <p class="kicker accent">404</p>
        <h1>This page is missing a part.</h1>
        <p class="lead">Let’s get you back on track.</p>
        <div class="actions"><a class="btn btn-primary" href="/">Go to the home page</a></div>
      </div>
    </section>'''

page("index.html", "home", f"{NAME} | Custom 3D-Printed Parts in Llano, TX",
     "Broken, discontinued, or impossible to find? Custom 3D-printed replacement parts made in Llano, Texas.", HOME)
page("services.html", "services", f"Services | {NAME}",
     "How custom part orders work, and the materials used: PLA, PETG, ASA and TPU.", SERVICES)
page("contact.html", "contact", f"Contact | {NAME}",
     f"Email {EMAIL} to get a broken or discontinued part made in Llano, Texas.", CONTACT)
page("404.html", "", f"Page not found | {NAME}", "Page not found.", NF)
print("built")

# 404.html is served at any depth, so its links/assets must be root-absolute.
import re
p = ROOT / "404.html"; s = p.read_text()
s = re.sub(r'(href|src)="(css|img|favicon)', r'\1="/\2', s)
for a in ("services.html", "contact.html"):
    s = s.replace(f'href="{a}"', f'href="/{a}"')
p.write_text(s.replace('href="./"', 'href="/"'))
