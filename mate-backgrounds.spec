Summary:	Background images for the MATE desktop
Name:		mate-backgrounds
Version:	1.2.1
Release:	1
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	mate-common

%description
This module contains a set of backgrounds packaged with the MATE desktop.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS
%{_datadir}/mate-background-properties/
%dir %{_datadir}/pixmaps/backgrounds/mate
%{_datadir}/pixmaps/backgrounds/mate/*

