Summary:	wmGrabImage grabs an image from the WWW and displays it
Summary(pl):	wmGrabImage wyci±ga obrazki ze stron WWW i wy¶wietla je
Name:		wmGrabImage
Version:	0.72
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tgz
# Source0-md5:	2cbd769b0cc909890ebdd48c2746f686
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
Requires:	ImageMagick
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	CFLAGS="%{rpmcflags} -Wall -I%{_includedir}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name}/wmGrabImage $RPM_BUILD_ROOT%{_bindir}
install %{name}/GrabImage $RPM_BUILD_ROOT%{_bindir}
install %{name}/wmGrabImage.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/wmGrabImage.desktop
%{_mandir}/man1/wmGrabImage.1*
