# Beyond Borders CHS

Static website for Beyond Borders, a student club at Campolindo High School supporting
North Korean refugee college students in South Korea.

Plain HTML and CSS — no build step, no dependencies, no framework.

## Structure

```
index.html          Home — hero, officers, mission statement
about.html          About + facts list
contact.html        Email / Instagram / YouTube
donate.html         Donate (GoFundMe placeholder)
404.html            Not-found page
robots.txt
vercel.json         cleanUrls + asset cache headers
assets/
  styles.css        All styling, design tokens at the top
  logo.png          Club logo  ← PLACEHOLDER, see below
  favicon.svg
```

## ⚠️ Replace the logo

`assets/logo.png` is a **placeholder** globe mark, not the real club logo. The original
PNG in the Claude Design project is larger than the 256 KiB the export API returns, so it
came back truncated and could not be recovered.

To fix: download the real logo from the design project and save it over
`assets/logo.png`, keeping the same filename. Every page references that one path, so no
HTML changes are needed. A square-ish PNG with a transparent or cream (`#faf8f4`)
background works best.

## Local preview

Any static server works. Clean URLs (`/about` rather than `/about.html`) are a Vercel
feature, so locally use the `.html` paths or a server that resolves extensions:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploy to Vercel

1. Push this folder to a GitHub repo.
2. In Vercel: **Add New → Project**, import the repo.
3. Framework Preset: **Other**. Leave build command and output directory **empty** —
   the repo root is already the deployable site.
4. Deploy.

`vercel.json` enables `cleanUrls`, so pages are served at `/about`, `/contact`, `/donate`.

Or from the CLI:

```sh
npx vercel --prod
```

## Editing content

- **Officers** — the three `<li class="officer">` blocks in `index.html`.
- **Contact links** — the `<a class="channel">` blocks in `contact.html`.
- **Donate** — `donate.html` has the live CTA markup commented out just below the
  placeholder card. Swap the card for it and drop in the real GoFundMe URL.
- **Colors and type** — the `:root` custom properties at the top of `assets/styles.css`.
