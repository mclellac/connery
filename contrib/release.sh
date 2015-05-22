#!/bin/sh
# Runs through the steps to release a Connery version. This is only useful to
# the people with permissions to do so, of course.
set -e
cd $(dirname $0)/..

version=$(python -c "import connery; print(connery.__version__)")
echo "Releasing Connery version $version."

echo "PyPI username:"
read pypi_user
echo "PyPI password:"
read pypi_pass
echo "connery.dftba.net username:"
read server_user

cat <<EOF > ~/.pypirc
[distutils]
index-servers =
    pypi

[pypi]
username:$pypi_user
password:$pypi_pass
EOF

echo "Building package and uploading to PyPI..."
./setup.py sdist upload --sign
rm ~/.pypirc

echo "Building docs..."
cd docs
make html

echo "Setting up folders on connery.dftba.net..."
ssh $server_user@connery.dftba.net "mkdir /var/www/connery/$version; rm /var/www/connery/docs; ln -s /var/www/connery/$version/docs /var/www/connery/docs"

echo "Uploading docs..."
scp -r build/html $server_user@connery.dftba.net:/var/www/connery/$version/docs

echo "Done!"
