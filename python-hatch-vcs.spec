Summary:	Hatch plugin for versioning with your preferred VCS
Name:		python-hatch-vcs
Version:	0.4.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/hatch-vcs/
Source0:	https://pypi.org/packages/source/h/hatch-vcs/hatch_vcs-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Hatch plugin for versioning with your preferred VCS

%files
%{py_sitedir}/hatch_vcs
%{py_sitedir}/hatch_vcs-*.*-info

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n hatch_vcs-%{version}

%build
%py_build

%install
%py_install

