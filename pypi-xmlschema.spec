#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : pypi-xmlschema
Version  : 3.4.5
Release  : 63
URL      : https://files.pythonhosted.org/packages/dd/de/a3b013b89addf4e22ea764acccc7c1a4f7ad407ea90d2acef8326b7921ef/xmlschema-3.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/de/a3b013b89addf4e22ea764acccc7c1a4f7ad407ea90d2acef8326b7921ef/xmlschema-3.4.5.tar.gz
Summary  : An XML Schema validator and decoder
Group    : Development/Tools
License  : MIT
Requires: pypi-xmlschema-bin = %{version}-%{release}
Requires: pypi-xmlschema-license = %{version}-%{release}
Requires: pypi-xmlschema-python = %{version}-%{release}
Requires: pypi-xmlschema-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n xmlschema-3.4.5
cd %{_builddir}/xmlschema-3.4.5
pushd ..
cp -a xmlschema-3.4.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742765022
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . elementpath
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . elementpath
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xmlschema
cp %{_builddir}/xmlschema-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-xmlschema/2daaf71cd8ac37f4a9ea4b5003a1d43a56aef9be || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} elementpath
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
/usr/share/package-licenses/pypi-xmlschema/2daaf71cd8ac37f4a9ea4b5003a1d43a56aef9be

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
