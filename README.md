# Template repository

This is a template repository with basic project set up.

## Virtual environment set up

1. `pip3 install -r requirements.txt`
2. Create `env.py` file with the following variables and add the file to `.gitignore`

``` python

import os

os.environ.setdefault("IP", "127.0.0.1")
os.environ.setdefault("PORT", "5500")
os.environ.setdefault("SECRET_KEY", "your_secret_key")
os.environ.setdefault("DEBUG", "development")
```

3. Run the app with the command: `python app.py`

## SCSS set up

### To install SCSS packages

**in terminal:**

1. `npm init` and follow the instructions to complete the initial set up
2. ` npm install ` to install all the packages in **package.json** file

### To add *prefixes* in `main.scss` file automatically in VS Code

1. Install Live Sass Compiler
2. Run *Watch Sass* in the background

### To initiate live server in development

- **in terminal:** `npm start`

### To compile code

- **in terminal:** `npm compress:css`. Make sure that you have **watch sass** running in the background to update `main.css` file.

### To build build your project ready for deployment

- **in terminal:** `npm build:css`
