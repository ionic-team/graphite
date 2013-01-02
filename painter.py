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
  regex = r'(\s*)([^\s]*)(\s*/\*{%s}\*/)' % field_name
  #print "Replacing field", field_name, "with", value
  return re.sub(regex, r'\g<1>' + value + '\g<3>', css)

def make_theme(props, theme_css):
  for prop in props:
    theme_css = _R(theme_css, prop, props[prop])
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

  images_dir = os.path.join(d, 'images/')
  if not os.path.exists(images_dir):
    shutil.copytree('res/jqm/%s/images' % jqm_version, images_dir)

def gen_theme(settings_file):
  stream = open(settings_file, 'r')
  import yaml
  settings = yaml.load(stream)

  print "Generating theme", settings['name']

  name = settings['name']
  jqm_version = settings['jqm-version']

  theme_css = open(settings['source-theme'], 'r').read()

  theme_css = make_theme(settings, theme_css)

  save_css(name, theme_css, jqm_version)

  # Replace the bar color and highlight colors


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print >> sys.stderr, "Usage: painter.py yaml-settings-file"
    sys.exit(1)
  gen_theme(sys.argv[1])
