%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

%global pypi_name PyMySQL

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        1.0.2
Release:        2%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}/
Source0:        %pypi_source

# Security fix for CVE-2024-36039: SQL injection if used with untrusted JSON input
# Resolved upstream: https://github.com/PyMySQL/PyMySQL/commit/521e40050cb386a499f68f483fefd144c493053c
# Tracking bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=2282821
Patch0:         CVE-2024-36039.patch

BuildArch:      noarch


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
# rsa extra
BuildRequires:  python%{python3_pkgversion}-cryptography
# ed25519 extra
# Disabled in RHEL due to missing dependency
# BuildRequires:  python%%{python3_pkgversion}-pynacl

%{?python_extras_subpkg:%python_extras_subpkg -n python%{python3_pkgversion}-%{pypi_name} -i %{python3_sitelib}/*.egg-info rsa}

%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%prep
%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info
# Remove tests files so they are not installed globally.
rm -rf tests


%build
%py3_build


%install
%py3_install


%check
# Tests cannot be launch on koji, they require a mysqldb running.


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pymysql/

%changelog
* Fri May 31 2024 Charalampos Stratakis <cstratak@redhat.com> - 1.0.2-2
- Security fix for CVE-2024-36039
Resolves: RHEL-38370

* Wed Nov 30 2022 Charalampos Stratakis <cstratak@redhat.com> - 1.0.2-1
- Initial package
- Fedora contributions by:
      Benjamin A. Beasley <code@musicinmybrain.net>
      Carl George <carl@george.computer>
      Damien Ciabrini <dciabrin@redhat.com>
      Haikel Guemar <hguemar@fedoraproject.org>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Itamar Reis Peixoto <itamar@ispbrasil.com.br>
      Julien Enselme <jujens@jujens.eu>
      Lumir Balhar <lbalhar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
