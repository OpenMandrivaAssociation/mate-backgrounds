%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Background images for the MATE desktop
Name:		mate-backgrounds
Version:	1.8.0
Release:	2
License:	GPLv2
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	mate-common

%description
This module contains a set of backgrounds packaged with the MATE desktop.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README AUTHORS
%{_datadir}/mate-background-properties/
%dir %{_datadir}/backgrounds/mate
%{_datadir}/backgrounds/mate/*

