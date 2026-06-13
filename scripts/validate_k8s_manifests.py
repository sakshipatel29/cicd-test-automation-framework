from pathlib import Path

import yaml

REQUIRED_FILES = [
    "k8s/deployment.yaml",
    "k8s/service.yaml",
]


def load_yaml_file(file_path: str) -> dict:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Missing Kubernetes manifest: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML structure in {file_path}")

    return data


def validate_required_fields(file_path: str, manifest: dict) -> None:
    required_fields = ["apiVersion", "kind", "metadata", "spec"]

    for field in required_fields:
        if field not in manifest:
            raise ValueError(f"{file_path} is missing required field: {field}")


def main() -> None:
    for file_path in REQUIRED_FILES:
        manifest = load_yaml_file(file_path)
        validate_required_fields(file_path, manifest)

        kind = manifest.get("kind")
        name = manifest.get("metadata", {}).get("name")

        print(f"Validated {file_path}: kind={kind}, name={name}")

    print("All Kubernetes manifests are valid.")


if __name__ == "__main__":
    main()
