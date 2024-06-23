from ambient_package_update.metadata.author import PackageAuthor
from ambient_package_update.metadata.constants import DEV_DEPENDENCIES
from ambient_package_update.metadata.package import PackageMetadata
from ambient_package_update.metadata.readme import ReadmeContent
from ambient_package_update.metadata.maintainer import PackageMaintainer
from ambient_package_update.metadata.ruff_ignored_inspection import (
    RuffIgnoredInspection,
)

METADATA = PackageMetadata(
    package_name="django-lucide-icons",
    maintainer=PackageMaintainer(
        name="Fabian Binz",
        email="fabian.binz@gmail.com",
        url="https://ambient.digital",
    ),
    authors=[
        PackageAuthor(
            name="Fabian Binz",
            email="fabian.binz@gmail.com",
        ),
    ],
    development_status="5 - Production/Stable",
    readme_content=ReadmeContent(tagline="Lucide Icons for Django", content=""),
    dependencies=["django >=3.2, < 6"],
    optional_dependencies={
        "dev": [
            *DEV_DEPENDENCIES,
        ],
        # you might add further extras here
    },
    ruff_ignore_list=[
        RuffIgnoredInspection(key="XYZ", comment="Reason why we need this exception"),
    ],
    company="Fabian Binz",
    has_migrations=False,
    supported_django_versions=["3.2", "4.0", "4.1"],
    supported_python_versions=["3.8", "3.9", "3.10"],
)
