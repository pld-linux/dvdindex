Summary:	dvdindex is a free, open-source CD/DVD archiving utility to manage a collection of CDs/DVDs
Name:		dvdindex
Version:	0.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/dvdindex/%{name}-%{version}.tar.gz
# Source0-md5:	8875b406d9d731164466e9278efb4e39
URL:		http://dvdindex.sourceforge.net/
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvdindex is a free, open-source CD/DVD archiving utility to manage a
collection of CDs/DVDs.


%prep
%setup -q -n %{name}

%build
qmake
%{__make} QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
