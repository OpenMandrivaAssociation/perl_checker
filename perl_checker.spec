# MODIFY IN THE SVN
%define debug_package %{nil}

%ifarch ppc64 %mips %arm aarch64
%define build_option PERL_CHECKER_TARGET='debug-code BCSUFFIX=""'
%else
%define build_option %{nil} 
%endif

Summary:	Verify Perl code
Name:		perl_checker
Version:	1.2.24
Release:	8
License:	GPLv2+
Group:		Development/Perl
Url:		http://svnweb.mageia.org/soft/perl_checker
Source0:	perl_checker-%version.tar.bz2
Patch0:	perl_checker-1.2.24-disable_test.patch
%ifnarch aarch64
BuildRequires:	ocaml >= 3.06
%endif
BuildRequires:	perl-MDK-Common
BuildRequires:	perl(Filesys::Df)
# for the faked packages:
AutoReqProv:	0
Obsoletes:	perl-MDK-Common-devel <= 1.1.24
Provides:	perl-MDK-Common-devel = 1.1.25

%description
Various verifying scripts created for DrakX.

%prep
%setup -q
%apply_patches

%build
make src/perl_checker %build_option
src/perl_checker --help

#CB Disable test for now as it causes weird errors on ABF
#%check
#make -C src/test

%install
%makeinstall_std %build_option

%files
%doc src/perl_checker.html
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*
%{_bindir}/*
%{_datadir}/perl_checker
%{_datadir}/vim/ftplugin/*

