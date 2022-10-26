#!/usr/bin/env python3
"""
    This file can be used to convert Grafana datasources YAML files
    to Kubernetes secrets, and to convert Grafana dashboard JSON files
    to Kubernetes ConfigMaps.
"""
import os

from grafana_settings.dashboard import Dashboard
from grafana_settings.datasource import Datasource

if __name__ == "__main__":
    datasources_namespace: str = os.getenv(
        "GRAFANA_DATASOURCES_NAMESPACE", "monitoring"
    )
    dashboards_namespace: str = os.getenv("GRAFANA_DASHBOARDS_NAMESPACE", "monitoring")
    datasource: Datasource = Datasource()
    datasource.convert(datasources_namespace)
    dashboard: Dashboard = Dashboard()
    dashboard.convert(dashboards_namespace)
