import os
import sys
from glob import glob
from traitlets.config import Config
from mod_lab.exporter import CustomHTMLExporter
from mod_lab.exporter import HeadingIDFixer
from mod_lab.exporter import StripNestedRoot


def export_notebook(input_path, output_file):
    c = Config()
    c.TemplateExporter.extra_template_basedirs = [os.path.abspath(os.path.join(os.path.dirname(__file__)))]
    c.TemplateExporter.template_name = 'mod_lab'
    
    exporter = CustomHTMLExporter(config=c)
    body, resources = exporter.from_filename(input_path)

    # Step 1: clean CSS with StripNestedRoot
    strip_root = StripNestedRoot()
    body = strip_root.postprocess(body)

    # Step 2: fix heading IDs
    heading_fixer = HeadingIDFixer(input_path)
    body = heading_fixer.feed_and_get_output(body)

    # Ensure parent dir exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write directly to the full file path
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(body)
    
    print(f"Exported {input_path} -> {output_file}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_base = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(script_dir, '../notebooks'))
    output_base = sys.argv[2] if len(sys.argv) > 2 else os.path.normpath(os.path.join(script_dir, '../../public/notebooks'))

    for input_path in glob(os.path.join(input_base, '**', '*.ipynb'), recursive=True):
        rel_path = os.path.relpath(input_path, input_base)  
        output_rel_path = os.path.splitext(rel_path)[0] + '.html'  
        output_file = os.path.join(output_base, output_rel_path)

        export_notebook(input_path, output_file)

