%define upstream_name    HTML-TreeBuilder-LibXML
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	HTML::Element compatible API for HTML::TreeBuilder::LibXML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-TreeBuilder-LibXML-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(HTML::TreeBuilder::XPath)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(XML::LibXML)
BuildArch:	noarch

%description
HTML::TreeBuilder::XPath is libxml based compatible interface to
HTML::TreeBuilder, which could be slow for a large document.

HTML::TreeBuilder::LibXML is drop-in-replacement for
HTML::TreeBuilder::XPath.

This module doesn't implement all of HTML::TreeBuilder and HTML::Element
APIs, but eough methods are defined so modules like Web::Scraper work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.120.0-3mdv2011.0
+ Revision: 654346
- rebuild for updated spec-helper

* Mon Dec 06 2010 Shlomi Fish <shlomif@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 612977
- Bumped the rel to rebuild
- import perl-HTML-TreeBuilder-LibXML


