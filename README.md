# Grafana settings

A repository for storing Grafana settings such as dashboards and datasource configurations.

## Requirements

These software packages must be installed prior to using this repo:

- Python
- git
- poetry

## Grafana Helm chart

Make sure that Grafana is deployed with the following settings:

```yaml
grafana:
  sidecar:
    dashboards:
      enabled: true
      label: grafana_dashboard
      labelValue: "1"
    datasources:
      enabled: true
      label: grafana_datasource
      labelValue: "1"
```

If searchNamespace has a value other than *null* under sidecar.dashboards, then the Grafana Dashboard ConfigMaps needs to be installed in the same namespace.

If searchNamespace has a value other than *null* under sidecar.datasources, then the Grafana Datasource Secrets needs to be installed in the same namespace. The Grafana pod needs to be restarted to pick up new datasources.

## Poetry installation

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Usage

This describes how to run the demo code in this project:

```bash
make install
make
```

## Development

### Virtual environment

```bash
poetry shell
poetry install
```

### Linter

```bash
make lint
```

### Install pre-commit hook

The Git pre-commit hook rules are defined in [.pre-commit-config.yaml](.pre-commit-config.yaml)

```bash
poetry shell
pre-commit install
```

### Git check

Check if the code can pass a git pre-commit hook.

```bash
make check
```
