Summary: wmGrabImage grabs an image from the WWW and displays it
%define version 0.63
Name: wmGrabImage
Version: %{version}
Release: 1
Copyright: GPL
Group: X Windows/Window Managers
Source: ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Packager: Ian Macdonald <ianmacd@xs4all.nl>
BuildRoot: /var/tmp/%{name}-root
Requires: wget

%description
wmGrabImage grabs an image from the WWW and displays it.

%prep
%setup

%build
touch %{name}/%{name}.c
make -C %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m 755 %{name}/GrabImage $RPM_BUILD_ROOT/usr/X11R6/bin
#install -m 444 %{name}/%{name}.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

%files
%defattr(-,root,root)
/usr/X11R6/bin/%{name}
/usr/X11R6/bin/GrabImage
#/usr/X11R6/man/man1/%{name}.1
%doc BUGS CHANGES COPYING HINTS INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>

- first RPM release
