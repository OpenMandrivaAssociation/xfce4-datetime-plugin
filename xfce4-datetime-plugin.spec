%define _disable_rebuild_configure 1
%define url_ver %(echo %{version} | cut -d. -f1,2)

Summary:	A date and time panel plugin for the Xfce panel
Name:		xfce4-datetime-plugin
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-datetime-plugin/%{url_ver}/xfce4-datetime-plugin-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxfce4ui-2)

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
