"""
    This file can be used to convert
    Grafana dashboards to Kubernetes ConfigMaps.
"""
import os

from grafana_settings.utilities import Utilities

DASHBOARD_DIR: str = "./dashboards"
EXTENSION: str = ".json"
CONFIGMAP_DIR: str = "./configmaps"
TEMPLATES_DIR: str = "./templates"
TEMPLATE_NAME: str = "dashboard-configmap.yaml.j2"

# pylint: disable=R0903


class Dashboard:
    """
    This class is used to manage Grafana dashboards.
    """

    def __init__(self):
        if not os.path.exists(CONFIGMAP_DIR):
            print(f"Creating {CONFIGMAP_DIR} directory")
            os.makedirs(CONFIGMAP_DIR)

    # pylint: disable=R0801
    def convert(self, namespace: str):
        """
        This method is the entrypoint for converting
        Grafana datasources to Kubernetes secrets.
        :param namespace: Which namespace to install the Kubernetes secrets in.
        :type namespace: str
        """
        for file in Utilities.get_files(DASHBOARD_DIR, EXTENSION):
            Utilities.convert_file_to_k8s_resource(
                DASHBOARD_DIR,
                file,
                EXTENSION,
                TEMPLATES_DIR,
                TEMPLATE_NAME,
                namespace,
                CONFIGMAP_DIR,
            )
        print("\nIn order to apply changes, run:\n")
        print(f"kubectl apply -f {CONFIGMAP_DIR}\n\n")
