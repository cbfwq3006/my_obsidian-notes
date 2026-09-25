const { chromium } = require('playwright');
(async() => {
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({userAgent:'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'});
  const url = process.argv[2];
  await page.goto(url, {waitUntil:'domcontentloaded', timeout:60000});
  await page.waitForTimeout(4000);
  const out = await page.evaluate(() => ({
    title: document.title,
    bodyText: document.body ? document.body.innerText.slice(0,3000) : '',
    article: document.querySelector('#js_content')?.innerText?.slice(0,3000) || '',
    biz: window.biz || '',
    nick: window.nickname || ''
  }));
  console.log(JSON.stringify(out,null,2));
  await browser.close();
})();
