"""
scripts/build_graph.py
──────────────────────
One-off script to build the maritime port graph from processed port data.
Outputs a serialised NetworkX graph to data/processed/graphs/.

Usage:
    python scripts/build_graph.py [--config configs/pipeline_config.yaml]
"""

from __future__ import annotations

import argparse
import pickle
from pathlib import Path

import yaml
from loguru import logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build maritime port graph")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/pipeline_config.yaml"),
        help="Path to pipeline config YAML",
    )
    return parser.parse_args()


def load_config(config_path: Path) -> dict:
    with config_path.open() as f:
        return yaml.safe_load(f)


def main() -> None:
    args = parse_args()
    config = load_config(args.config)

    graph_cfg = config["graph"]
    output_path = Path(graph_cfg["output_path"])
    output_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Building maritime port graph...")
    logger.info(f"  Min port depth: {graph_cfg['min_port_depth_m']} m")
    logger.info(f"  Max edge distance: {graph_cfg['max_edge_distance_nm']} nm")
    logger.info(f"  Canals included: {graph_cfg['include_canals']}")

    # ── Import graph builder (implemented in src/graph/) ─────────────────────
    # Uncomment once src/graph/builder.py is implemented:
    # from src.graph.builder import MaritimeGraphBuilder
    # builder = MaritimeGraphBuilder(config)
    # G = builder.build()
    # with output_path.open("wb") as f:
    #     pickle.dump(G, f)
    # logger.info(f"Graph saved to {output_path} ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")

    logger.warning("Graph builder not yet implemented. Add src/graph/builder.py to proceed.")


if __name__ == "__main__":
    main()
