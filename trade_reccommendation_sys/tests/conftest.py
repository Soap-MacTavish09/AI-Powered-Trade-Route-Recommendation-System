"""
tests/conftest.py
Shared pytest fixtures available to all tests.
"""

from __future__ import annotations

import pytest


@pytest.fixture(scope="session")
def sample_port_data() -> list[dict]:
    """Minimal port records for unit testing graph construction."""
    return [
        {
            "port_unlocode": "SGSIN",
            "port_name": "Singapore",
            "country_code": "SG",
            "latitude": 1.264,
            "longitude": 103.820,
            "port_depth_m": 20.0,
            "berth_count": 50,
        },
        {
            "port_unlocode": "NLRTM",
            "port_name": "Rotterdam",
            "country_code": "NL",
            "latitude": 51.920,
            "longitude": 4.480,
            "port_depth_m": 23.0,
            "berth_count": 80,
        },
        {
            "port_unlocode": "AEDXB",
            "port_name": "Dubai (Jebel Ali)",
            "country_code": "AE",
            "latitude": 24.985,
            "longitude": 55.061,
            "port_depth_m": 17.0,
            "berth_count": 67,
        },
    ]


@pytest.fixture(scope="session")
def sample_disruption() -> dict:
    """Minimal disruption event for ranking tests."""
    return {
        "incident_type": "blockage",
        "incident_severity": 0.9,
        "affected_segment": "suez_canal",
        "closure_flag": 1,
        "timestamp_utc": "2024-03-20T06:00:00Z",
    }
