%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Blowfish
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		subver	RC2
%define		rel		1
Summary:	%{_pearname} - quick two-way blowfish encryption
Summary(pl.UTF-8):	%{_pearname} - szybkie dwustronne szyfrowanie algorytmem blowfish
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	0.%{subver}.%{rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	09f0e38a4d524ba4102db5d11b07ffe9
URL:		http://pear.php.net/package/Crypt_Blowfish/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Crypt_Blowfish-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to preform two-way blowfish on the fly using
only PHP. This package does not require the Mcrypt PHP extension to
work.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pozwala na dwustronne szyfrowanie w locie z użyciem algorytmu
blowfish. Klasa ta nie wymaga rozszerzenia Mcrypt.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# badly packaged, i think
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
