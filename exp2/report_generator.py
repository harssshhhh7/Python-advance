class ReportTemplate:
    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    def add_section(self, section):
        self.sections.append(section)


class ReportGenerator:
    _formatters = {}

    def __init__(self, template, **options):
        self.template = template
        self.options = options

    @classmethod
    def register_formatter(cls, name):
        def decorator(func):
            cls._formatters[name] = func
            return func
        return decorator

    @classmethod
    def get_formatter(cls, name):
        return cls._formatters.get(name)

    def apply_formatters(self, text):
        result = text
        for name in self.options.get("formatters", []):
            formatter = self.get_formatter(name)
            if formatter:
                result = formatter(result)
            else:
                print(f"Formatter '{name}' is not available.")
        return result

    def generate(self):
        lines = []
        title = self.template.title.upper() if self.options.get("uppercase_title", False) else self.template.title
        lines.append(title)

        for section in self.template.sections:
            lines.append(self.apply_formatters(section))

        return "\n".join(lines)

    def __str__(self):
        return self.generate()

    def __repr__(self):
        return f"ReportGenerator(template={self.template.title!r}, options={self.options!r})"


@ReportGenerator.register_formatter("uppercase")
def uppercase(text):
    return text.upper()


@ReportGenerator.register_formatter("title_case")
def title_case(text):
    return text.title()


@ReportGenerator.register_formatter("wrap")
def wrap(text):
    return text.replace(" ", " | ")


@ReportGenerator.register_formatter("reverse")
def reverse(text):
    return text[::-1]


def get_user_input():
    title = input("Enter report title: ").strip() or "Untitled Report"

    sections = []
    print("Enter sections one by one. Press Enter on an empty line to finish:")
    while True:
        section = input("Section: ").strip()
        if not section:
            break
        sections.append(section)

    formatter_names = input("Enter formatters (uppercase, title_case, wrap, reverse) separated by commas: ").strip()
    if formatter_names:
        formatters = [name.strip() for name in formatter_names.split(",") if name.strip()]
    else:
        formatters = []

    uppercase_title = input("Make the title uppercase? (y/n): ").strip().lower() in {"y", "yes", "true", "1"}

    return title, sections, formatters, uppercase_title


if __name__ == "__main__":
    title, sections, formatters, uppercase_title = get_user_input()
    template = ReportTemplate(title, sections)
    report = ReportGenerator(template, formatters=formatters, uppercase_title=uppercase_title)

    print("\nGenerated Report:\n")
    print(report)
    print("\nObject Representation:")
    print(repr(report))