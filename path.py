from pathlib import Path
import tests


def path_schemas(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'schema/{file_name}'))


def path_resources(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'resources/{file_name}'))


