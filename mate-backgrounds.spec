%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Background images for the MATE desktop
Name:		mate-backgrounds
Version:	1.18.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	mate-common

%description
This module contains a set of backgrounds packaged with the MATE desktop.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc NEWS README AUTHORS
%{_datadir}/mate-background-properties/
%dir %{_datadir}/backgrounds/mate
%{_datadir}/backgrounds/mate/*

