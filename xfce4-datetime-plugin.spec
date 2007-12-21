Summary:	A date and time panel plugin for the Xfce panel
Name:		xfce4-datetime-plugin
Version:	0.5.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-datetime-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-datetime-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-datetime-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/datetime.desktop
