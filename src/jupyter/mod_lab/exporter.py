from nbconvert.exporters.html import HTMLExporter


class StripNestedRoot:
    """
    The class removes nested :root { in dark in light theme css blocks
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
            # Rule 1: Detect MD comment, then line with "*/", then empty line, and finally ":root {"
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

            # Rule 2: Remove next line after switch color var
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

