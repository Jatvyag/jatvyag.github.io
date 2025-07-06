# Changes to template

We can make our own templates here. 
Then just run command like the following.

The themes are here: `.venv/share/jupyter/nbconverter/templates`

```sh
# Dark theme
jupyter nbconvert \
  --to html \
  --template=mod_lab \
  --TemplateExporter.extra_template_basedirs=./src/jupyter_templates \
  ./src/assets/notebooks/* \
  --theme dark \
  --output-dir=public/notebooks/dark

# Light theme
jupyter nbconvert \
  --to html \
  --template=mod_lab \
  --TemplateExporter.extra_template_basedirs=./src/jupyter_templates \
  ./src/assets/notebooks/* \
  --output-dir=public/notebooks/light
```

Or, if you want ordinary theme, run the following
```sh
# Dark theme
jupyter nbconvert \
  --to html \
  --template lab \
  --theme dark \
  ./src/assets/notebooks/analyse_tv.ipynb \
  --output-dir public/notebooks/dark

# Light theme
jupyter nbconvert \
  --to html \
  --template lab \
  --theme light \
  ./src/assets/notebooks/analyse_tv.ipynb \
  --output-dir public/notebooks/light
```

