#!/usr/bin/env python

import re
import sys

import urllib2

from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader

import xml.etree.ElementTree as ET

from weasyprint import HTML
from weasyprint import CSS

#---------------------------------------------------------------------
#
#  Usage:
#
#  ./to_render.py index.html
#  ./to_render.py --url "http://www.sbcl.org/manual/index.html"
#
#---------------------------------------------------------------------

def get_title(content):
	title = ''

	for line in content: 
		if re.search("<title>", line, re.IGNORECASE) != None:
			tree = ET.fromstring(line)
			title = tree.text
			break

	return title

def get_title_from_address(address):
	response = urllib2.urlopen(address)
	content = response.readlines()

	return get_title(content)

def get_title_from_file(filename):
	content =  open(filename)
	return get_title(content)

title = ''

if sys.argv[1] == '--url':
	title = get_title_from_address(sys.argv[2])
	source = sys.argv[2]
else:
	title = get_title_from_file(sys.argv[1])
	source = sys.argv[1]

#output = source.replace('html', 'pdf')
output = "./output.pdf"

# Define document's title
env = Environment(loader=FileSystemLoader("."))
css = env.get_template('style.css').render(title=title)

HTML(source).write_pdf(output, stylesheets=[CSS(string=css)])
