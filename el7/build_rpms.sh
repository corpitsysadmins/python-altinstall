#!/bin/bash

yum -y install rpmdevtools yum-utils

rpmdev-setuptree
mv python38-altinstall.spec rpmbuild/SPECS/

yum-builddep -y rpmbuild/SPECS/python38-altinstall.spec
spectool -g -R rpmbuild/SPECS/python38-altinstall.spec
rpmbuild -ba rpmbuild/SPECS/python38-altinstall.spec
