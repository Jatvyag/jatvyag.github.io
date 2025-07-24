# Jupyter Notebook Lab template adaptation to dark/light modes

Firstly, we need to install `jupyter`, and `nbconvert=7.16.6` libraries.

The available templates are here: `.template_venv/share/jupyter/nbconverter/templates`.

In order to use ordinary template (from ./src/jupyter), we need to run the following command:
```sh
# Dark theme
jupyter nbconvert \
  --to html \
  --template lab \
  --theme dark \
  ../notebooks/en/analyse_tv.ipynb \
  --output-dir ../../public/notebooks/en

# Light theme
jupyter nbconvert \
  --to html \
  --template lab \
  --theme light \
  ../notebooks/en/analyse_tv.ipynb \
  --output-dir ../../public/notebooks/en
```

However, for our case, this is not enough. We need to adapt templates a bit:
- import both dark and light css styles
- add listener to sessionStorage, where the value of `theme` is stored (the listener is used in the `ThemeSwitcher.vue` component)
- fix of tables css
- fix of heading ids in HTML exported from Jupyter Notebooks

The notebooks are in the directories that represented the languages in which they are written. The notebooks could be placed in subdirectories as well, if needed.

To convert the notebooks, we need to run from this directory the following command:

```sh
python3 export_mod_lab.py
```
