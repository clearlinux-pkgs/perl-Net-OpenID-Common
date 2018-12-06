#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-OpenID-Common
Version  : 1.20
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Common-1.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/W/WR/WROG/Net-OpenID-Common-1.20.tar.gz
Summary  : 'Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-OpenID-Common-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Crypt::DH::GMP)
BuildRequires : perl(HTML::Parser)
BuildRequires : perl(HTTP::Headers::Util)
BuildRequires : perl(HTTP::Message)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Status)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Escape)
BuildRequires : perl(XML::Simple)

%description
This archive contains the distribution Net-OpenID-Common,
version 1.20:
Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server

%package dev
Summary: dev components for the perl-Net-OpenID-Common package.
Group: Development
Provides: perl-Net-OpenID-Common-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-OpenID-Common package.


%package license
Summary: license components for the perl-Net-OpenID-Common package.
Group: Default

%description license
license components for the perl-Net-OpenID-Common package.


%prep
%setup -q -n Net-OpenID-Common-1.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-OpenID-Common
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-OpenID-Common/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/Common.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/Extension.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/Extension/SimpleRegistration.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/ExtensionMessage.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/IndirectMessage.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/URIFetch.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/Yadis.pm
/usr/lib/perl5/vendor_perl/5.28.1/Net/OpenID/Yadis/Service.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::OpenID::Common.3
/usr/share/man/man3/Net::OpenID::Extension.3
/usr/share/man/man3/Net::OpenID::Extension::SimpleRegistration.3
/usr/share/man/man3/Net::OpenID::ExtensionMessage.3
/usr/share/man/man3/Net::OpenID::IndirectMessage.3
/usr/share/man/man3/Net::OpenID::URIFetch.3
/usr/share/man/man3/Net::OpenID::Yadis.3
/usr/share/man/man3/Net::OpenID::Yadis::Service.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-OpenID-Common/LICENSE
