# MODIFY IN THE SVN

%define version 1.2.8
%define release %mkrel 1

%ifarch ppc64
%define build_option PERL_CHECKER_TARGET='debug-code BCSUFFIX=""'
%define require_ocaml /usr/bin/ocamlrun
%else
%define build_option %nil
%define require_ocaml %nil
%endif

Summary: Verify perl code
Name: perl_checker
Version: %{version}
Release: %{release}
License: GPL
Group: Development/Perl
Requires: perl-base >= 2:5.8.0 %{require_ocaml}
URL: http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/perl_checker
Source0: perl_checker-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ocaml >= 3.06
# for the faked packages:
AutoReqProv: 0

Obsoletes: perl-MDK-Common-devel <= 1.1.24
Provides: perl-MDK-Common-devel <= 1.1.24

%description
Various verifying scripts created for DrakX

%prep
%setup -q

%build
make %build_option

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std %build_option

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc src/perl_checker.html
%{_bindir}/*
%{_datadir}/perl_checker
%{_datadir}/vim/ftplugin/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*


