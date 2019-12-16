#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : multidict
Version  : 4.7.1
Release  : 15
URL      : https://files.pythonhosted.org/packages/34/68/38290d44ea34dae6d52719f0c94bd09951387cec75e36cdce6805b5f27e9/multidict-4.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/68/38290d44ea34dae6d52719f0c94bd09951387cec75e36cdce6805b5f27e9/multidict-4.7.1.tar.gz
Summary  : multidict implementation
Group    : Development/Tools
License  : Apache-2.0
Requires: multidict-license = %{version}-%{release}
Requires: multidict-python = %{version}-%{release}
Requires: multidict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
=========
multidict
=========
.. image:: https://dev.azure.com/aio-libs/multidict/_apis/build/status/CI?branchName=master
:target: https://dev.azure.com/aio-libs/multidict/_build
:alt: Azure Pipelines status for master branch

%package license
Summary: license components for the multidict package.
Group: Default

%description license
license components for the multidict package.


%package python
Summary: python components for the multidict package.
Group: Default
Requires: multidict-python3 = %{version}-%{release}

%description python
python components for the multidict package.


%package python3
Summary: python3 components for the multidict package.
Group: Default
Requires: python3-core

%description python3
python3 components for the multidict package.


%prep
%setup -q -n multidict-4.7.1
cd %{_builddir}/multidict-4.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576522175
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/multidict
cp %{_builddir}/multidict-4.7.1/LICENSE %{buildroot}/usr/share/package-licenses/multidict/9bda5c883efd96d295207e8ca8a4f38320fc2cf7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/multidict/9bda5c883efd96d295207e8ca8a4f38320fc2cf7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
