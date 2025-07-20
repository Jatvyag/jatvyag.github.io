import re
import os
from html.parser import HTMLParser
from nbconvert.exporters.html import HTMLExporter


class HeadingIDFixer(HTMLParser):
    def __init__(self, file_path):
        super().__init__()
        self.output = []
        self.used_ids = set()
        self.counter_by_level = {}

        # Extract directory name and file name without extension
        self.dir_name = self.slugify(os.path.basename(os.path.dirname(file_path)))
        base_file = os.path.basename(file_path)
        self.file_name = self.slugify(os.path.splitext(base_file)[0])

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3"):
            level = tag
            count = self.counter_by_level.get(level, 1)
            new_id = self.make_unique_id(level, count)
            self.counter_by_level[level] = count + 1

            # Remove old id and add the new one
            attrs = [(k, v) for k, v in attrs if k != "id"]
            attrs.append(("id", new_id))
        self.output.append(f"<{tag}{self.format_attrs(attrs)}>")

    def handle_endtag(self, tag):
        self.output.append(f"</{tag}>")

    def handle_data(self, data):
        self.output.append(data)

    def format_attrs(self, attrs):
        return ''.join(f' {k}="{v}"' for k, v in attrs)

    def make_unique_id(self, level, count):
        base_id = f"{self.dir_name}-{self.file_name}-{level}-{count}"
        if base_id in self.used_ids:
            suffix = 1
            while f"{base_id}-{suffix}" in self.used_ids:
                suffix += 1
            base_id = f"{base_id}-{suffix}"
        self.used_ids.add(base_id)
        return base_id

    def slugify(self, value):
        return re.sub(r'[^\w\-]', '-', value.strip().lower())

    def feed_and_get_output(self, html):
        self.feed(html)
        return ''.join(self.output)
    

class StripNestedRoot:
    """
    The class removes nested :root { in dark in light theme css blocks.
    """
    def __init__(self):
        pass
    
    def postprocess(self, html, resources=None):
        """
        Takes only html as input and postprocess file in-memory
        """
        lines = html.splitlines()
        new_lines = []
        skip_next = False
        found_md_comment = False

        for i, line in enumerate(lines):
            # === Rule 1: Detect MD comment, then line with "*/", then empty line, and finally ":root {" ===
            if "all of MD as it is not optimized for dense, information rich UIs." in line:
                found_md_comment = True
                new_lines.append(line)
                continue
            if found_md_comment:
                if line.strip() == "*/":
                    new_lines.append(line)
                    continue
                elif line.strip() == "":
                    new_lines.append(line)
                    continue
                elif line.strip() == ":root {":
                    found_md_comment = False  # reset
                    continue  # skip this line
                else:
                    found_md_comment = False  # no match, reset

            # === Rule 2: Remove next line after switch color var ===
            if skip_next:
                skip_next = False  # reset
                continue  # skip closing }

            if line.strip().startswith("--jp-switch-true-position-color:"):
                new_lines.append(line)
                skip_next = True
                continue
        
            # Default behavior: keep the line
            new_lines.append(line)

        # Add footer marker for debugging
        return "\n".join(new_lines) + "\n<!-- StripNestedRoot was here -->\n"


class CustomHTMLExporter(HTMLExporter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strip_nested_root = StripNestedRoot()
        
    def from_filename(self, filename, resources=None, **kw):
        body, resources = super().from_filename(filename, resources=resources, **kw)
        body = self.strip_nested_root.postprocess(body)
        return body, resources

