Name:		python-hatch-vcs
Version:	0.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/hatch_vcs/hatch_vcs-%{version}.tar.gz
Summary:	Hatch plugin for versioning with your preferred VCS
URL:		https://pypi.org/project/hatch-vcs/
License:	GPL
Group:		Development/Python
BuildRequires:	python-pip
BuildRequires:	python3dist(hatchling)
BuildArch:	noarch

%description
Hatch plugin for versioning with your preferred VCS

%prep
%autosetup -p1 -n hatch_vcs-%{version}

%build
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%{py_puresitedir}/hatch_vcs
%{py_puresitedir}/hatch_vcs*info
