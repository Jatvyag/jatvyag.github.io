# Jupyter Notebook Lab template adaptation to dark/light modes

Firstly, we need to install `jupyter`, and `nbconvert=7.16.6` libraries.

The available templates are here: `.venv/share/jupyter/nbconverter/templates`.

In order to use ordinary template we can apply the following commands:
```sh
# Dark theme
jupyter nbconvert \
  --to html \
  --template lab \
  --theme dark \
  ./src/jupyter/notebooks/en/analyse_tv.ipynb \
  --output-dir public/notebooks/en

# Light theme
jupyter nbconvert \
  --to html \
  --template lab \
  --theme light \
  ./src/jupyter/notebooks/en/analyse_tv.ipynb \
  --output-dir public/notebooks/en
```

However, for our case, this is not enough. We need to adapt templates a bit, and import both dark and light css styles. 
For that reason we can use script `export_mod_lab.py`.
This script imports both styles, listener sessionStorage, message from `ThemeSwitcher.vue` component, and fix a bit css of tables.
The notebooks are in the directories that represented the languages in which they are written. 
The notebooks could be placed in subdirectories as well, if needed.