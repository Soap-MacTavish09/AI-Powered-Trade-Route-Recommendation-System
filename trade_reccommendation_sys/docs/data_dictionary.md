# Data Dictionary

Full variable definitions derived from the AI-Powered Trade Route Recommendation System Scoping Report.

---

## 4.1 Static and Slowly Changing Data

| Variable | Type / Format | Expected Values | Why Needed | Typical Source |
|----------|--------------|----------------|-----------|---------------|
| `port_unlocode` | Categorical string | Five-character UN/LOCODE e.g. `INMUN` | Unique port/location identifier for graph nodes | UN/LOCODE |
| `port_name` | Categorical string | Text | Human-readable label | UN/LOCODE, WPI |
| `country_code` | Categorical string | ISO 3166-1 alpha-2 / alpha-3 | Country-level filtering and aggregation | UN/LOCODE, World Bank |
| `latitude` | Numerical | −90 to 90 | Node coordinates and distance calculations | WPI, port APIs |
| `longitude` | Numerical | −180 to 180 | Node coordinates and distance calculations | WPI, port APIs |
| `port_depth_m` | Numerical | Typically 0–30+ | Vessel feasibility and draft constraints | World Port Index |
| `max_vessel_size` | Numerical / categorical | DWT, TEU, vessel class | Candidate filtering by ship size | World Port Index, port APIs |
| `berth_count` | Integer | 0+ | Approximate handling capacity | World Port Index, port authorities |
| `port_facilities_profile` | Categorical / multi-hot | Pilots, tugs, cranes, fuel, repairs, etc. | Constraint and suitability features | World Port Index |
| `port_liner_connectivity` | Numerical index | Index values or rank | Measures connection to liner networks | UNCTAD PLSCI |
| `country_lpi_score` | Numerical index | 1–5 scale or sub-scores | Proxy for logistics reliability and customs efficiency | World Bank LPI 2.0 |
| `route_distance_nm` | Numerical | 0+ | Core routing cost feature | Searoutes / Kpler / computed graph |
| `route_travel_time_hr` | Numerical | 0+ | ETA baseline for candidate routes | Searoutes / Kpler / computed graph |
| `canal_passage_flags` | Binary flags | Suez, Panama, Malacca, etc. | Hard constraint and disruption exposure | Route engine / graph rules |
| `piracy_risk_zone_flag` | Binary / score | 0/1 or 0–1 | Security risk for route ranking | Route engine / external risk layer |
| `historical_route_frequency` | Numerical count / share | 0+ | Prior likelihood of route choice | AIS history / training set |

---

## 4.2 Dynamic Operational Data

| Variable | Type / Format | Expected Values | Why Needed | Typical Source |
|----------|--------------|----------------|-----------|---------------|
| `voyage_id` | Categorical string | Unique identifier | Link ship, route, and outcome | AIS / internal ETL |
| `vessel_imo` | Categorical string | 7-digit IMO number | Vessel-level tracking and constraints | AIS API |
| `mmsi` | Categorical string | 9-digit MMSI | AIS vessel identity | AIS API |
| `timestamp_utc` | Datetime | ISO-8601 UTC | Time alignment across feeds | All sources |
| `current_position` | Geospatial point | Latitude/longitude pair | Real-time vessel state | AIS API |
| `speed_knots` | Numerical | 0+ | Progress state and ETA estimation | AIS API |
| `heading_deg` | Numerical | 0–359 | Trajectory inference | AIS API |
| `eta_to_next_stop` | Datetime / numerical | Timestamp or hours remaining | Candidate ranking and delay prediction | AIS / route engine |
| `cargo_type` | Categorical | Container, bulk, tanker, etc. | Compatibility and routing constraints | Booking / vessel system |
| `cargo_volume` | Numerical | TEU, tonnes, cbm | Capacity and load-sensitive routing | Booking / vessel system |
| `port_congestion_index` | Numerical index | Usually 0+ or rank | Core disruption signal | MarineTraffic / port dashboards |
| `port_wait_time_hr` | Numerical | 0+ | Direct delay cost from congestion | MarineTraffic / port authority |
| `berth_occupancy_pct` | Numerical | 0–100 | Capacity pressure feature | Port authority / AIS inferred |
| `weather_wind_speed` | Numerical | m/s or knots | Hazard and delay feature | NOAA NWS / GFS / Open-Meteo |
| `weather_wave_height` | Numerical | Metres | Sailing safety and speed impact | Marine weather API |
| `storm_alert_flag` | Binary | 0/1 | Hard disruption indicator | NOAA alerts / GDELT |
| `closure_flag` | Binary | 0/1 | Route impossible if closed | Port authority / news / route engine |
| `incident_type` | Categorical | strike, blockage, weather, conflict, customs | Disruption taxonomy | GDELT / port feeds |
| `incident_severity` | Ordinal / numerical | Low–Med–High or 0–1 | Route penalty weighting | Engineered from event data |
| `realized_delay_hr` | Numerical | Can be negative or positive | Training target for ETA and reroute value | Historical voyages |
| `reroute_label` | Binary / categorical | Original route kept vs alternative chosen | Supervised learning target | Historical outcomes |
| `switching_cost_usd` | Numerical | 0+ | Penalty for changing route or port | Business rules / estimates |
| `emissions_delta_kgco2` | Numerical | Can be positive or negative | Sustainability objective | Route engine / emissions model |

---

## 4.3 Training Labels and Derived Targets

| Label | Description |
|-------|-------------|
| **Chosen route label** | The actual route taken in historical voyage data |
| **Successful diversion label** | Whether an alternative route reduced delay, cost, or risk relative to the original plan |
| **Utility score label** | A scalar target computed from weighted time, cost, risk, and emissions outcomes |
| **Pairwise preference label** | Route A was better than Route B for the same origin–destination–disruption context |

---

## Disruption Taxonomy

| Category | Examples |
|----------|---------|
| Physical blockages / closures | Canal blockage, port closure, lock outage, route segment unavailable |
| Service degradation | Berth congestion, extended waiting time, reduced handling capacity |
| External hazards | Severe weather, cyclones, ice, piracy risk, conflict, sanctions |
| Administrative delays | Customs slowdown, labor strike, documentation delay, inspection backlogs |

---

## Port Crosswalk Table

The master identifier is `port_unlocode`. A crosswalk table maps it to:

- `port_name` (multiple name variants across sources)
- `wpi_id` (NGA World Port Index identifier)
- `ais_vendor_id` (MarineTraffic / Kpler internal port ID)
- `national_port_code` (country-specific codes)

See `data/external/port_crosswalk.csv` for the maintained crosswalk.
