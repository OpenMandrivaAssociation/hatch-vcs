Summary:	Hatch plugin for versioning with your preferred VCS
Name:		python-hatch-vcs
Version:	0.3.0
Release:	3
License:	GPL
Group:		Development/Python
URL:		https://pypi.org/project/hatch-vcs/
Source0:	https://files.pythonhosted.org/packages/source/h/hatch_vcs/hatch_vcs-%{version}.tar.gz
# https://github.com/ofek/hatch-vcs/issues/8
Patch0:		https://github.com/ofek/hatch-vcs/commit/47364faf5563df0eaa631ed10383817762c6b547.patch
BuildRequires:	python-pip
BuildRequires:	python3dist(hatchling)
BuildArch:	noarch
Requires:	python%{pyver}dist(setuptools-scm)
Requires:	python%{pyver}dist(hatchling)

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
