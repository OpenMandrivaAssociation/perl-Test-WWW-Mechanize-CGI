%define module   Test-WWW-Mechanize-CGI
%define version    0.1
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Test CGI applications with Test::WWW::Mechanize
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::WWW::Mechanize)
BuildRequires: perl(WWW::Mechanize::CGI)
BuildRequires: perl(CGI)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Provides a convenient way of testing CGI applications without a external
daemon.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Test

