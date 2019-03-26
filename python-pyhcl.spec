# Created by pyp2rpm-3.3.2
%global pypi_name pyhcl

Name:           python-%{pypi_name}
Version:        0.3.12
Release:        1%{?dist}
Summary:        HCL configuration parser for python

License:        None
URL:            https://github.com/virtuald/pyhcl
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(ply) < 4
BuildRequires:  python3dist(ply) < 4
BuildRequires:  python3dist(ply) >= 3.8
BuildRequires:  python3dist(ply) >= 3.8
BuildRequires:  python3dist(setuptools)

%description
|Build Status|Implements a parser for HCL (HashiCorp Configuration Language) <
in Python. This implementation aims to be compatible with the original golang
version of the parser.The grammar and many of the tests/fixtures were
copied/ported from the golang parser into pyhcl. All releases are tested with a
variety of python versions from Python 2.7 onward.Installation :: pip install
pyhclUsage...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(ply) < 4
Requires:       python3dist(ply) >= 3.8
%description -n python3-%{pypi_name}
|Build Status|Implements a parser for HCL (HashiCorp Configuration Language) <
in Python. This implementation aims to be compatible with the original golang
version of the parser.The grammar and many of the tests/fixtures were
copied/ported from the golang parser into pyhcl. All releases are tested with a
variety of python versions from Python 2.7 onward.Installation :: pip install
pyhclUsage...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/hcltool
%{python3_sitelib}/hcl
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Mar 25 2019 Mike DePaulo <mikedep333@redhat.com> - 0.3.12-1
- Initial package.