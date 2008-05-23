# NOTE:
# Wammu must be build with python-gammu rebuild against current gammu-devel

Summary:	Wammu - Gammu GUI - Mobile phone manager
Summary(pl.UTF-8):	Wammu - interfejs graficzny dla Gammu
Name:		wammu
Version:	0.27
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.cihar.com/wammu/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	2d1761b34ff2af56d149319b59a37905
URL:		http://wammu.eu/
BuildRequires:	gammu-devel >= 1:1.11.91
BuildRequires:	pkgconfig >= 1:0.21-2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gammu >= 0.24
BuildRequires:	python-wxPython
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
Requires:	gammu
Requires:	obexfs
Requires:	obextool
Requires:	python-gammu >= 0.24
Requires:	python-wxPython
Suggests:	bluez-gnome
Suggests:	python-pybluez
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wammu is mobile phone manager running on Linux, Windows and possibly
other platforms, where Gammu and wxPython works. The communication is
made by Gammu library. Currently supported features:

* complete support for contacts, todo, calendar
* can read/create/save/send/backup SMSes
* sending files to phone (OBEX and Sony Ericsson phones only)
* SMS composer for multi part SMSes
* display message including pictures and ringtones playback
* support for backup and import in various formats
	(vCard, vCalendar, vTodo, iCalendar, gammu own backup, ...)
* export messages to mail (IMAP4, maildir and mailbox storages)
* searching for phone

%description -l pl.UTF-8
Wammu to zarządca telefonów komórkowych działający pod Linuksem,
Windows i być może na innych platformach, na których działa Gammu i
wxPython. Komunikacja jest wykonywana przez bibliotekę Gammu.
Aktualnie dostępne możliwości:
- pełna obsługa kontaktów, listy zadań, kalendarza
- odczyt przeczytanych/utworzonych/zapisanych/wysłanych/zachowanych
  SMS-ów
- przesyłanie plików do telefonu (tylko OBEX i telefony Sony Ericsson)
- narzędzie do tworzenia wieloczęściowych SMS-ów
- wyświetlanie komunikatów wraz z obrazkami i dzwonkami
- obsługa kopii bezpieczeństwa i importu z różnych formatów
  (vCard, vCalendar, vTodo, iCalendar, własny format kopii Gammu...)
- eksport wiadomości do e-maili (IMAP4, maildir i mailbox)
- szukanie telefonów

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
%{_mandir}/man1/%{name}*.*
%dir %{_datadir}/Wammu
%{_datadir}/Wammu/*
%{_desktopdir}/%{name}.desktop
