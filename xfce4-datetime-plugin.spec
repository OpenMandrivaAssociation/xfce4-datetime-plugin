Summary:	A date and time panel plugin for the Xfce panel
Name:		xfce4-datetime-plugin
Version:	0.6.2
Release:	4
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
