# TODO:
# - desktop file and icons
Summary:	OSD mail notifier
Summary(pl):	Powiadamianie o poczcie poprzez OSD
Name:		osd_mail
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.hellion.org.uk/source/%{name}-%{version}.tar.gz
URL:		http://www.hellion.org.uk/osd_mail/
BuildRequires:	XFree86-devel
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
osd_mail watches a set of mbox style mail boxes for new mail and
displays on screen the names of those containing new mail.

%description -l pl
osd_mail nadzoruje zestaw skrzynek pocztowych w stylu mbox i wy�wietla
na ekranie nazwy tych, w kt�rych jest nowa poczta.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
