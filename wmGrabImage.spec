Summary:	wmGrabImage grabs an image from the WWW and displays it
Summary(pl):	wmGrabImage wyci±ga obrazki ze stron WWW i wy¶wietla je
Name: 		wmGrabImage
Version:	0.63
Release:	3
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmGrabImage.desktop
Requires: 	wget
BuildPrereq:    XFree86-devel
BuildPrereq:    xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix		/usr/X11R6

%description
wmGrabImage grabs an image from the WWW and displays it.

%description -l pl
wmGrabImage jest programem, który wyci±ga pliki graficzne ze stron
WWW, a potem je wy¶wietla.

%prep
%setup -q

%build
make -C %{name} clean
make -C %{name} \
        CFLAGS="$RPM_OPT_FLAGS -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
        $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

install -s %{name}/wmGrabImage $RPM_BUILD_ROOT/usr/X11R6/bin
install %{name}/GrabImage $RPM_BUILD_ROOT/usr/X11R6/bin
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf BUGS CHANGES HINTS 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS}.gz

%attr(755,root,root) %{_bindir}/wmGrabImage
%attr(755,root,root) %{_bindir}/GrabImage

/etc/X11/applnk/DockApplets/wmGrabImage.desktop

%changelog
* Sat May 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.63-3]
- spec file modified for PLD use,
- package is FHS 2.0 compliant.

* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release.
