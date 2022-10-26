"""
    Common utility methods.
"""

import os

from jinja2 import Environment, FileSystemLoader


class Utilities:
    """
    This class is used to offer common utilities for
    working with Grafana objects.
    """

    @staticmethod
    def get_files(directory: str, extension: str) -> list:
        """Get files in directory with a specific file extension.
        :param directory: A directory in the filesystem containing Grafana objects.
        :param extension: A valid file extentions. Usually .yaml or .json.
        :type directory: str
        :type extension: str
        :return: list
        """
        files = []
        print(f"Finding all {extension} files in directory {directory}")
        for file in os.listdir(directory):
            if file.endswith(extension):
                files.append(os.path.join(directory, file))
        return files

    @staticmethod
    def get_resource_name(directory: str, filename: str, extension: str) -> str:
        """Get a Kubernetes resource name based on a filename.
        :param directory: A directory in the filesystem containing Grafana objects.
        :param filename: The filename to be converted.
        :param extension: A valid file extentions. Usually .yaml or .json.
        :type directory: str
        :type filename: str
        :type extension: str
        :return: str
        """
        resource_name = (
            filename.replace(directory, "")
            .replace(extension, "")
            .replace(" ", "")
            .replace("/", "")
        )
        return resource_name.lower()

    @staticmethod
    def get_content(filename: str) -> str:
        """Get a the file contents of a Grafana object.
        :param filename: The filename to be converted.
        :return: str
        """
        with open(filename, encoding="utf-8") as file:
            lines = file.readlines()
        content = "".join(lines)
        content = f"    {content}"  # In order to fix indentiation
        return content

    # pylint: disable=R0913
    @staticmethod
    def convert_file_to_k8s_resource(
        in_directory: str,
        filename: str,
        extension: str,
        template_directory: str,
        template_name: str,
        namespace: str,
        out_directory: str,
    ):
        """Get a the file contents of a Grafana object.
        :param in_directory: A directory in the filesystem containing Grafana objects.
        :param filename: The filename to be converted.
        :param extension: A valid file extentions. Usually .yaml or .json.
        :param template_directory: A directory with Jinja2 templates.
        :param template_name: The Jinja2 template used for conversion.
        :param namespace: Which namespace to create the Kubernetes resource in.
        :param out_directory: Where on file to store the Kubernetes resource YAML file.
        :type in_directory: str
        :type filename: str
        :type extension: str
        :type template_directory: str
        :type template_name: str
        :type namespace: str
        :type out_directory: str
        """
        resource_name = Utilities.get_resource_name(in_directory, filename, extension)
        print(f"Convert file {filename} to secret {resource_name}")
        file_loader = FileSystemLoader(template_directory)
        env = Environment(loader=file_loader, autoescape=False)  # nosec
        template = env.get_template(template_name)
        resource_yaml = template.render(
            resource_name=resource_name,
            namespace=namespace,
            content=Utilities.get_content(filename),
        )
        with open(
            f"{out_directory}/{resource_name}.yaml", "w", encoding="utf-8"
        ) as file:
            file.write(resource_yaml)
