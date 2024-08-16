burndown:
	@echo "===================\nThings to implement\n==================="
	@rg TODO: --glob "*.py"

test:
	poetry run pytest
