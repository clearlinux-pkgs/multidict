#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : multidict
Version  : 4.5.2
Release  : 8
URL      : https://files.pythonhosted.org/packages/7f/8f/b3c8c5b062309e854ce5b726fc101195fbaa881d306ffa5c2ba19efa3af2/multidict-4.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/7f/8f/b3c8c5b062309e854ce5b726fc101195fbaa881d306ffa5c2ba19efa3af2/multidict-4.5.2.tar.gz
Summary  : multidict implementation
Group    : Development/Tools
License  : Apache-2.0
Requires: multidict-license = %{version}-%{release}
Requires: multidict-python = %{version}-%{release}
Requires: multidict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
multidict
        =========

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
%setup -q -n multidict-4.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543417280
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/multidict
cp LICENSE %{buildroot}/usr/share/package-licenses/multidict/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/multidict/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
