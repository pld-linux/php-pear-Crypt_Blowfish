%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Blowfish
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - quick two-way blowfish encryption
Summary(pl):	%{_pearname} - szybkie dwustronne szyfrowanie algorytmem blowfish
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	02858a3c46db133f95a9b18c36f52688
URL:		http://pear.php.net/package/Crypt_Blowfish/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	sed >= 4.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to preform two-way blowfish on the fly using
only PHP. This package does not require the Mcrypt PHP extension to
work.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pozwala na dwustronne szyfrowanie w locie z u¿yciem algorytmu
blowfish. Klasa ta nie wymaga rozszerzenia Mcrypt.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# bad pear package
sed -i -e 's,Blowfish/DefaultKey.php,Crypt/Blowfish/DefaultKey.php,' ./%{php_pear_dir}/%{_class}/%{_subclass}.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
