%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Blowfish
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - quick two-way blowfish encryption
Summary(pl.UTF-8):	%{_pearname} - szybkie dwustronne szyfrowanie algorytmem blowfish
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	93873efe07a267b2b415965994a0af98
URL:		http://pear.php.net/package/Crypt_Blowfish/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
