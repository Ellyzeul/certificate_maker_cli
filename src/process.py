from csv import reader
from re import sub
from os.path import dirname
from os import system


def create_temp(text, path):
    file = open(path, 'w')

    file.write(text)
    file.close()

def process_on_wkhtmltopdf(certificate_html, filename):
    dir = dirname(dirname(__file__))
    exec = dir + "\\wkhtmltox\\bin\\wkhtmltopdf.exe"
    tmp_filepath = dir + "\\temp.html"
    output = "\"" + dir + "\\" + filename
    cmd = "%s -O landscape --disable-smart-shrinking --enable-local-file-access --images -s A4 -T 0 -B 0 -L 0 -R 0 %s %s" % (exec, tmp_filepath, output)

    create_temp(certificate_html, tmp_filepath)

    system(cmd)
    system("del %s" % tmp_filepath)

def process(csv_path, html_path, img_path, naming_pattern):
    csv_file = open(csv_path)
    template = open(html_path).read()

    csv = reader(csv_file, delimiter=",", quotechar="\"")

    first_row = True
    header = []
    header_len = 0
    get_pattern = lambda field: "%\__"+field+"__%"

    print(html_path)
    print(img_path)
    img_path = sub("\\\\", "/", img_path)
    template = sub(get_pattern("IMAGE"), img_path, template)
    for row in csv:
        if first_row:
            header = row
            header_len = len(header)
            first_row = False
            continue
        
        certificate_html = template
        filename = naming_pattern

        for i in range(0, header_len):
            pattern = get_pattern(header[i])
            row[i].encode("cp1252").decode("utf8")
            certificate_html = sub(pattern, row[i], certificate_html)
            filename = sub(header[i], row[i], filename)

        process_on_wkhtmltopdf(certificate_html, "output\\%s.pdf" % filename)
