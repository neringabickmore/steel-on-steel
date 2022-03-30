# Project set up

## Virtual environment

1. `pip3 install -r requirements.txt`
2. Create `env.py` file with the following variables and add the file to `.gitignore`

``` python

import os

os.environ.setdefault("IP", "127.0.0.1")
os.environ.setdefault("PORT", "5500")
os.environ.setdefault("SECRET_KEY", "your_secret_key")
os.environ.setdefault("DEBUG", "development")
```

3. Run the app with the command: `python app.py` (thats if your file is called `app.py`)

## SCSS

1. Create `sass` folder with `main.scss` file with appropriate imports (i.e. `@import "base";` for `_base.scss` file etc).
2. To compile, prefix and build your `CSS`, install **LIVE SASS COMPILER** in your IDE (I am using VS Code) and keep it running in the background.
3. In your `head.html` file, make sure you have a correct link to your compiled css file.
4. Job done.
