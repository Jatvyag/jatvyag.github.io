# About

The repository contains the source code for a Vue-based personal application.

The code is processed, bundled, and optimized during the build step (via vite build) to produce the output, which is deployed to GitHub Pages.

## Jupyter Notebooks

The application also includes the Jupyter Notebooks to generate the content for the blog posts. The notebooks are located in the `src/jupyter/notebooks` directory. 

The HTML version of the notebooks is generated based on the "lab" template with some modifications to adapt it to the dark/light mode switching. The HTML files are generated during the build step with a Python script.

## Development
To start the development server, run the following command:

```bash
npm run dev
```

This will start the development server on port 5173.

To start ESLint, run the following command:
```bash
npm run lint
``` 

To fix ESLint issues, run the following command:
```bash
npm run lint:fix
```