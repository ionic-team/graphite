Graphite for jQuery Mobile
===========

Requires: jQuery Mobile 1.3.1

Graphite is a curated set of nice, simple, and clean jQuery Mobile themes based on the _default_ jQM swatches. It also comes with a generator script for building your own with a given base color and base highlight color. Since the themes are based on the default swatches, highlight swatches might not match the theme correctly for this release.

We've included a modified jQuery Mobile base theme that we use to generate the "Graphite" set of themes. This theme has a few changes made to the default theme.

Created by [Ben Sperry](http://bensperry.com/) and [Max Lynch](http://maxlynch.com/) creators of [Codiqa, the jQuery Mobile interface builder](http://codiqa.com/), and Joe Nelson of [Bendyworks](http://bendyworks.com/) in Madison, Wisconsin.

---

## Creating a custom color scheme

#### .1 Define your customized colors 

To generate a new color scheme using you're own custom colors you first need tp create a new config  file (in Yaml format). You can use the configs stored in `/themes/` as your base.

The most basic version looks something like this.

	name: candy
	'source-theme': 'res/jqm/1.3.2/jquery.mobile-1.3.2.graphite.blue.css'
	'jqm-version': '1.3.2'

	base_color: &BASE_COLOR '#f75548'
	secondary_color: &SECONDARY_COLOR '#ff6b5f'
	highlight_border_color: &HIGHLIGHT_COLOR '#a9281e'
	
You then need to add your new theme file to the `Makefile` in side the `generate` function.

	generate:
		@python helper/painter.py themes/aloe.yaml
		@python helper/painter.py themes/candy.yaml
		...
		@python helper/painter.py <<your theme location>>.yaml

#### .2 Generating your theme

To generate your new theme you need to call `generate` in the Makefile. This will call a Python script that will create the files needed for your theme.

Before calling this Python script you need to install Python and the other dependices using the following method.

*Note - this method assumes you have Python, PIP and  Virtualenv installed. For a guide on installing and using PIP and Virutalenv visit [http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/](http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)*

1. In terminal `cd` into the root directory of Graphite
2. Now create a new virutalenv by inputting `virutalenv env` into your terminal window
3. Activate your new virutalenv `source env/bin/activate`
4. Install any requirements `pip install -r requirements.txt`
5. Now you can call the makefile using `make Makefile generate`
6. Your newly generated theme will be stored at `/generated/<<name at top of theme.yaml>>`

