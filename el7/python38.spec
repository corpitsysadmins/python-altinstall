# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:           python38-altinstall
Version:        3.8.3
Release:        1%{?dist}
Summary:        Interpreter of the Python programming language.

License:        Python
URL:            https://www.python.org/
Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz

BuildRequires:  python3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  uuid-devel
BuildRequires:  readline-devel
BuildRequires:  openssl-devel
BuildRequires:  make
Requires:		uuid
Requires:		libuuid
Requires:		readline
Requires:		openssl

%description
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

This uses the upstream method using altinstall which would install in /usr/local

%prep
%setup -q -n Python-%{version}


%build
env CXX=/usr/bin/c++ $RPM_BUILD_DIR/Python-%{version}/configure --enable-optimizations --enable-loadable-sqlite-extensions


%install
rm -rf $RPM_BUILD_ROOT
make altinstall DESTDIR=$RPM_BUILD_ROOT

 
%files
/usr/local/bin/2to3-3.8
/usr/local/bin/easy_install-3.8
/usr/local/bin/idle3.8
/usr/local/bin/pip3.8
/usr/local/bin/pydoc3.8
/usr/local/bin/python3.8
/usr/local/bin/python3.8-config
/usr/local/lib/libpython3.8.a
/usr/local/lib/pkgconfig/python-3.8.pc
/usr/local/lib/pkgconfig/python-3.8-embed.pc
/usr/local/include/python3.8
/usr/local/lib/python3.8
%doc /usr/local/share/man/man1/python3.8.1

%changelog
