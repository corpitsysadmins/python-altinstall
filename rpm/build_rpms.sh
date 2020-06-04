#!/bin/bash

yum -y install rpmdevtools

rpmdev-setuptree
mv python38.spec rpmbuild/SPECS/

spectool -g -R rpmbuild/SPECS/python38.spec
rpmbuild -ba rpmbuild/SPECS/python38.spec
