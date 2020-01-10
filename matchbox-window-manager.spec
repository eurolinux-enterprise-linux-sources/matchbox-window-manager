%define libmatchbox_devel_ver 1.9-2
%define alphatag 20070628svn

Summary:       Window manager for the Matchbox Desktop
Name:          matchbox-window-manager
Version:       1.2
Release:       16.1.%{alphatag}%{?dist}
Url:           http://projects.o-hand.com/matchbox/
# svn checkout http://svn.o-hand.com/repos/matchbox/trunk/matchbox-window-manager
License:       GPLv2+
Group:         User Interface/Desktops
Source0:       %{name}-%{version}-%{alphatag}.tar.gz

Patch1: matchbox-window-manager-1.2-keysyms.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1284728
Patch10: zero-height-width.patch

Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  pkgconfig 
BuildRequires:  expat-devel
BuildRequires:  libmatchbox-devel >= %{libmatchbox_devel_ver}
BuildRequires:  startup-notification-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pango-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXcursor-devel
Requires:       filesystem

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the window manager from Matchbox.

%prep
%setup -q

%patch1 -p2 -b .keysyms
%patch10 -p1 -b .zero

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog COPYING
%{_bindir}/*
%dir %{_sysconfdir}/matchbox
%config(noreplace) %{_sysconfdir}/matchbox/kbdconfig
%dir %{_datadir}/matchbox
%{_datadir}/matchbox/*
%{_datadir}/themes/*

%changelog
* Thu Apr 14 2016 Petr Lautrbach <plautrba@redhat.com> - 1.2-16.20070628svn
- Do not try to compute new proportions when one of the original is 0 (#1284728)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.2-15.20070628svn
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-14.20070628svn
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13.20070628svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.2-12.20070628svn
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.2-11.20070628svn
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10.20070628svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9.20070628svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Adam Jackson <ajax@redhat.com> 1.2-8.20070628svn
- Rebuild for libpng 1.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7.20070628svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6.20070628svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5.20070628svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2-4.20070628svn
- fix license tag

* Sun Mar  9 2008 Marco Pesenti Gritti <mpg@redhat.com> - 1.2-3.20070628svn
- Add dist tag

* Fri Nov  9 2007 Marco Pesenti Gritti <marco@localhost.localdomain> - 1.2-3.20070628svn
- Add patch to fix some keybindings

* Thu Jun 28 2007 Marco Pesenti Gritti <mpg@redhat.com> - 1.2-2.20070628svn
- New snapshot

* Tue Jun 19 2007 Marco Pesenti Gritti <mpg@redhat.com> 1.2-1
- Update source to 1.2

* Tue Jun 19 2007 John (J5) Palmieri <johnp@redhat.com> 1.9-3
- Fix buildroot
- Add COPYING license file to docs
- Added {} braces around % macros
- Own {_sysconfdir}/matchbox directory
- Own {_datadir}/matchbox

* Sat Feb 24 2007 Marco Pesenti Gritti <mpg@redhat.com> 1.1-6.cvs20072402.6
- Update to cvs20072402

* Wed Jan 31 2007 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20073101.6
- Update to cvs20073101

* Wed Dec 20 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20061219.5
- Build with Xcursor support

* Tue Dec 19 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20061219.4
- Update to cvs20061219

* Tue Oct 17 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20060911.3
- Temporarily drop composite

* Thu Oct  5 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20060911.2
- Enable composite
- Add some composite dependencies

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20060911.1
- Remove some gconf leftovers

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-5.cvs20060911.0
- Rebuild

* Mon Sep 11 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-cvs20060911-1
- Update

* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-3
- Rebuild
- Depend on libmatchbox 1.9-2
- Do not package gconf schemas

* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-3
- Build with the default options

* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-2
- Missing build reqs

* Mon Aug 21 2006 Marco Pesenti Gritti <mpg@redhat.com> 1.1-1
- Update to 1.1

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 0.9.5-1mdk
- New release 0.9.5

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 0.9.4-1mdk
- 0.9.4
- new URLs

* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.9.2-1mdk
- 0.9.2

* Mon Jan 10 2005 Austin Acton <austin@mandrake.org> 0.9-1mdk
- 0.9

* Wed Sep 29 2004 Austin Acton <austin@mandrake.org> 0.8.4-1mdk
- 0.8.4

* Mon Aug 23 2004 Austin Acton <austin@mandrake.org> 0.8.3-2mdk
- fix schemas

* Mon Aug 23 2004 Austin Acton <austin@mandrake.org> 0.8.3-1mdk
- 0.8.3

* Tue Aug 10 2004 Austin Acton <austin@mandrake.org> 0.8.2-3mdk
- buildrequires xsettings

* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.8.2-1mdk
- enable startup-notification

* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 0.8.2-1mdk
- 0.8.2

