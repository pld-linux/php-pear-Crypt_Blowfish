%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Blowfish
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - quick two-way blowfish encryption
Summary(pl):	%{_pearname} - szybkie dwustronne szyfrowanie algorytmem blowfish
Name:		php-pear-%{_pearname}
Version:	0.8.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	78062205f22ae26052d80af20e1495a0
URL:		http://pear.php.net/package/Crypt_Blowfish/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	sed >= 4.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to preform two-way blowfish on the fly using
only PHP. This package does not require the Mcrypt PHP extension to
work.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pozwala na dwustronne szyfrowanie w locie z u�yciem algorytmu
blowfish. Klasa ta nie wymaga rozszerzenia Mcrypt.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%build
sed -i -e 's,Blowfish/DefaultKey.php,Crypt/Blowfish/DefaultKey.php,' %{_pearname}-%{version}/%{_subclass}.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
