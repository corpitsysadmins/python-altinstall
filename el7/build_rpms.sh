#!/bin/bash

yum -y install rpmdevtools yum-utils

rpmdev-setuptree
mv python38.spec rpmbuild/SPECS/

yum-builddep -y rpmbuild/SPECS/python38.spec
spectool -g -R rpmbuild/SPECS/python38.spec
rpmbuild -ba rpmbuild/SPECS/python38.spec
