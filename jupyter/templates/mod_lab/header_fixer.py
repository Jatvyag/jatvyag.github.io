import re
import os
from html.parser import HTMLParser

class HeadingIDFixer(HTMLParser):
    """
    The class is used to fix heading ids in HTML exported from Jupyter Notebooks.
    """
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