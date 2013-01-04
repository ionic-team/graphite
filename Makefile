generate-themes:
	@python helper/painter.py themes/aloe.yaml
	@python helper/painter.py themes/blue.yaml
	@python helper/painter.py themes/candy.yaml
	@python helper/painter.py themes/melon.yaml
	@python helper/painter.py themes/mint.yaml
	@python helper/painter.py themes/red.yaml
	@python helper/painter.py themes/sand.yaml
	@python helper/painter.py themes/coal.yaml

publish-themes:
	echo "Publishing themes"
	@mkdir -p docs/themes/
	@cp -R generated/* docs/themes/

all: generate-themes publish-themes
