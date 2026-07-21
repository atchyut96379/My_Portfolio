# Fix 404 — Enable GitHub Pages (2 minutes)

Your code is on GitHub. The site shows 404 because **Pages is not turned on yet**.

## Option A — Recommended (works with `My_Portfolio` repo)

1. Open: https://github.com/atchyut96379/My_Portfolio/settings/pages
2. **Build and deployment → Source:** choose **Deploy from a branch**
3. **Branch:** select **`gh-pages`** and folder **`/ (root)`**
4. Click **Save**
5. Wait 2–5 minutes, then open: https://atchyut96379.github.io/My_Portfolio/

## Option B — No settings needed (cleaner URL)

Create a user site repo — GitHub turns on Pages automatically.

1. Open: https://github.com/new?name=atchyut96379.github.io
2. Keep name **`atchyut96379.github.io`**, Public, **no** README → Create
3. In PowerShell:

```powershell
cd D:\Projects\Portfolio
git remote add usersite https://github.com/atchyut96379/atchyut96379.github.io.git
git push usersite main:main
```

4. Wait 2–5 minutes → live at **https://atchyut96379.github.io/**

## Temporary preview (works right now)

https://htmlpreview.github.io/?https://github.com/atchyut96379/My_Portfolio/blob/main/index.html

Use this until Pages is enabled.
