.PHONY: help install install-dev lint format typecheck test test-cov \
        data-setup build-graph run-api clean

PYTHON   := python
PYTEST   := pytest
UVICORN  := uvicorn
SRC      := src tests scripts

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ── Setup ─────────────────────────────────────────────────────────────────────
install:  ## Install production dependencies
	pip install -r requirements.txt

install-dev:  ## Install dev + production dependencies
	pip install -r requirements-dev.txt
	pre-commit install

# ── Code quality ──────────────────────────────────────────────────────────────
lint:  ## Run ruff linter
	ruff check $(SRC)

format:  ## Auto-format code with ruff
	ruff format $(SRC)
	ruff check --fix $(SRC)

typecheck:  ## Run mypy type checker
	mypy $(SRC)

# ── Testing ───────────────────────────────────────────────────────────────────
test:  ## Run test suite
	$(PYTEST) tests/

test-cov:  ## Run tests with HTML coverage report
	$(PYTEST) --cov=src --cov-report=html --cov-report=term-missing tests/
	@echo "Coverage report: htmlcov/index.html"

test-unit:  ## Run unit tests only
	$(PYTEST) tests/unit/

test-integration:  ## Run integration tests only
	$(PYTEST) tests/integration/

# ── Data & graph ──────────────────────────────────────────────────────────────
data-setup:  ## Download public static data (UN/LOCODE, WPI)
	bash scripts/setup_data.sh

build-graph:  ## Build the maritime port graph from processed port data
	$(PYTHON) scripts/build_graph.py

# ── Application ───────────────────────────────────────────────────────────────
run-api:  ## Start FastAPI dev server
	$(UVICORN) src.api.main:app --reload --host 0.0.0.0 --port 8000

run-api-prod:  ## Start FastAPI production server
	$(UVICORN) src.api.main:app --host 0.0.0.0 --port 8000 --workers 4

# ── Cleanup ───────────────────────────────────────────────────────────────────
clean:  ## Remove build artefacts, caches, and coverage reports
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache"   -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov"       -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".coverage" -delete 2>/dev/null || true
	@echo "Clean complete."
