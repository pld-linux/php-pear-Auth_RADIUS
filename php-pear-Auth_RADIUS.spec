%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define		_subclass	RADIUS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Wrapper Classes for the RADIUS PECL
Summary(pl):	%{_pearname} - Wrapper dla klasy RADIUS PECL
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	33bc926537310799e2cc3a3451aa8585
URL:		http://pear.php.net/package/Auth_RADIUS/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pecl-radius >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides wrapper-classes for the RADIUS PECL. There are
different Classes for the different authentication methods. If you are
using CHAP-MD5 or MS-CHAP you need also the Crypt_CHAP package. If you
are using MS-CHAP you need also the mhash extension.

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet udostêpnia klasy obudowuj±ce RADIUS PECL. S± ró¿ne klasy
dla ró¿nych metod uwierzytelniania. Do u¿ywania CHAP-MD5 lub MS-CHAP
potrzebny jest tak¿e pakiet Crypt_CHAP. Do MS-CHAP potrzebne jest
dodatkowo rozszerzenie mhash.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples/*
%{php_pear_dir}/%{_class}/*.php
