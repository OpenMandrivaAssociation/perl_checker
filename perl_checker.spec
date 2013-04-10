# MODIFY IN THE SVN

%ifarch ppc64 %mips %arm
%define build_option PERL_CHECKER_TARGET='debug-code BCSUFFIX=""'
%else
%define build_option %nil 
%endif

Summary:	Verify Perl code
Name:		perl_checker
Version:	1.2.24
Release:	1
License:	GPLv2+
Group:		Development/Perl
URL:		http://svnweb.mageia.org/soft/perl_checker
Source0:	perl_checker-%version.tar.bz2
Patch0:		perl_checker-1.2.24-disable_test.patch
%ifarch ppc64 %mips %arm
# need ocamlrun
Requires:	ocaml
%endif
BuildRequires:	ocaml >= 3.06
BuildRequires:	perl-MDK-Common
BuildRequires:  perl(Filesys::Df)
# for the faked packages:
AutoReqProv:	0

Obsoletes:	perl-MDK-Common-devel <= 1.1.24
Provides:	perl-MDK-Common-devel = 1.1.25

%description
Various verifying scripts created for DrakX.

%prep
%setup -q
%patch0 -p1

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
%{_bindir}/*
%{_datadir}/perl_checker
%{_datadir}/vim/ftplugin/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.11-6mdv2011.0
+ Revision: 667472
- mass rebuild

* Sun Oct 24 2010 Thierry Vignaud <tv@mandriva.org> 1.2.11-5mdv2011.0
+ Revision: 587840
- fix summary
- fix license tag
- fix URL

* Sun Oct 24 2010 Thierry Vignaud <tv@mandriva.org> 1.2.11-4mdv2011.0
+ Revision: 587834
- fix testsuite

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 1.2.11-3mdv2010.0
+ Revision: 450268
- do not try to use ocamlopt on arm and mips
  (from Arnaud Patard)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.11-2mdv2010.0
+ Revision: 426602
- rebuild

* Fri Sep 26 2008 Thierry Vignaud <tv@mandriva.org> 1.2.11-1mdv2009.0
+ Revision: 288557
- re-allow "$object->state" and "sub state ..."
- ignore "use feature"

* Thu Sep 25 2008 Pixel <pixel@mandriva.com> 1.2.10-1mdv2009.0
+ Revision: 288112
- 1.2.10:
- recognize "state"
- fix typo causing qq(} $foo) to be parsed as q(} $foo)

* Wed Sep 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.9-1mdv2009.0
+ Revision: 285545
- fake_packages:
  o add Gtk2::Notify (which replaces Gtk2::NotificationBubble)
  o add Gtk2::Sexy
  o fix error in generated Glib

* Wed Sep 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.8-1mdv2009.0
+ Revision: 285529
- fake_packages:
  o fix error in generated Gtk2

* Wed Sep 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.7-1mdv2009.0
+ Revision: 285525
- fake_packages:
  o add URPM (for rpmdrake)

* Wed Sep 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.6-1mdv2009.0
+ Revision: 285523
- fake_packages:
  o add Gtk2::WebKit (for mcc)
  o update Glib & Gtk2

* Thu Sep 04 2008 Pixel <pixel@mandriva.com> 1.2.5-1mdv2009.0
+ Revision: 280818
- 1.2.5:
- recognize //=
- recognize file test "-o" (File is owned by effective uid.)
- don't die when @ISA packages are unknow, make it a warning instead

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.2.4-3mdv2009.0
+ Revision: 223588
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2.4-2mdv2008.1
+ Revision: 131296
- kill re-definition of %%buildroot on Pixel's request


* Thu Dec 21 2006 Pixel <pixel@mandriva.com> 1.2.4-2mdv2007.0
+ Revision: 101038
- new release, 1.2.4
- handle P(...) for plurals (similar to N(...))

* Tue Dec 12 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.2.3-2mdv2007.1
+ Revision: 95270
- x86_64 now has a native compiler but not ppc64

* Mon Dec 04 2006 Pixel <pixel@mandriva.com> 1.2.3-1mdv2007.1
+ Revision: 90410
- 1.2.3
- fake_packages:
  o add MDV::Distribconf methods used by urpm.pm
  o add Gtk2::Html2 (for mcc)
  o add a fake module for Gtk2::NotificationBubble so that network tools
  can be checked
  o update Gnome2::Vte
- fix some warnings:
  o don't suggest replacing "\l" with "l"
  o fix warning for "\"x'"
  o handle -z and -t (per titi request)
  o handle "use base 'Exporter'"
  o no warnings on: !our $foo

* Tue Nov 07 2006 Pixel <pixel@mandriva.com> 1.2.2-1mdv2007.0
+ Revision: 77297
- urpm.pm and URPM/Resolve.pm are now perl_checker compliant
- moved SVN repository out of perl-MDK-Common to its own dir
- %%INC is known

* Thu Oct 26 2006 Pixel <pixel@mandriva.com> 1.1.31-1mdv2007.1
+ Revision: 72699
- Curses::UI: add Dialog::Progress methods

* Sat Oct 21 2006 Pixel <pixel@mandriva.com> 1.1.30-1mdv2007.0
+ Revision: 71565
- add a few more functions to Curses/UI.pm and Curses

* Thu Oct 19 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.1.29-1mdv2007.1
+ Revision: 66619
- sync with Glib & Gtk2 bindings 1.140
- sync with Gnome2-Vte-0.06
- sync with Gnome2-1.040

* Thu Oct 19 2006 Pixel <pixel@mandriva.com> 1.1.28-1mdv2007.0
+ Revision: 66598
- new release
- added fake package Curses::UI
- remove false warning for "\c"
- detect some unreachable code (code following exit/die/...)
- new release
- added fake package Curses::UI
- remove false warning for "\c"
- detect some unreachable code (code following exit/die/...)
- Import perl_checker

* Thu Aug 24 2006 Pixel <pixel@mandriva.com> 1.1.27-1mdv2007.0
- add fake MDV::Distribconf

* Thu Jun 22 2006 Pixel <pixel@mandriva.com> 1.1.26-1mdv2007.0
- handle $o->pop

* Fri Jun 16 2006 Pixel <pixel@mandriva.com> 1.1.25-1mdv2007.0
- handle "use base ..."
- add a fake packdrake.pm

* Thu Jun 15 2006 Pixel <pixel@mandriva.com> 1.1.24-1mdv2007.0
- "pop @l" return value can be dropped (ie make it similar to "shift")

* Tue May 16 2006 Pixel <pixel@mandriva.com> 1.1.23-1mdk
- it seems stack is smaller on amd64, function concat_spaces need to be tail-recursive

* Wed Apr 12 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.1.22-1mdk
- sync with Glib/Gtk2-1.120

* Fri Nov 25 2005 Pixel <pixel@mandriva.com> 1.1.21-1mdk
- renamed package from perl-MDK-Common-devel to perl_checker
- new option --generate-package-dependencies-graph

* Fri Nov 26 2004 Pixel <pixel@mandrakesoft.com> 1.1.20-2mdk
- new checks

* Wed Nov 10 2004 Pixel <pixel@mandrakesoft.com> 1.1.19-1mdk
- various enhancements/fixes

* Thu Aug 19 2004 Pixel <pixel@mandrakesoft.com> 1.1.17-3mdk
- use DESTDIR
- add perl_checker-vim
- add Ctrl-return in perl and cperl emacs mode
- fake Getopt::Long

* Thu Aug 12 2004 Pixel <pixel@mandrakesoft.com> 1.1.17-2mdk
- various enhancements/fixes

* Sat Jul 24 2004 Pixel <pixel@mandrakesoft.com> 1.1.15-2mdk
- workaround bug in ocaml on ultrasparc 
  (can't catch exception "Fatal error: out-of-bound access in array or string" in native code)

* Tue May 11 2004 Pixel <pixel@mandrakesoft.com> 1.1.12-1mdk
- many enhancements and cleanup

* Thu Apr 08 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.11-4mdk
- perl_checker:
  o add perl_checker.html
  o add testsuite
  o fix detecting of boolean context vs scalar context
  o fix some warning
  o in "$a ? $a : xxx", "xxx" can need short circuit
  o recognize "-c" function
  o turn some errors to warnings
- perl_checker's faked packages:
  o sync with glib/gtk+ 2.4.0
  o support Gnome2 and Gnome2::Vte too

* Fri Feb 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.10-2mdk
- update gtk2-perl binding fake package

* Tue Jan 13 2004 Pixel <pixel@mandrakesoft.com> 1.1.11-1mdk
- sync perl_checker_fake_packages/{Glib,Gtk2}.pm
- fix build time overflow in cache

* Fri Jan 09 2004 Pixel <pixel@mandrakesoft.com> 1.1.10-2mdk
- entries in generated pot file are sorted by files

* Mon Jan 05 2004 Pixel <pixel@mandrakesoft.com> 1.1.9-1mdk
- many enhancements

