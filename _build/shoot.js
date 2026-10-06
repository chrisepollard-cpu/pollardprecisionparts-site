// node _build/shoot.js  -> preview-*.png (needs playwright-core + Chrome)
const { chromium } = require('/node_modules/playwright-core');
const path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox'] });
  const shots = [
    ['index.html', 'desktop', { width: 1440, height: 900 }, 1],
    ['index.html', 'phone', { width: 390, height: 844 }, 3],
    ['services.html', 'services-desktop', { width: 1440, height: 900 }, 1],
    ['contact.html', 'contact-desktop', { width: 1440, height: 900 }, 1],
    ['contact.html', 'contact-phone', { width: 390, height: 844 }, 3],
  ];
  for (const [file, name, viewport, dpr] of shots) {
    const ctx = await browser.newContext({ viewport, deviceScaleFactor: dpr });
    const page = await ctx.newPage();
    await page.goto('file://' + path.join(root, file));
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(root, `preview-${name}.png`), fullPage: true });
    await ctx.close();
  }
  await browser.close();
  console.log('done');
})();
