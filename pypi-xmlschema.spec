#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xmlschema
Version  : 2.0.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/94/44/b91e377bcb55cf9dfce5c7bc91aee50a1c4a6567d6a9a4841f2e5224d3d1/xmlschema-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/44/b91e377bcb55cf9dfce5c7bc91aee50a1c4a6567d6a9a4841f2e5224d3d1/xmlschema-2.0.0.tar.gz
Summary  : An XML Schema validator and decoder
Group    : Development/Tools
License  : MIT
Requires: pypi-xmlschema-bin = %{version}-%{release}
Requires: pypi-xmlschema-license = %{version}-%{release}
Requires: pypi-xmlschema-python = %{version}-%{release}
Requires: pypi-xmlschema-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(elementpath)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
*********
xmlschema
*********
.. image:: https://img.shields.io/pypi/v/xmlschema.svg
:target: https://pypi.python.org/pypi/xmlschema/
.. image:: https://img.shields.io/pypi/pyversions/xmlschema.svg
:target: https://pypi.python.org/pypi/xmlschema/
.. image:: https://img.shields.io/pypi/implementation/xmlschema.svg
:target: https://pypi.python.org/pypi/xmlschema/
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
:alt: MIT License
:target: https://lbesson.mit-license.org/
.. image:: https://img.shields.io/pypi/dm/xmlschema.svg
:target: https://pypi.python.org/pypi/xmlschema/
.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
:target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity

%package bin
Summary: bin components for the pypi-xmlschema package.
Group: Binaries
Requires: pypi-xmlschema-license = %{version}-%{release}

%description bin
bin components for the pypi-xmlschema package.


%package license
Summary: license components for the pypi-xmlschema package.
Group: Default

%description license
license components for the pypi-xmlschema package.


%package python
Summary: python components for the pypi-xmlschema package.
Group: Default
Requires: pypi-xmlschema-python3 = %{version}-%{release}

%description python
python components for the pypi-xmlschema package.


%package python3
Summary: python3 components for the pypi-xmlschema package.
Group: Default
Requires: python3-core
Provides: pypi(xmlschema)
Requires: pypi(elementpath)

%description python3
python3 components for the pypi-xmlschema package.


%prep
%setup -q -n xmlschema-2.0.0
cd %{_builddir}/xmlschema-2.0.0
pushd ..
cp -a xmlschema-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658186606
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . elementpath
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . elementpath
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xmlschema
cp %{_builddir}/xmlschema-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-xmlschema/7507376d580cb5b5c2ff25e049bf82420bf2ca56
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} elementpath
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xmlschema-json2xml
/usr/bin/xmlschema-validate
/usr/bin/xmlschema-xml2json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-xmlschema/7507376d580cb5b5c2ff25e049bf82420bf2ca56

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
