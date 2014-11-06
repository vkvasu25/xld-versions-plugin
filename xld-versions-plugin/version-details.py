version_id = request.query["version"]

packages = {}

version = repositoryService.read(version_id)
if version.type == 'udm.CompositePackage':
    for package in version.packages:
        package_name = package.id.rsplit('/',1)[0]
        package_version = package.id.rsplit('/',1)[1]
        packages[package_name] = package_version
else:
    package_name = version.id.rsplit('/',1)[0]
    package_version = version.id.rsplit('/',1)[1]
    packages[package_name] = package_version

response.entity = {'id': version_id, 'packages': packages}
