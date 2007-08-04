Summary:	Wammu - Gammu GUI - Mobile phone manager
Summary(pl.UTF-8):	Wammu - interfejs graficzny dla Gammu
Name:		wammu
Version:	0.21
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.cihar.com/wammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	6bd3fa7e8842a3713d9534ccb1a5d777
URL:		http://wammu.eu/
BuildRequires:	gammu-devel >= 1:1.11.91
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gammu >= 0.20
BuildRequires:	python-wxPython
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
Requires:	gammu
Requires:	obexfs
Requires:	obextool
Requires:	python-gammu >= 0.20
Requires:	python-wxPython
Suggests:	bluez-gnome
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wammu is mobile phone manager running on Linux, Windows and possibly
other platforms, where Gammu and wxPython works. The communication is
made by Gammu library. Currently supported features:

* complete support for contacts,todo,calendar
* can read/create/save/send/backup smses
* sending files to phone (OBEX and Sony Ericsson phones only)
* sms composer for multi part smses
* display message including pictures and ringtones playback
* support for backup and import in various formats 
	(vCard, vCalendar, vTodo, iCalendar, gammu own backup,...)
* export messages to mail (IMAP4, maildir and mailbox storages )
* searching for phone

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ NEWS README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/%{name}.*
%dir %py_sitescriptdir/Wammu
%{py_sitescriptdir}/Wammu/*
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/%{name}.*
%dir %{_datadir}/Wammu
%{_datadir}/Wammu/*
%{_desktopdir}/%{name}.desktop
