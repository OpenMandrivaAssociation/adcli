Name:		adcli
Version:	0.9.0
Release:	1
Summary:	System/Configuration/Networking
License:	LGPLv2+
URL:		http://cgit.freedesktop.org/realmd/adcli
Source0:	https://gitlab.freedesktop.org/realmd/adcli/-/archive/%{version}/adcli-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	krb5-devel
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	pkgconfig(com_err)
BuildRequires:	xmlto
Requires:	sasl-plug-gssapi

%description
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%prep
%autosetup -p1
./autogen.sh
%configure

%build
%make_build

%check
make check

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc %{_docdir}/%{name}
%{_sbindir}/adcli
%{_mandir}/*/*
