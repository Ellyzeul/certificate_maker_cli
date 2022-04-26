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
    output = "\"" + dir + "\\" + filename + ".pdf\""
    cmd = "%s -O landscape --disable-smart-shrinking %s %s" % (exec, tmp_filepath, output)

    create_temp(certificate_html, tmp_filepath)

    system(cmd)

def process(csv_path, html_path, img_path):
    csv_file = open(csv_path)
    template = open(html_path).read()

    csv = reader(csv_file, delimiter=",", quotechar="\"")

    first_row = True
    header = []
    header_len = 0
    get_pattern = lambda field: "%\__"+field+"__%"
    for row in csv:
        if first_row:
            header = row
            header_len = len(header)
            first_row = False
            continue
        
        certificate_html = template

        for i in range(0, header_len):
            pattern = get_pattern(header[i])
            print(row[i])
            certificate_html = sub(pattern, row[i], certificate_html)
        
        process_on_wkhtmltopdf(certificate_html, row[0])
