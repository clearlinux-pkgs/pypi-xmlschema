#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlschema
Version  : 1.9.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/fc/89/cafdaabbf2725472f0b7feaa6daf1883b65742dd5137f03a2f32da852947/xmlschema-1.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/89/cafdaabbf2725472f0b7feaa6daf1883b65742dd5137f03a2f32da852947/xmlschema-1.9.1.tar.gz
Summary  : An XML Schema validator and decoder
Group    : Development/Tools
License  : MIT
Requires: xmlschema-bin = %{version}-%{release}
Requires: xmlschema-license = %{version}-%{release}
Requires: xmlschema-python = %{version}-%{release}
Requires: xmlschema-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(elementpath)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

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
.. image:: https://travis-ci.org/sissaschool/xmlschema.svg?branch=master
:target: https://travis-ci.org/sissaschool/xmlschema
.. image:: https://img.shields.io/pypi/dm/xmlschema.svg
:target: https://pypi.python.org/pypi/xmlschema/
.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
:target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity

%package bin
Summary: bin components for the xmlschema package.
Group: Binaries
Requires: xmlschema-license = %{version}-%{release}

%description bin
bin components for the xmlschema package.


%package license
Summary: license components for the xmlschema package.
Group: Default

%description license
license components for the xmlschema package.


%package python
Summary: python components for the xmlschema package.
Group: Default
Requires: xmlschema-python3 = %{version}-%{release}

%description python
python components for the xmlschema package.


%package python3
Summary: python3 components for the xmlschema package.
Group: Default
Requires: python3-core
Provides: pypi(xmlschema)
Requires: pypi(elementpath)

%description python3
python3 components for the xmlschema package.


%prep
%setup -q -n xmlschema-1.9.1
cd %{_builddir}/xmlschema-1.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639063033
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xmlschema
cp %{_builddir}/xmlschema-1.9.1/LICENSE %{buildroot}/usr/share/package-licenses/xmlschema/7507376d580cb5b5c2ff25e049bf82420bf2ca56
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xmlschema-json2xml
/usr/bin/xmlschema-validate
/usr/bin/xmlschema-xml2json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmlschema/7507376d580cb5b5c2ff25e049bf82420bf2ca56

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
