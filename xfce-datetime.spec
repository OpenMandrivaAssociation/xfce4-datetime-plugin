Summary: 	A date and time panel plugin for the Xfce panel
Name: 		xfce-datetime-plugin
Version: 	0.5.0
Release: 	%mkrel 1
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-datetime-plugin/xfce4-datetime-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.1.99.1
BuildRequires:	perl(XML::Parser)
BuildRequires:	xfce-panel-devel >= 4.1.99.1
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A date and time panel plugin for the Xfce panel.


%prep
%setup -q -n xfce4-datetime-plugin-%{version}

%build
%configure2_5x \
	--enable-final
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang xfce4-datetime-plugin

%clean
rm -rf %{buildroot}

%files -f xfce4-datetime-plugin.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/datetime.desktop
