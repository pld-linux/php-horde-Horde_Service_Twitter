%define		status		stable
%define		pearname	Horde_Service_Twitter
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Twitter client
Name:		php-horde-Horde_Service_Twitter
Version:	1.0.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	4df9b3e6ff60f392a72878d8609c105c
URL:		http://pear.horde.org/package/Horde_Service_Twitter/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Controller < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Http < 2.0.0
Requires:	php-horde-Horde_Oauth < 2.0.0
Requires:	php-horde-Horde_Url < 2.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides client libraries for the Twitter REST API.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Horde_Service_Twitter/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Horde/Service
%{php_pear_dir}/Horde/Service/Twitter.php
%{php_pear_dir}/Horde/Service/Twitter
