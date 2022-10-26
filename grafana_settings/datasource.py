"""
    This file can be used to convert
    Grafana datasources to Kubernetes secrets.
"""
import os

from grafana_settings.utilities import Utilities

DATASOURCE_DIR: str = "./datasources"
EXTENSION: str = ".yaml"
SECRET_DIR: str = "./secrets"
TEMPLATES_DIR: str = "./templates"
TEMPLATE_NAME: str = "datasource-secret.yaml.j2"

# pylint: disable=R0903


class Datasource:
    """
    This class is used to manage Grafana datasources.
    """

    def __init__(self):
        if not os.path.exists(SECRET_DIR):
            print(f"Creating {SECRET_DIR} directory")
            os.makedirs(SECRET_DIR)

    # pylint: disable=R0801
    def convert(self, namespace: str):
        """
        This method is the entrypoint for converting
        Grafana datasources to Kubernetes secrets.
        :param namespace: Which namespace to install the Kubernetes secrets in.
        :type namespace: str
        """
        for file in Utilities.get_files(DATASOURCE_DIR, EXTENSION):
            Utilities.convert_file_to_k8s_resource(
                DATASOURCE_DIR,
                file,
                EXTENSION,
                TEMPLATES_DIR,
                TEMPLATE_NAME,
                namespace,
                SECRET_DIR,
            )
        print("\nIn order to apply changes, run:\n")
        print(f"kubectl apply -f {SECRET_DIR}\n\n")
