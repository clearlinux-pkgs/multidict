#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : multidict
Version  : 4.4.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/3b/83/3ef3889c4bd1a5145b8b4c02f1be6cf174d3824f806968506c8912e65692/multidict-4.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/83/3ef3889c4bd1a5145b8b4c02f1be6cf174d3824f806968506c8912e65692/multidict-4.4.0.tar.gz
Summary  : multidict implementation
Group    : Development/Tools
License  : Apache-2.0
Requires: multidict-python3
Requires: multidict-license
Requires: multidict-python
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
Requires: multidict-python3

%description python
python components for the multidict package.


%package python3
Summary: python3 components for the multidict package.
Group: Default
Requires: python3-core

%description python3
python3 components for the multidict package.


%prep
%setup -q -n multidict-4.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536088470
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/multidict
cp LICENSE %{buildroot}/usr/share/doc/multidict/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/multidict/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
