%define module   Test-WWW-Mechanize-CGI

Name:		perl-%{module}
Version:	0.1
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Test CGI applications with Test::WWW::Mechanize
Url:		http://search.cpan.org/dist/%{module}
Source:	http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Mechanize)
BuildRequires:	perl(WWW::Mechanize::CGI)
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
Provides a convenient way of testing CGI applications without a external
daemon.

%prep
%setup -q -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Test


%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-3mdv2010.0
+ Revision: 430601
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-2mdv2009.0
+ Revision: 268775
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2009.0
+ Revision: 213782
- import perl-Test-WWW-Mechanize-CGI


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdv2009.0
- first mdv release
