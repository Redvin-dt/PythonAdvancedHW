import texgen as texgen
from string import Template

_TEX_TEMPLATE = Template("""\\documentclass[letterpaper,11pt]{article}                         
\\usepackage{graphicx}
\\begin{document}

$table
                         
$image

\\end{document}                        
""")

def main():
    file = open("../artifacts/document.tex", "w")
    file.write(_TEX_TEMPLATE.substitute(
        table=texgen.generate_table([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
        image=texgen.generate_image("../data/demotivator.png")
    ))


if __name__ == "__main__":
    main()
