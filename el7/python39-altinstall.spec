# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define debug_package %{nil}
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:           python39-altinstall
Version:        3.9.0
Release:        1%{?dist}
Summary:        Interpreter of the Python programming language

License:        Python
URL:            https://www.python.org/
Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz

BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  libffi-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  tk-devel
BuildRequires:  uuid-devel
BuildRequires:  xz-devel
Provides:       /usr/local/bin/python3.9
# Don't even bother with default python. It's required by this package, that's why is listed here.
Provides:       /usr/local/bin/python

%description
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readability.
It includes an extensive standard library, and has a vast ecosystem of
third-party libraries.

This uses the upstream method using altinstall which would install in /usr/local

%prep
%setup -q -n Python-%{version}


%build
env CXX=/usr/bin/c++ %{_builddir}/Python-%{version}/configure --enable-optimizations --enable-loadable-sqlite-extensions


%install
rm -rf %{buildroot}
make altinstall DESTDIR=%{buildroot}
# Remove the bytecode generated by the installer. The bytecode is unusable because of mtime not being set correctly.
find %{buildroot} -type f -name '*.pyc' -delete
# Compress man page
%{__gzip} --name --best %{buildroot}/usr/local/share/man/man1/python3.9.1

 
%files
/usr/local/bin/2to3-3.9
/usr/local/bin/easy_install-3.9
/usr/local/bin/idle3.9
/usr/local/bin/pip3.9
/usr/local/bin/pydoc3.9
/usr/local/bin/python3.9
/usr/local/bin/python3.9-config
/usr/local/lib/libpython3.9.a
/usr/local/lib/pkgconfig/python-3.9.pc
/usr/local/lib/pkgconfig/python-3.9-embed.pc
/usr/local/include/python3.9
/usr/local/lib/python3.9
%doc /usr/local/share/man/man1/python3.9.1.gz

%changelog
* Mon Oct 12 2020 Irving Leonard <mm-irvingleonard@github.com> 3.9.0-1
- Initial RPM release
