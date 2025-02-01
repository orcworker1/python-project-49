install: 
	uv sync

brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime

brain-games: 
	uv run brain-games


build: 
	uv build

package-install: 
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

lint-1:
	uv run ruff check --fix brain_games