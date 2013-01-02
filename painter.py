import os
import shutil
import sys

import re

CURRENT_JQM_VERSION = '1.2.0'

DEFAULT_THEME = {
  'a': {
    'bar': '3c3c3c'
  }
}

# Replace the value for the given field name in the CSS.
# For example, to replace the global-radii-blocks field, call this function like this:
# _R('global-radii-blocks', '0.4em')
def _R(css, field_name, value):
  #regex = r'(.*:\s*)(.*)(\s*/\*{%s}\*/)' % field_name
  regex = r'\s*([^\s]*)(\s*/\*{%s}\*/)' % field_name
  print "Replacing field", field_name, "with", value
  #print regex
  #print re.findall(regex, css)
  #import pdb
  #pdb.set_trace()
  return re.sub(regex, r'' + value + '\g<2>', css)

def normalize(theme_css):
  theme_css = _R(theme_css, 'global-radii-blocks', '0.1em')
  theme_css = _R(theme_css, 'global-radii-buttons', '0.1em')

  return theme_css

def save_css(name, theme_css, jqm_version=CURRENT_JQM_VERSION):
  filename = 'generated/%s/jquery.mobile-%s.css' % (name, jqm_version)
  d = os.path.dirname(filename)
  
  if not os.path.exists(d):
    os.makedirs(d)

  f = open(filename, 'w')
  f.write(theme_css)
  f.close()

  shutil.copy('res/index.html', d)

def gen_theme(name, base_hex, light_hex, jqm_version=CURRENT_JQM_VERSION):
  print "Generating theme", base_hex, jqm_version

  if not base_hex[0] == '#':
    base_hex = '#' + base_hex
  if not light_hex[0] == '#':
    light_hex = '#' + light_hex

  theme_css = open('res/jqm/%s/jquery.mobile-%s.css' % (jqm_version, jqm_version), 'r').read()

  theme_css = normalize(theme_css)
  
  theme_css = _R(theme_css, 'a-bar-background-end', base_hex)
  theme_css = _R(theme_css, 'a-bar-background-start', light_hex)

  save_css(name, theme_css, jqm_version)

  # Replace the bar color and highlight colors


if __name__ == "__main__":
  if len(sys.argv) < 4:
    print >> sys.stderr, "Usage: painter.py name baseColorHex lightColorHex"
    sys.exit(1)
  gen_theme(sys.argv[1], sys.argv[2], sys.argv[3])
