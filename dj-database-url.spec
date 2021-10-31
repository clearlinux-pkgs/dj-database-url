#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dj-database-url
Version  : 0.5.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/01/c4/98fbf678e810029be8078419f7bba626aafa2e81bc38748757db954c477c/dj-database-url-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/c4/98fbf678e810029be8078419f7bba626aafa2e81bc38748757db954c477c/dj-database-url-0.5.0.tar.gz
Summary  : Use Database URLs in your Django Application.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: dj-database-url-license = %{version}-%{release}
Requires: dj-database-url-python = %{version}-%{release}
Requires: dj-database-url-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
dj-database-url
        ~~~~~~~~~~~~~~~

%package license
Summary: license components for the dj-database-url package.
Group: Default

%description license
license components for the dj-database-url package.


%package python
Summary: python components for the dj-database-url package.
Group: Default
Requires: dj-database-url-python3 = %{version}-%{release}

%description python
python components for the dj-database-url package.


%package python3
Summary: python3 components for the dj-database-url package.
Group: Default
Requires: python3-core
Provides: pypi(dj_database_url)

%description python3
python3 components for the dj-database-url package.


%prep
%setup -q -n dj-database-url-0.5.0
cd %{_builddir}/dj-database-url-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635724369
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
mkdir -p %{buildroot}/usr/share/package-licenses/dj-database-url
cp %{_builddir}/dj-database-url-0.5.0/LICENSE %{buildroot}/usr/share/package-licenses/dj-database-url/a86bec165cb5fd5b009fb8c04e919e2a4edbb33b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dj-database-url/a86bec165cb5fd5b009fb8c04e919e2a4edbb33b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
