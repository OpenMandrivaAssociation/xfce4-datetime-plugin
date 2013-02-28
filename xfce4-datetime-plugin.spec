Summary:	A date and time panel plugin for the Xfce panel
Name:		xfce4-datetime-plugin
Version:	0.6.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-datetime-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxfce4ui-1)

%description
A date and time panel plugin for the Xfce panel.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel/plugins/libdatetime.so
%{_datadir}/xfce4/panel/plugins/datetime.desktop


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-4mdv2010.1
+ Revision: 543422
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-3mdv2010.0
+ Revision: 445982
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-2mdv2009.1
+ Revision: 349449
- rebuild for xfce-4.6.0

* Thu Nov 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 305323
- update to new version 0.6.1

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-2mdv2009.1
+ Revision: 294992
- rebuild for new Xfce4.6 beta1

* Fri Jul 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 231697
- add buildrequires on intltool
- update to new version 0.6.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-2mdv2008.1
+ Revision: 110115
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- spec file clean
- use upstream name

* Thu May 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5.0-1mdv2008.0
+ Revision: 30458
- Fix File list

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update url
    - spec file clean
    - new version

