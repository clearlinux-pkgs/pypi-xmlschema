#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-xmlschema
Version  : 2.4.0
Release  : 42
URL      : https://files.pythonhosted.org/packages/ad/67/3c978288628c14696b66a8aef9341909ce0c3ba74be858234eb6a359b6a5/xmlschema-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/67/3c978288628c14696b66a8aef9341909ce0c3ba74be858234eb6a359b6a5/xmlschema-2.4.0.tar.gz
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
%setup -q -n xmlschema-2.4.0
cd %{_builddir}/xmlschema-2.4.0
pushd ..
cp -a xmlschema-2.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690556347
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
cp %{_builddir}/xmlschema-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-xmlschema/042c68f16f2d66075973b93104fe04d14095f2aa || :
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
/usr/share/package-licenses/pypi-xmlschema/042c68f16f2d66075973b93104fe04d14095f2aa

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
