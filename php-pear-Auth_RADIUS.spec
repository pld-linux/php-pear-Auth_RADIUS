%define		_status		stable
%define		_pearname	Auth_RADIUS
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Wrapper Classes for the RADIUS PECL
Summary(pl.UTF-8):	%{_pearname} - Wrapper dla klasy RADIUS PECL
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6505f01b549a6113482a3d082222183a
URL:		http://pear.php.net/package/Auth_RADIUS/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(radius) >= 1.2.5
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides wrapper-classes for the RADIUS PECL. There are
different Classes for the different authentication methods. If you are
using CHAP-MD5 or MS-CHAP you need also the Crypt_CHAP package. If you
are using MS-CHAP you need also the mhash extension.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet udostępnia klasy obudowujące RADIUS PECL. Są różne klasy
dla różnych metod uwierzytelniania. Do używania CHAP-MD5 lub MS-CHAP
potrzebny jest także pakiet Crypt_CHAP. Do MS-CHAP potrzebne jest
dodatkowo rozszerzenie mhash.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Auth/*.php
