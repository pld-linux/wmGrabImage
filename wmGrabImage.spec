Summary:	wmGrabImage grabs an image from the WWW and displays it
Summary(pl):	wmGrabImage wyci�ga obrazki ze stron WWW i wy�wietla je
Name:		wmGrabImage
Version:	0.70
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	f77223e45fbcb7056eb4ae9393c3f601
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Requires:	wget
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmGrabImage grabs an image from the WWW and displays it.

%description -l pl
wmGrabImage jest programem, kt�ry wyci�ga pliki graficzne ze stron
WWW, a potem je wy�wietla.

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
#install %{SOURCE1}		$RPM_BUILD_ROOT%{_applnkdir}/DockApplets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HINTS TODO
%attr(755,root,root) %{_bindir}/wmGrabImage
%attr(755,root,root) %{_bindir}/GrabImage
%{_mandir}/man1/wmGrabImage.1*
#%%{_applnkdir}/DockApplets/wmGrabImage.desktop
