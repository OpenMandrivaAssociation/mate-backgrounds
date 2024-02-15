%define mate_ver	%(echo %version | cut -d\. -f1-2)

Summary:	Background images for the MATE desktop
Name:		mate-backgrounds
Version:	1.28.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	autoconf-archive
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk-doc)

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a set of backgrounds images and data packaged with the
MATE desktop.

%files
%doc NEWS README AUTHORS
%{_datadir}/mate-background-properties/
%dir %{_datadir}/backgrounds/mate
%{_datadir}/backgrounds/mate/*

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

# locales
#find_lang %{name} --with-gnome --all-name

