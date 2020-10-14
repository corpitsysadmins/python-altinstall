#!/bin/bash

if [ $# -ne 1 ]; then
  echo 1>&2 "Usage: $0 PYTHON_SPEC_VERSION"
  exit 3
fi

yum -y install rpmdevtools yum-utils

rpmdev-setuptree

for spec_files in *.spec; do
	
	if [ -e "$spec_files" ]; then
		mv *.spec rpmbuild/SPECS/
	else
		echo "No new specs files were found"
	fi
    
    break
done

yum-builddep -y rpmbuild/SPECS/python$1-altinstall.spec
spectool -g -R rpmbuild/SPECS/python$1-altinstall.spec
rpmbuild -ba rpmbuild/SPECS/python$1-altinstall.spec
