Summary:	wmGrabImage grabs an image from the WWW and displays it
Summary(pl):	wmGrabImage wyci±ga obrazki ze stron WWW i wy¶wietla je
Name:		wmGrabImage
Version:	0.70
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Requires:	wget
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
wmGrabImage grabs an image from the WWW and displays it.

%description -l pl
wmGrabImage jest programem, który wyci±ga pliki graficzne ze stron
WWW, a potem je wy¶wietla.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name}/wmGrabImage	$RPM_BUILD_ROOT%{_bindir}
install %{name}/GrabImage	$RPM_BUILD_ROOT%{_bindir}
install %{name}/wmGrabImage.1	$RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1}		$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS CHANGES HINTS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,HINTS,TODO}.gz

%attr(755,root,root) %{_bindir}/wmGrabImage
%attr(755,root,root) %{_bindir}/GrabImage
%{_mandir}/man1/wmGrabImage.1*

%{_applnkdir}/DockApplets/wmGrabImage.desktop
